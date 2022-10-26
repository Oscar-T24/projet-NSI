from random import randint
from pendu_initial_eleves import dessinPendu

def jeu_pendu():
    
    fichier = open("mots.txt",'r')
    liste_mots = fichier.readlines()
    fichier.close()
    mot_mystere = (liste_mots[randint(1,323470)]) # tirer au hasard un mot appelé ensuite mot_mystere dans le fichier mots.txt
    # l’ordinateur devra choisir un mot auhasard
    mot_trouve = (len(mot_mystere)-1)*["_"] # définir mot_trouve comme une liste de caractères (et non comme une chaîne de caractères) de la longueur du mot à deviner
    # en utilisant des tirets pour les lettres inconnues
    print(" *----------LE JEU DU PENDU:----------* \n")
    print(' '.join(mot_trouve))
    print(mot_mystere) # option triche #
    
    stage = 0
    L = []
    while stage < 6 and (' '.join(mot_trouve)).rstrip() != (' '.join(mot_mystere).rstrip()):
        l = input("entrez un caractère: ") # demander au joueur une lettre
        # demander des lettres à l’utilisateur
        miseajour_mot(mot_mystere, mot_trouve, l)
        if miseajour_mot(mot_mystere, mot_trouve, l) == True:
            print(f"La lettre '{l}' est bien dans le mot a deviner.")
            if stage != 0:
                print(dessinPendu(0+stage)) # afficher le pendu si le mot n’a pas été trouvé après le nombre d’essais permis par les dessins
                # l’état du pendu   
        else:
            stage += 1
            print(f"\nLa lettre '{l}' n'est pas dans le mot a deviner.")
            print(dessinPendu(0+stage)) # afficher le pendu si le mot n’a pas été trouvé après le nombre d’essais permis par les dessins
            # l’état du pendu
        print(' '.join(mot_trouve)) # afficher l’état d’avancement de mot_trouve
        # les lettres du mot déjà devinées
        L += l
        print("\nCarctères déja essayés: ",' // '.join(L))
        # affichant après chaque proposition
        print("\n *-----------------------------------------------* \n")
    
    if stage < 6:
        print(f"Le mot a trouver était bien {mot_mystere} \n Victoire ! \n") # terminer le jeu si toutes les lettres du mot ont été trouvées.
    else:
        print(f"Défaite :-( \n Le mot a trouver était {mot_mystere}")
        
def miseajour_mot(mot_mystere, mot_trouve, l):
    '''
    met à jour mot_trouve si la lettre l
    est contenue dans le mot mystère et qui renvoie un booléen indiquant si
    la lettre est dans mot_mystere
    '''
    check = 0
    for i in range(0,len(mot_mystere)):
        if l == mot_mystere[i]:
            mot_trouve[i] = l
            check += 1
    if check > 0:
        return True
    else: 
        return False

jeu_pendu() 
