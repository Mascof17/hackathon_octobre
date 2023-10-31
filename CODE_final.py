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

#NOUS GENERONS DESORMAIS TOUTES LES FIGURES CORRESPONDANT A TOUTES LES LETTRES ROTATEES ET REFLECHIES

#gros problème ici que je ne comprends toujours pas donc je tente un autre tri moins propre
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

#la voici cette fonction

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

#ON AJOUTE TOUTES CES FIGURES AU DICTIONNAIRE INTRODUIT PLUS AVANT
for piece in RAW_SHAPES:
    positions_2(piece)




def vérification(board, piece, x, y):
    """
    Renvoie True si la pièce peut être placée, False sinon.
    """
    piece_hauteur, piece_largeur = piece.shape
    board_hauteur, board_largeur = board.shape

    # Vérifie si la pièce peut être placée à la position (x, y)
    if x + piece_hauteur > board_hauteur or y + piece_largeur > board_largeur:
        return False

    for i in range(piece_hauteur) :
        for k in range(piece_largeur) :
            if (piece[i,k] == 1 and board[x+i, y+k] == 1) : return False
    return True





def trouver_emplacements_pentamino(board, piece):
    board_hauteur, board_largeur = board.shape
    piece_hauteur, piece_largeur = piece.shape

    emplacements = []

    for x in range(board_hauteur):
        for y in range(board_largeur):
            if vérification(board, piece, x, y):
                emplacements.append((x, y))

    return emplacements

# Exemple d'utilisation
# board = np.array([
#     [0, 1, 1, 1, 0],
#     [0, 1, 1, 1, 0],
#     [1, 0, 1, 0, 0],
#     [1, 0, 0, 0, 0]
# ])

# piece = np.array([
#     [1, 1],
#     [1, 1],
#     [1, 0]
# ])

# emplacements_possibles = trouver_emplacements_pentamino(board, piece)
# print("Emplacements possibles pour le pentamino :")
# print(emplacements_possibles)

# à partir des emplacements possibles j'essaye de faire le tableau :

#je fais une fonction qui crée le tableau pour une seule pièce

#problème : faire un dictionnaire où on a rajouté les pièces pivotées de max pour qu'elles aient le même nom pour bien remplir la première partie
def piece_unique(piece, board) :
    board_hauteur, board_largeur = board.shape
    emplacements_possibles = trouver_emplacements_pentamino(board, piece)
    #on initialise le tableau nul
    tab = np.zeros((len(emplacements_possibles), 72))
    #on remplit la première partie pour indiquer l'indice de la pièce
    i = RAW_SHAPES.index(piece)
    for liste in tab : tab[liste][i] = 1

    #on remplit le tableau
    for (x,y) in emplacements_possibles :
        for (i,k) in piece :
            tab[(x+i)*board_longueur + (y+k)] = 1
    return tab

#puis j'additionne les tableaux en concaténant par le bas



#ON IMPLEMENTE ENSUITE LA FONCTION EXACT_COVER


# data = np.array([[1, 1,1, 0,0,0],[0,0,0,1,0,1],[0, 0,0, 1,1,1],[0,0,0,0,1,0]], dtype=np.int32)
# expected = np.array([0, 1])
# actual = exact_cover.get_exact_cover(data)






def imprimer(n,L,rep,longueur,hauteur):
    pieces=[]
    tableau=[[0 for k in range (longueur)]for i in range(hauteur) ]
    print(tableau)
    for elem in rep:
        pieces.append(L[elem])
    print(pieces)
    for elem in pieces:
        num=0
        for i in range(n):
            if elem[i]==1:
                num=i+1
        print(num)
        for k in range (n,len(L[0])):
            if elem[k]==1:
                tableau [((k-n)//longueur)][(k-n)%longueur]=num
                print((k-n)//hauteur,(k-n)//hauteur,k)
    return tableau
l=[[1,0,0,1,1,1,0,0,0],[1,0,0,0,0,0,1,1,1],[0,1,0,0,0,0,0,1,0],[0,0,1,0,0,0,1,0,1]]
reptest=[0,2,3]
# print(imprimer(3,l,reptest,2,3))
        


#IL MANQUE ENCORE QUELQUES LIGNES POUR FAIRE LE LIEN ENTRE LES PROGRAMMES ECRITS PAR CHACUN