from random import randint
from pendu_initial_eleves import dessinPendu

def jeu_pendu():
    
    fichier = open("mots.txt",'r')
    liste_mots = fichier.readlines()
    fichier.close()
    mot_mystere = (liste_mots[randint(1,323470)])
    mot_trouve = (len(mot_mystere)-1)*["_"]
    print(" *----------LE JEU DU PENDU:----------* \n")
    print(' '.join(mot_trouve))
    print(mot_mystere) # option triche
    
    stage = 0
    while stage < 6 and (' '.join(mot_trouve)).rstrip() != (' '.join(mot_mystere).rstrip()):
        l = input("entrez un caractère: ") # À faire: Afficher Erreur si "l" n'est pas une lettre
        miseajour_mot(mot_mystere, mot_trouve, l)
        if miseajour_mot(mot_mystere, mot_trouve, l) == True:
            print(f"La lettre '{l}' est bien dans le mot a deviner.")
            if stage != 0:
                print(dessinPendu(0+stage))   
        else:
            stage += 1
            print(f"La lettre '{l}' n'est pas dans le mot a deviner.")
            print(dessinPendu(0+stage))
        print(' '.join(mot_trouve))
        print("\n *-----------------------------------------------* \n")
    
    if stage < 6:
        print('\n Victoire ! \n')
    else:
        print('Défaite :-( \n')


            
    
        
def miseajour_mot(mot_mystere, mot_trouve, l):
    check = 0
    for i in range(0,len(mot_mystere)):
        if l == mot_mystere[i]: # Changer pour que le programme accept minuscule et majuscule
            mot_trouve[i] = l
            check += 1
    if check > 0:
        return True
    else: 
        return False

        


    


jeu_pendu() 
