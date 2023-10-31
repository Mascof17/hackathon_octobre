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
board = np.array([
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [1, 0, 1, 0, 0],
    [1, 0, 0, 0, 0]
])

piece = np.array([
    [1, 1],
    [1, 1],
    [1, 0]
])

emplacements_possibles = trouver_emplacements_pentamino(board, piece)
print("Emplacements possibles pour le pentamino :")
print(emplacements_possibles)

#à partir des emplacements possibles j'essaye de faire le tableau :

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
