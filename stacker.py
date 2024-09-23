from max7219 import Max7219
from machine import Pin, SPI
from num import Number
import time
import gc


# ======= Stacker Layout ==========#
# ========X16==========
#                   0 |
#                     |
#                     |
#                     |
#                     Y
#                     64
#                     |
#                     |
#                     |
#                     |
#                     |
# ========X16==========



class Stacker():
    gc.enable()
    spi = SPI
    DISPLAY_HIGHT = 64
    DISPLAY_WIDTH = 16
    #Rect List Indexes
    LAST_INDEX = -1
    PENULTIMATE_INDEX = -2
    shape_hight = 4
    shape_width = 5
    shape_y_position = DISPLAY_HIGHT - shape_hight
    shape_x_position = 0
    v_line_x_position = 0
    rc_shape_x_position = 0 #right corner_shape_x_position
    lc_shape_x_position = 0 #left_corner_shape_x_position
    increment_position = 1
    button_flag = 1
    rect_list = []
    dropdown_animation_time = 40000
    interval_time = 100000
    interval = interval_time
    high_score = "0000"
    current_score = "0000"
    
    
    def __init__(self):
        """Init Display(screen), Button, time variables"""
        self.spi = Stacker.spi(0, baudrate=10000000, polarity=1, phase=0, sck=Pin(2), mosi=Pin(3))
        self.ss = Pin(5, Pin.OUT)       
        self.screen = Max7219(Stacker.DISPLAY_HIGHT, Stacker.DISPLAY_WIDTH, self.spi, self.ss)    
        self.button = Pin(16, Pin.IN, Pin.PULL_UP)
        self.start_time = time.ticks_us()
        self.start_time_dropdown = time.ticks_us()
        self.start_time_color_change = time.ticks_us()
        
        self.screen.brightness(5)
        
        Stacker.high_score = str(self.read_from_file("highscore.txt"))

              
    def string_to_digit(self, char):
        """Transforms the equivalent of an character from a string to Number Class"""

        if char == "1":
            return Number.one
        elif char == "2":
            return Number.two
        elif char == "3":
            return Number.three
        elif char == "4":
            return Number.four
        elif char == "5":
            return Number.five
        elif char == "6":
            return Number.six
        elif char == "7":
            return Number.seven
        elif char == "8":
            return Number.eight
        elif char == "9":
            return Number.nine
        else:
            return Number.zero
        
               
    def draw_score(self):
        """Draws score after Game Over"""
        char_row_x_pos = 17
        text_row_x_pos = 1
        char_y_pos = 15
        high_score_list = [x for x in Stacker.high_score]
        current_score_list = [x for x in str(Stacker.current_score)]
        word_list = [Number.Scor, Number.High, Number.Your]
        wl_index_sequance = [1,0,2,0]
        
        #Draw Text High Score, Curent Score
        for index in range(4):
            counter = 0
            for i in range(6):
                for j in range(16):
                    y = 15
                    self.screen.pixel(text_row_x_pos + i, y - j, word_list[wl_index_sequance[index]][i][j])
            if index == 1:
                text_row_x_pos += 12
            text_row_x_pos += 8
        
        #Draw High Score, Curent Score
        for h_char, c_char in zip(high_score_list, current_score_list):
            for i in range(6):
                x = char_row_x_pos
                for j in range(4):
                    y = char_y_pos
                    self.screen.pixel(x + i, y - j, self.string_to_digit(h_char)[i][j])
                    self.screen.pixel((x + 28) + i, y - j, self.string_to_digit(c_char)[i][j])
            char_y_pos += -4
        
        self.screen.show()
        time.sleep(5)
        
    
    def create_shape(self, y_position, x_position, hight, lenght, color=1):
        """Create a shape"""
        self.screen.fill_rect(y_position,
                      x_position,
                      hight,
                      lenght,
                      color)
        
        
    def draw_v_line(self, x_pos):
        """Draw a v line, the screen it's rotated 90 degrees,
           the line shows as horizontal
        """
        self.screen.vline(x_pos, 0, 16, 1)
        
        
    def refresh_obj_in_list(self, r_list, direction = 1):
        """Updates last index in shape list"""
        if direction == 1: #Direction, Moving Right to Left <--
            r_list[Stacker.LAST_INDEX][3] = Stacker.shape_width
            r_list[Stacker.LAST_INDEX][5] = Stacker.rc_shape_x_position + Stacker.shape_width
            
        elif direction == 0: #Direction, Moving Left to Right -->
            r_list[Stacker.LAST_INDEX][3] = Stacker.shape_width
            r_list[Stacker.LAST_INDEX][4] = Stacker.rc_shape_x_position + (r_list[Stacker.PENULTIMATE_INDEX][3] - Stacker.shape_width)
            Stacker.shape_x_position = r_list[Stacker.LAST_INDEX][4]
        if Stacker.shape_width == 1:
            r_list[Stacker.LAST_INDEX][5] = r_list[Stacker.LAST_INDEX][4]
                
                
    def trim_shape(self, r_list, tslc, tsrc, bslc, bsrc):
        """Trim the original shape"""
        if Stacker.shape_width != 1:
            if tslc > bslc and tsrc > bsrc: #Top Shape on Left Side
                Stacker.shape_width = (bslc - tsrc)
                self.refresh_obj_in_list(r_list, direction = 1)
                self.shape_dropdown_animation((r_list[Stacker.PENULTIMATE_INDEX][3] - Stacker.shape_width) , (r_list[Stacker.LAST_INDEX][4] + Stacker.shape_width)) #Start drop Down Animation
            
            elif tslc < bslc and tsrc < bsrc: #Top Shape on Right Side
                Stacker.shape_width = (tslc - bsrc)
                self.refresh_obj_in_list(r_list, direction = 0)
                self.shape_dropdown_animation((r_list[Stacker.PENULTIMATE_INDEX][3] - Stacker.shape_width) , (r_list[Stacker.LAST_INDEX][4] - (r_list[Stacker.PENULTIMATE_INDEX][3] - Stacker.shape_width)))
                    

    def shape_dropdown_animation(self, n_shape_width, n_shape_x_pos):
        """Creates an animation from the results of trim_shape() method"""
        n_shape_y_pos = Stacker.shape_y_position
        color = 1
        while True:
            self.screen.fill(0)
            self.draw_v_line(Stacker.v_line_x_position)
            for i in Stacker.rect_list:
                self.create_shape(i[0],
                                  i[4],
                                  i[2],
                                  i[3])
             
            self.create_shape(n_shape_y_pos,
                              n_shape_x_pos,
                              Stacker.shape_hight,
                              n_shape_width,
                              color)
            
            self.screen.show()

            current_time = time.ticks_us()
            
            if (current_time - self.start_time_dropdown) >= Stacker.dropdown_animation_time:
                n_shape_y_pos += 1
                self.start_time_dropdown = current_time
                
            #Flip color 1 or 0
            if (current_time - self.start_time_color_change) >= 2000:
                color = not color
                self.start_time_color_change = current_time
                
            if n_shape_y_pos > Stacker.DISPLAY_HIGHT:
                break
                
    
    def write_to_file(self, file_name, data):
        f = open(f"{file_name}", "w")
        f.write(str(data))
        f.close()


    def read_from_file(self, file_name):
        f = open(f"{file_name}")
        data = f.read()
        f.close()
        
        return data


    def restart_game(self, restart_interval = False):
        """Restarts the game. If the restart_interval = True, all variables
           are set to default
        """
        self.screen.fill(0)
        Stacker.rect_list = []
        Stacker.shape_width = 5
        Stacker.shape_y_position = Stacker.DISPLAY_HIGHT - Stacker.shape_hight
        Stacker.high_score = self.read_from_file("highscore.txt")
        
        #Restart the game if shape dosen t stack one top of last one
        if restart_interval:
            Stacker.interval = Stacker.interval_time 
            self.draw_score()
            Stacker.current_score = "0000"
            Stacker.v_line_x_position = 0
            
        if int(Stacker.current_score) > int(Stacker.high_score):
            self.write_to_file("highscore.txt", Stacker.current_score)
                
              
    def check_win(self, r_list):
        if len(r_list) > 1:
            tsrc = r_list[Stacker.LAST_INDEX][4] # Top Shape Right Corner
            tslc = r_list[Stacker.LAST_INDEX][5] # Top Shape Left Corner
            bsrc = r_list[Stacker.PENULTIMATE_INDEX][4] # Bottom Shape Right Corner
            bslc = r_list[Stacker.PENULTIMATE_INDEX][5] # Bottom Shape Left Corner
            
            #if shape do not stack on top o each other, reset.
            if (Stacker.shape_width != 1 and (tslc <= bsrc or tsrc >= bslc)):
                self.restart_game(True)
            elif (tslc < bsrc or tsrc > bslc):
                self.restart_game(True)
            else:  
                self.trim_shape(r_list, tslc, tsrc, bslc, bsrc)
               
        if (r_list[Stacker.LAST_INDEX][0] <= Stacker.v_line_x_position):

            Stacker.interval -= 20000
            Stacker.v_line_x_position += 8
            self.restart_game()
        
        
    def screen_update(self):
        self.screen.fill(0)
        self.draw_v_line(Stacker.v_line_x_position)
