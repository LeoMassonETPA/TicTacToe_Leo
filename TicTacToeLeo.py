def initialiseGrille(grille[9]):
    compteur = 0
    for compteur in range(0,9):
        grille[compteur] = " "
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
        if(grille[3*i+j] != " ")
            grille[3*i+j] != " " = joueur
            choixIncorrect = False
    return()
    
def testVictoireHorizontale(grille[9]):
    compteur = 0
    while(compteur<3):
        if(grille[compteur] != " " and grille[compteur*3] = grille[compteur*3+1] and grille[compteur*3] = grille[compteur*3+2]):
            return(True)
    return(False)
           
def testVictoireVerticale(grille[9]):
    compteur = 0
    while(compteur<3):
        if(grille[compteur] != " " and grille[compteur] = grille[compteur+3] and grille[compteur] = grille[compteur+6]
            return(True)
    return(False)

def testVictoireDiagonale (grille[9]):
    if(grille[compteur] != " " and grille[4] = grille[0] and grille[4] = grille[8]
        return(True)
    if(grille[compteur] != " " and grille[4] = grille[2] and grille[4] = grille[6]
        return(True)
    return(False)
    
