from random import randint
from pendu_initial_eleves import dessinPendu
from READ import lecture_serveur_TS
from PARSING import publier_score
import os
import time
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Si le code bloque sur la biblioteque urllib sur Mac OS 
    # ==> Executer le fichier sur Machintosh HD > Applications > Pyhton 3.xx > Install Certificates.comman
    # Ce fichier debloque la decouverte ssl non certifié

# ==========Fonction 'clear'========== #
def cls():
    '''
    Nettoie le 'buffer' de l'ecran pour plus de lisibilité

    None
    '''
    os.system('cls' if os.name=='nt' else 'clear')

# ==========Fonction du jeu du pendu========== #
def jeu_pendu(niveau):
    '''
    permet de jouer au pendu et renvoie le mot
    'victoire' ou 'defaite' selon le résultat.

    int (niv de difficulté) --> string
    '''
    # ==========Choix du niveau========== #
    global niv
    niv = niveau

    # ==========Lecture mot.txt========== #
    fichier = open("Main/mots.txt",'r')
    liste_mots = fichier.readlines()
    mot_mystere = ''
    while len(mot_mystere) > (niveau+4)*(niveau+2) or len(mot_mystere) < (niveau+2)*(niveau+2):
        mot_mystere = (liste_mots[randint(1,323470)])
    fichier.close()

    # ==========Definition de 'mot_trouve'========== #
    mot_trouve = []
    for i in mot_mystere[0:-1]:
        if i == '-':
            mot_trouve.append("-") # Traits d'unions negligés
        else:
            mot_trouve.append('_')

    cls()
    print("\033[1;3m \n ✱----------✱ LE JEU DU PENDU ✱----------✱ \n \033[0m", "❖ Si a tout moment vous souhaitez deviner le mot dans son integralité tapez 'guess' ❖ \n \n",' '.join(mot_trouve))
    # print(mot_mystere) # OPTION TRICHE A RETIRER 

    stage = 0 # Pour les étapes du dessin ascii du pendu
    L = [] # Pour la liste des caractères essayés

    # ==========Boucle du jeu========== #
    while stage < 6 and (''.join(mot_trouve)).rstrip() != (''.join(mot_mystere).rstrip()): # Tant que le pendu n'est pas finit et que le mot ne sois pas trouvé...
        
        # ==========Entrée de l'utilisateur========== #
        l = input(">> Entrez un caractère: ").lower() 
        if len(l) > 1:
            if l == 'guess':
                if input('\n Vous avez entré la commande GUESS. Veuillez entrez votre guess : ').strip() == (''.join(mot_mystere).rstrip()):
                    break # 'guess' pour essayer de deviner le mot complet
                print('Mauvais mot ! Bien essayé quand meme')
            else:
                print("\033[31m {}\033[00m" .format('vous ne pouvez pas entrer plus de 1 carcteres à la fois !'))
            continue 
        
        # ==========Verification de l'entrée========== #
        if l in L:
            print("\033[31m {}\033[00m".format(f"caractère '{l}' déja essayé ! veuillez rentrer un autre caractère"))
            continue
        if l.isalpha() == False:
            print("\033[31m {}\033[00m".format(f"le caractère '{l}' n'est pas dans l'alphabet ! Notez que les mots ne contiennent pas de caracteres spéciaux"))       
            continue
        cls() 
        
        # ==========Affichage du pendu et autre========== #
        print("\033[1;3m \n ✱----------✱ LE JEU DU PENDU ✱----------✱ \n \033[0m")
        if miseajour_mot(mot_mystere, mot_trouve, l) == True:
            print(f"La lettre '{l}' est bien dans le mot a deviner.")
        else:
            stage += 1
            print(f"La lettre '{l}' n'est pas dans le mot a deviner.")
        L += l
        print(dessinPendu(stage),"\033[94m{}\033[00m" .format("\n Tu a le droit à " + str(abs(6-stage)) + " erreur" + ("s" if 6-stage > 1 else "") + " avant d'être pendu!\n"),f"\033[1;3m \n{' '.join(mot_trouve)}\n \033[0m","\n>> Caractères déja essayés: ║",' ║ '.join(L)) 
    
    jeu_pendu.var = (''.join(mot_mystere).rstrip()) # '.var' pour pouvoir utiliser une variable locale dans une autre fonction

    # ==========Retour========== #
    if stage < 6:
        return 'Victoire'
    else:
        return 'Défaite'


def miseajour_mot(mot_mystere, mot_trouve, l):
    '''
    met à jour 'mot_trouve' si la lettre l est contenue dans le mot mystère 
    et qui renvoie un booléen indiquant si la lettre est dans 'mot_mystere'

    string, list, string ==> bool
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

    none ==> string
    """
    global niv
    
    # ==========Variables========== #
    pourcentage_victoire = 0
    effectif_victoire = 0
    total = 0
    re = ''
    difficulté = ['facile','moyen','difficile']
    cls()

    while True:
        if input(f"========================================\n➥ Voulez vous {re}jouer au pendu? [o/n]: ") == "o":
            try:
                
                # ==========Victoire========== #
                if jeu_pendu(difficulté.index(input('➥ Quel niveau de difficulté choisissez vous? [facile, moyen, difficile]: '))) == 'Victoire':
                    effectif_victoire += 1
                    cls()
                    print("\033[1;3m \n ✱----------✱ LE JEU DU PENDU ✱----------✱ \n \033[0m")
                    print(f"Le mot a trouver était bien '{jeu_pendu.var}' \n Victoire ! \n")
                
                # ==========Défaite========== #
                else:
                    cls()
                    print("\033[1;3m \n ✱----------✱ LE JEU DU PENDU ✱----------✱ \n \033[0m")
                    print(f"Défaite, désole ca sera pour la prochaine fois ;-) \n le mot était \033[1m{jeu_pendu.var}\033[0m \n \n")
                
                # ==========Stats de l'utilisateur========== #
                total += 1
                pourcentage_victoire = round(effectif_victoire * 100 / total)
                print(f"⭆\x1B[4m Pourcentage de 'Victoire // Défaite': \x1B[0m \n \n ⮑ [ {pourcentage_victoire} % // {100-pourcentage_victoire} % ]⮐ \n ")
                niv+=2
                score = int(total*niv)
                print(f"⭆\x1B[4m Votre score: \x1B[0m \n \n ⮑ [ {score} ]⮐ \n ")
                état = True
                
                # ==========Affichage leaderboard========== #
                while True:
                    état = publier_score(input("Veuillez entrez votre nom d'utilisateur en minuscule, en caratcres alphabétiques (sera utilisé pour le classement): "),score)
                    match état:
                        case True:
                            break
                lecture_serveur_TS()
                if total > 0 : 
                    re = 're'
            except ValueError:
                print('veuillez entrer un niveau valide')
        else:
            print('Au revoir !')
            break

main()