#         self.draw_score()
        for i in Stacker.rect_list:
            self.create_shape(i[0],
                              i[4],
                              i[2],
                              i[3])
         
        self.create_shape(Stacker.shape_y_position,
                          Stacker.shape_x_position,
                          Stacker.shape_hight,
                          Stacker.shape_width)
        
        self.screen.show()

        
    def play_game(self):
        while True:
            current_time = time.ticks_us()
            Stacker.rc_shape_x_position = Stacker.shape_x_position
            Stacker.lc_shape_x_position = Stacker.shape_x_position + Stacker.shape_width
            if Stacker.shape_width == 1:
                Stacker.lc_shape_x_position = Stacker.rc_shape_x_position
            self.screen_update()
                 
            if self.button.value() == 0 and Stacker.button_flag:
                Stacker.button_flag = 0

                shape_list = [Stacker.shape_y_position,#store y Position
                              Stacker.shape_x_position,#store x Position
                              Stacker.shape_hight,#store shape hight
                              Stacker.shape_width,#store shape lenght
                              Stacker.rc_shape_x_position,#store right corner x Position
                              Stacker.lc_shape_x_position#store left corner x Position
                              ]
                
                Stacker.rect_list.append(shape_list)
                Stacker.current_score = str("{:04d}").format(int(Stacker.current_score) + 10)
                Stacker.shape_y_position -= Stacker.shape_hight
                self.check_win(Stacker.rect_list)
          
            if self.button.value() == 1 and Stacker.button_flag == 0:
                Stacker.button_flag = 1

            if (current_time - self.start_time) >= Stacker.interval:
                self.start_time = current_time
                Stacker.shape_x_position += Stacker.increment_position
      
            #Shift direction left <-> right    
            if Stacker.shape_x_position >= Stacker.DISPLAY_WIDTH - Stacker.shape_width:
                Stacker.increment_position = -1
            elif Stacker.shape_x_position <= 0:
                Stacker.increment_position = 1
                
#             print("Mem Aloc  ", gc.mem_alloc())
#             print("Mem Free  ",gc.mem_free())
                

                
                


