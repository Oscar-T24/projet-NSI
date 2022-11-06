from random import randint
from pendu_initial_eleves import dessinPendu
from READ import lecture_serveur_TS
from PARSING import publier_score
import os
import time

def cls():
    '''
    nettoie le 'buffer' de l'ecran pour plus de lisibilité
    None
    '''
    os.system('cls' if os.name=='nt' else 'clear')
    #print ("\n" * 100)
def jeu_pendu(niveau):
    global niv 
    niv = niveau
    fichier = open("mots.txt",'r')
    liste_mots = fichier.readlines()
    mot_mystere = ''
    while len(mot_mystere) > (niveau+4)*(niveau+2) or len(mot_mystere) < (niveau+2)*(niveau+2):
        mot_mystere = (liste_mots[randint(1,323470)])
    
    fichier.close()
    # l’ordinateur devra choisir un mot auhasard
    
    # mot_trouve = (len(mot_mystere)-1)*["_"] NE COMPTE PAS LES TRAITS D'UNIONS
    
    mot_trouve = [] # définir mot_trouve comme une liste de caractères (et non comme une chaîne de caractères) de la longueur du mot à deviner
    for i in mot_mystere[0:-1]: # j'ajoute le -1 pour pas que le nombre d'underscore depasse le nombre de caracteres
        if i == '-':
            mot_trouve.append("-")
        else:
            mot_trouve.append('_')
    # rajouter les traits d'unions s'ils existent(car ce ne sont pas des caracteres)... en utilisant des tirets pour les lettres inconnues
    
    print(" *----------LE JEU DU PENDU:----------* \n Si a tout moment vous souhaitez deviner le mot dans son integralité \n tapez 'guess' ")
    print(' '.join(mot_trouve))
    print(mot_mystere) # OPTION TRICHE A RETIRER 
    
    stage = 0
    L = []

    while stage < 6 and (''.join(mot_trouve)).rstrip() != (''.join(mot_mystere).rstrip()): # Tant que le pendu n'est pas finit et que le mot ne sois pas trouvé...

        l = input("entrez un caractère: ").lower() # demander au joueur une lettre
        if len(l) > 1:
            if l == 'guess':
                if input('\n vous avez entré la commande GUESS. Veuillez entrez votre guess : ').strip() == (''.join(mot_mystere).rstrip()):
                    break # attention 
                print('mauvais mot ! Bien essayé quand meme')
            else:
                print("\033[31m {}\033[00m" .format('vous ne pouvez pas entrer plus de 1 carcteres à la fois !'))
            continue
        if l in L:
            print("\033[31m {}\033[00m".format(f"caractère '{l}' déja essayé ! veuillez rentrer un autre caractère"))
            continue
        if l.isalpha() == False:
            print("\033[31m {}\033[00m".format(f"le caractère '{l}' n'est pas dans l'alphabet ! Notez que les mots ne contiennent pas de caracteres spéciaux"))       
            continue
        

        
        # verifications du caractere entré, auquel cas ou il y aurait un probleme passer la boucle active
        cls()
        if miseajour_mot(mot_mystere, mot_trouve, l) == True:
            print(f"La lettre '{l}' est bien dans le mot a deviner.")
            #if stage != 0:
                # l’état du pendu   
        else:
            stage += 1
            print(f"\nLa lettre '{l}' n'est pas dans le mot a deviner.")
            #print(dessinPendu(stage)) # afficher le pendu si le mot n’a pas été trouvé après le nombre d’essais permis par les dessins
            # l’état du pendu
        print(dessinPendu(stage),"\033[94m {}\033[00m" .format(f" \n il reste {7-stage} essais")) # afficher le pendu si le mot n’a pas été trouvé après le nombre d’essais permis par les dessins
        print(' '.join(mot_trouve)) # afficher l’état d’avancement de mot_trouve
        L += l
        print("\nCarctères déja essayés: ",' // '.join(L)) # les lettres du mot déjà devinées
        # affichant après chaque proposition
        #print("\n *-----------------------------------------------* \n")  
        
        
    jeu_pendu.var = (''.join(mot_mystere).rstrip()) # Pour pouvoir utiliser une variable locale dans une autre fonction
    
    if stage < 6:
        return 'Victoire'
    else:
        return 'Défaite'
#renvoie le mot ‘victoire’ ou ‘defaite’ selon le résultat.
        
def miseajour_mot(mot_mystere, mot_trouve, l):
    '''
    met à jour mot_trouve si la lettre l est contenue dans le mot mystère et qui renvoie un booléen indiquant si la lettre est dans mot_mystere
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
    global niv
    """
    execute le code principal 
    """
    pourcentage_victoire = 0
    effectif_victoire = 0
    total = 0
    re = ''     
    difficulté = ['facile','moyen','difficile']  
    while True:
        if input(f"voulez vous {re}jouer au pendu? [o/n]: ") == "o":
            try:                
                if jeu_pendu(difficulté.index(input('quel niveau de difficulté choisissez vous?[facile, moyen, difficile]'))) == 'Victoire':
                    effectif_victoire += 1
                    cls()
                    print(f"Le mot a trouver était bien '{jeu_pendu.var}' \n Victoire ! \n") # terminer le jeu si toutes les lettres du mot ont été trouvées.
                else:
                    cls()
                    print(f"Défaite, désole ca sera pour la prochaine fois ;-) \n le mot était \033[1m{jeu_pendu.var}\033[0m \n \n")
                total += 1
                pourcentage_victoire = round(effectif_victoire * 100 / total)
                print(f"Pourcentage de 'Victoire // Défaite': {pourcentage_victoire} % // {100-pourcentage_victoire} % ")
                niv+=2
                score = int(total*niv)
                print('votre score  :', score)
                publier_score(input("veuillez entrez votre nom d'utilisateur en minuscule, en caratcres alphabétiques(sera utilisé pour le classement)"),score)
                lecture_serveur_TS()
                if total > 0 : 
                    re = 're'
            except ValueError:
                print('veuillez entrer un niveau valide')
        else:
            print('au revoir !')
            break

main()