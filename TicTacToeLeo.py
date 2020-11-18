def initialiseGrille(grille[9]):
    compteur = 0
    for compteur in range(0,9):
        grille[compteur] = "_"
    return()

def afficheGrille(grille[9]):
    i = 0
    for i in range(0,3):
        print(grille[3*i], grille[3*i+1], grille[3*i+2], "\n")
    return()
    
def ajouteSymbole(grille[9], joueur):
    i = 0
    j = 0
    choixIncorrect = True
    while (choixIncorrect = True):
        i = int(input("Sur quelle ligne voulez vous jouer ?"))
        j = int(input("Sur quelle colonne voulez vous jouer ?"))
        if(grille[3*i+j]!="_")
            grille[3*i+j]!="_" = joueur
            choixIncorrect = False
    return()