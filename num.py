


class Number:
    zero = [[0,1,1,0],
        [1,0,0,1],
        [1,0,0,1],
        [1,0,0,1],
        [1,0,0,1],
        [0,1,1,0]]

    one = [[0,0,1,0],
         [0,1,1,0],
         [0,0,1,0],
         [0,0,1,0],
         [0,0,1,0],
         [0,0,1,0]]

    two = [[0,1,1,0],
         [1,0,0,1],
         [0,0,0,1],
         [0,0,1,0],
         [0,1,0,0],
         [1,1,1,1]]

    three =  [[0,1,1,0],
             [1,0,0,1],
             [0,0,1,1],
             [0,0,1,1],
             [1,0,0,1],
             [0,1,1,0]]

    four =   [[1,0,0,0],
             [1,0,1,0],
             [1,0,1,0],
             [1,1,1,1],
             [0,0,1,0],
             [0,0,1,0]]

    five =   [[1,1,1,1],
             [1,0,0,0],
             [1,1,1,0],
             [0,0,0,1],
             [1,0,0,1],
             [0,1,1,0]]

    six =   [[0,1,1,0],
             [1,0,0,0],
             [1,1,1,0],
             [1,0,0,1],
             [1,0,0,1],
             [0,1,1,0]]

    seven =  [[1,1,1,1],
             [0,0,0,1],
             [0,0,1,0],
             [0,0,1,0],
             [0,0,1,0],
             [0,0,1,0]]

    eight =  [[1,1,1,1],
             [1,0,0,1],
             [1,1,1,1],
             [1,0,0,1],
             [1,0,0,1],
             [1,1,1,1]]

    nine =  [[1,1,1,1],
             [1,0,0,1],
             [1,1,1,1],
             [0,0,0,1],
             [0,0,0,1],
             [1,1,1,1]]
    
    High = [[1,0,0,1,0,1,0,0,1,1,0,0,1,0,0,0],
            [1,0,0,1,0,0,0,1,0,0,1,0,1,0,0,0],
            [1,1,1,1,0,1,0,1,1,1,1,0,1,0,0,0],
            [1,0,0,1,0,1,0,0,0,0,1,0,1,1,1,0],
            [1,0,0,1,0,1,0,1,1,0,1,0,1,0,0,1],
            [1,0,0,1,0,1,0,1,1,1,0,0,1,0,0,1]]
    
    Scor = [[0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,1,0,1,1,0,0,1,1,0,0,1,1,0],
            [0,1,0,0,1,0,0,1,1,0,0,1,0,1,0,1],
            [0,0,1,0,1,0,0,0,1,0,0,1,0,1,0,0],
            [1,0,0,1,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,1,0,0,1,1,0,0,1,1,0,0,1,0,0]]
    
    
    Your = [[1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
            [0,1,0,1,0,1,1,0,0,1,0,0,1,0,1,1],
            [0,0,1,0,1,0,0,1,0,1,0,0,1,0,1,0],
            [0,0,1,0,1,0,0,1,0,1,0,0,1,0,1,0],
            [0,0,1,0,0,1,1,0,0,0,1,1,0,0,1,0]]
    

    
#     S = [[0,1,1,0],
#          [1,0,0,1],
#          [0,1,0,0],
#          [0,0,1,0],
#          [1,0,0,1],
#          [0,1,1,0]]
#     
#     c = [[0,0,0,0],
#          [0,1,1,0],
#          [1,0,0,1],
#          [1,0,0,0],
#          [1,0,0,1],
#          [0,1,1,0]]
#     
#     o =  [[0,0,0,0],
#          [0,1,1,0],
#          [1,0,0,1],
#          [1,0,0,1],
#          [1,0,0,1],
#          [0,1,1,0]]
#     
#     r =  [[0,0,0,0],
#          [0,1,1,0],
#          [0,1,0,1],
#          [0,1,0,0],
#          [0,1,0,0],
#          [0,1,0,0]]
#     
#     
#     e =  [[0,0,0,0],
#          [0,1,1,0],
#          [1,0,0,1],
#          [1,1,1,0],
#          [1,0,0,0],
#          [0,1,1,0]]
    
#     
#     H =   [[1,0,0,1],
#          [1,0,0,1],
#          [1,1,1,1],
#          [1,0,0,1],
#          [1,0,0,1],
#          [1,0,0,1]]
#     
#     
#     i =   [[0,1,0,0],
#              [0,0,0,0],
#              [0,1,0,0],
#              [0,1,0,0],
#              [0,1,0,0],
#              [0,0,0,0]]
#     
#     
#     g =    [[0,1,1,0],
#              [1,0,0,1],
#              [1,1,1,1],
#              [0,0,0,1],
#              [1,1,0,1],
#              [1,1,1,0]]
#     
#     
#     h =  [[1,0,0,0],
#          [1,0,0,0],
#          [1,1,1,0],
#          [1,0,0,1],
#          [1,0,0,1],
#          [1,0,1,1]]
    




