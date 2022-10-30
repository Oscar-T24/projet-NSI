from random import randint
from pendu_initial_eleves import dessinPendu
import os
import sys
os.system("")

def jeu_pendu():
    fichier = open("mots.txt",'r')
    liste_mots = fichier.readlines()
    fichier.close()

    mot_mystere = (liste_mots[randint(1,323470)]) # tirer au hasard un mot appelé ensuite mot_mystere dans le fichier mots.txt
    # l’ordinateur devra choisir un mot auhasard
    
    # mot_trouve = (len(mot_mystere)-1)*["_"] NE COMPTE PAS LES TRAITS D'UNIONS
    
    mot_trouve = [] # définir mot_trouve comme une liste de caractères (et non comme une chaîne de caractères) de la longueur du mot à deviner
    for i in mot_mystere[0:-1]: # j'ajoute le -1 pour pas que le nombre d'underscore depasse le nombre de caracteres
        if i == '-':
            mot_trouve.append("-")
        else:
            mot_trouve.append('_')
    # rajouter les traits d'unions s'ils existent(car ce ne sont pas des caracteres)... en utilisant des tirets pour les lettres inconnues
    
    print(" *----------LE JEU DU PENDU:----------* \n")
    print(' '.join(mot_trouve))
    print(mot_mystere) # option triche #
    
    stage = 0
    L = []
    while stage < 6 and (''.join(mot_trouve)).rstrip() != (''.join(mot_mystere).rstrip()): # Tant que le pendu n'est pas finit et que le mot ne sois pas trouvé...
        l = input("entrez un caractère: ") # demander au joueur une lettre
        # demander des lettres à l’utilisateur
        if miseajour_mot(mot_mystere, mot_trouve, l) == True:
            print(f"La lettre '{l}' est bien dans le mot a deviner.")
            if stage != 0:
                print(dessinPendu(stage)) # afficher le pendu si le mot n’a pas été trouvé après le nombre d’essais permis par les dessins
                # l’état du pendu   
        else:
            stage += 1
            print(f"\nLa lettre '{l}' n'est pas dans le mot a deviner.")
            print(dessinPendu(stage)) # afficher le pendu si le mot n’a pas été trouvé après le nombre d’essais permis par les dessins
            # l’état du pendu
        print(' '.join(mot_trouve)) # afficher l’état d’avancement de mot_trouve
        L += l
        print("\nCarctères déja essayés: ",' // '.join(L)) # les lettres du mot déjà devinées
        # affichant après chaque proposition
        print("\n *-----------------------------------------------* \n")
    
    jeu_pendu.var = (''.join(mot_mystere).rstrip())
    
    if stage < 6:
        return 'Victoire'
    else:
        return 'Défaite'
#renvoie le mot ‘victoire’ ou ‘defaite’ selon le résultat.
        
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

def main():
    """
    execute le code principal 
    """
    pourcentage_victoire = 0
    pourcentage_defaite = 0
    effectif_victoire = 0
    effectif_defaite = 0
    total = 0
    re = ''         
    while True:
        if input(f'voulez vous {re}jouer au pendu? [o/n]') == 'o':
            if jeu_pendu() == 'Victoire':
                effectif_victoire += 1
                print(f"Le mot a trouver était bien '{jeu_pendu.var}' \n Victoire ! \n") # terminer le jeu si toutes les lettres du mot ont été trouvées.
            else:
                print(f"Défaite, désole ca sera pour la prochaine fois ;-) \n le mot était \033[1m{jeu_pendu.var}\033[0m")
                effectif_defaite += 1
            total += 1
            pourcentage_victoire = round(effectif_victoire * 100 / total)
            pourcentage_defaite = round(effectif_defaite * 100 / total)
            print(f"Pourcentage de 'Victoire // Défaite': {pourcentage_victoire} % // {pourcentage_defaite} % ")
            if total > 0 : 
                re = 're'
        else:
            print('au revoir !')
            break

main()