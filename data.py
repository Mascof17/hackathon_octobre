#
# some predefined problems
#
# the conventions here are
# - board:  0 is for a place that must be covered by a piece
#           1 is for obstacles - should not be filled
# - pieces: 1 means there is some material at this location
#           0 where there is just air

import numpy as np
import exact_cover

DTYPE = exact_cover.io.DTYPE_FOR_ARRAY

RAW_SHAPES = {
    "F": [np.array([[1, 1, 0], [0, 1, 1], [0, 1, 0]])],
    "I": [np.array([[1, 1, 1, 1, 1]])],
    "L": [np.array([[1, 0, 0, 0], [1, 1, 1, 1]])],
    "N": [np.array([[1, 1, 0, 0], [0, 1, 1, 1]])],
    "P": [np.array([[1, 1, 1], [1, 1, 0]])],
    "T": [np.array([[1, 1, 1], [0, 1, 0], [0, 1, 0]])],
    "U": [np.array([[1, 1, 1], [1, 0, 1]])],
    "V": [np.array([[1, 1, 1], [1, 0, 0], [1, 0, 0]])],
    "W": [np.array([[1, 0, 0], [1, 1, 0], [0, 1, 1]])],
    "X": [np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])],
    "Y": [np.array([[0, 1, 0, 0], [1, 1, 1, 1]])],
    "Z": [np.array([[1, 1, 0], [0, 1, 0], [0, 1, 1]])],
}

PENTOMINOS = [np.array(shape, dtype=DTYPE) for shape in RAW_SHAPES.values()]


# 0 means the spot is free; 1 means its not in the shape to fill

# rectangles
BOARD_3_20 = np.zeros((3, 20), dtype=DTYPE)
BOARD_4_15 = np.zeros((4, 15), dtype=DTYPE)
BOARD_5_12 = np.zeros((5, 12), dtype=DTYPE)
BOARD_6_10 = np.zeros((6, 10), dtype=DTYPE)

# 8x8 with a 2x2 hole in the middle
BOARD_8_8 = np.zeros((8, 8), dtype=DTYPE)
BOARD_8_8[3:5, 3:5] = 1

# 2 separate 3x10 rectangles
BOARD_2_3_10 = np.zeros((3, 21), dtype=DTYPE)
BOARD_2_3_10[:, 10] = 1

# 2 separate 5x6 rectangles
BOARD_2_5_6 = np.zeros((5, 13), dtype=DTYPE)
BOARD_2_5_6[:, 6] = 1

# 3 separate 4x5 rectangles
BOARD_3_4_5 = np.zeros((3, 23), dtype=DTYPE)
BOARD_3_4_5[:, 5:6] = 1

BOARD_8_9 = np.zeros((8, 9), dtype=DTYPE)
BOARD_8_9[::7, ::8] = 1
BOARD_8_9[1::5, ::8] = 1
BOARD_8_9[::7, 1::6] = 1



# a smaller problem for developping / debugging
# the board is
# +--+--+--+
# |xx|  |xx|
# +--+--+--+
# |  |  |  |
# +--+--+--+
# |xx|  |  |
# +--+--+--+
# and we have 2 identical pieces that look like this
#    +--+
#    |  |
# +--+--+
# |  |  |
# +--+--+

SMALL_BOARD = np.array([[1, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=DTYPE)
SMALL_PIECE = np.array([[0, 1], [1, 1]], dtype=DTYPE)



# def positions(piece):
#     rotat1= np.rot90(RAW_SHAPES[piece][0],k=1)
#     rotat2= np.rot90(RAW_SHAPES[piece][0],k=2)
#     rotat3= np.rot90(RAW_SHAPES[piece][0],k=3)
#     symetr= np.fliplr(RAW_SHAPES[piece][0])
#     s_rotat1= np.rot90(symetr,k=1)
#     s_rotat2= np.rot90(symetr,k=2)
#     s_rotat3= np.rot90(symetr,k=3)
#     seq=[RAW_SHAPES[piece][0],rotat1,rotat2,rotat3,symetr,s_rotat1,s_rotat2,s_rotat3]
#     return
    #vu = {str(seq[0]): True}
    # for element in seq:
    #     if str(element) not in vu:
    #         vu[tuple(element)] = True
    #         RAW_SHAPES[piece].append(element)
    # return 

def positions_2(piece):
    rotat1= np.rot90(RAW_SHAPES[piece][0],k=1)
    rotat2= np.rot90(RAW_SHAPES[piece][0],k=2)
    rotat3= np.rot90(RAW_SHAPES[piece][0],k=3)
    symetr= np.fliplr(RAW_SHAPES[piece][0])
    s_rotat1= np.rot90(symetr,k=1)
    s_rotat2= np.rot90(symetr,k=2)
    s_rotat3= np.rot90(symetr,k=3)
    seq=[RAW_SHAPES[piece][0],rotat1,rotat2,rotat3,symetr,s_rotat1,s_rotat2,s_rotat3]
 

    for k in range(1,len(seq)):
        doublon=False
        a=0
        for i in range(len(RAW_SHAPES[piece])):
            if np.array_equal(seq[k],RAW_SHAPES[piece][i]):
                doublon=True

            
        if doublon ==False:
            RAW_SHAPES[piece].append(seq[k])

    return 



    


for piece in RAW_SHAPES:
    positions_2(piece)


print(RAW_SHAPES)
