def initialiseGrille(grille[9]):
    compteur = 0
    for compteur in range(0,8):
        grille[compteur] = "_"
    return()

def afficheGrille(grille[9]):
    i = 0
    for i in range(0,2):
        print(grille[3*i], grille[3*i+1], grille[3*i+2], "\n")
    return()
    
