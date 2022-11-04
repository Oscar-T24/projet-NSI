#code du jeu de pendu , fait par Oscar et Cosmo

# WINDOWS : NE FONCTIONNE PAS SUR IDLE : UTILISER POWERSHELL(car l'invite de commande ne fonctionne pas)
"""
mot_mystere : STRING , mot tiré au hasard
mot_trouve : LIST , caracteres décomposés de mot_mystere
caracteres_essais : LIST , caracteres DEJA essayés par l'utilisateur
mot_substitue + old_mot_substitue : STRING , deux chaines de caracteres permettant de connaitre l'écolution de l'utilisateur
stage : INTEGER , donne l'avancement de l'utilisateur
entree : STRING , caractere entré par l'utilisateur


"""
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    #print ("\n" * 100)
# du code pour vider l'écran : WINDOWS utilise cls tandis que MAC et LINUX utilisent clear : cette commande est cross-plateforme!

import sys # si l'utilisateur est sur windows, il faudra utiliser cette librairie pour le formatage de sortie
os.system("") # sur windows, pour activer les séquences de sortie ANSI(mise en forme)
from random import randint
from pendu_initial_eleves import dessinPendu #pour suimplifier la lecture, j'importe les pendus
difficulté = ['facile','moyen','difficile']
def jeu_pendu(niveau):
    '''
    lance le jeu du pendu et renvoi 'victoire' ou 'défaite'
    tire au hasard un mots parmis ceux de 'mots.txt' et le stocke dans 'mot_mystere'
    la stocke ensuite dans une liste de caractere 'mot_trouve'
    demande à l'utilisateur une lettre
    None
    '''
    fichier = open("mots.txt",'r')
    
    liste_mots = fichier.readlines()
    fichier.close()
    global mot_mystere
    mot_mystere = (liste_mots[randint(1,323470)])
    while len(mot_mystere) > (niveau+4)*(niveau+2) or len(mot_mystere) < (niveau+2)*(niveau+2):
        mot_mystere = (liste_mots[randint(1,323470)])
    # ====== FAIRE UNE BPUCLE WHILE QUI REGARDE LE NOMBRE DE DISPARITE ENTRE CARACTERES EN FONCTION DE LA DIFFICULT2
    global mot_trouve
    mot_trouve = []

    for i in mot_mystere[0:-1]: # j'ajoute le -1 pour pas que le nombre d'underscore depasse le nombre de caracteres
        if i == '-':
            mot_trouve.append("-")
        else:
            mot_trouve.append('_')
    # rajouter les traits d'unions s'ils existent(car ce ne sont pas des caracteres)...
    print(' '.join(mot_trouve))
    mot_trouve = []
    #print(' '.join(mot_mystere)) #juste pour le test 
    global mot_trouve 
    '''
    ... , line 54
    global mot_trouve
    ^^^^^^^^^^^^^^^^^
    SyntaxError: name 'mot_trouve' is used prior to global declaration'''
    mot_trouve = []
    global mot_substitue #global permet d'utiliser une variable dans n'importe quelle fonction du code
    mot_substitue = len(mot_mystere)*['']
    old_mot_subsitue = 0
    stage = 6#+(2-niveau)
    while stage != 0 and (' '.join(mot_substitue)).rstrip() != (' '.join(mot_mystere).rstrip()): # condition de jeu : tant que l'utilisateur n'a pas envcore gangé ou perdu
        n = len(mot_trouve)
        old_mot_substitue = mot_substitue.count('')
        #print('comptt:',old_mot_substitue)
        # ---------------- ENTREE DES CARACTERES ----------------------
        while True:
            old_mot_substitue = mot_substitue.count('')
            mot_trouve.extend(list(entree_utilisateur(input("entrez un caractère     "),mot_trouve)))
            mot_trouve = [i for i in mot_trouve if i != '']
            #mot_trouve = [mot_trouve.remove(e) for e in mot_trouve if mot_trouve.count(e) > 1]
            for e in mot_trouve:
                if mot_trouve.count(e) > 1:
                    mot_trouve.remove(e)
            print("carctères déja essayés : ",mot_trouve)
            if len(mot_trouve) > n:
                break
        # ---------------------------------------------------------------------
        cls()
        
        for i in range(len(mot_mystere)): # ok jusqu'ici
            if actualisation(i) == True:
                print(' '+mot_mystere[i], end = ' '),
            else:
                print(" _", end = ' '), 
            #print("_", end = '')
        #print('nouveau compte',mot_substitue.count(''))
                
        #si aucun mot n'a été trouvé comme bon entre temps, alors il n'y aura pas moins de ' ' dans mot_susbtitue
        #print(old_mot_substitue, ' VS' , mot_substitue.count(''))
        if old_mot_substitue == mot_substitue.count(''):
            stage -=1
        # <===== pour le test uniquement ====> print('\n','mot substitué : ',' '.join(mot_substitue))
        print("\033[94m {}\033[00m" .format(f"il reste {stage} essais"))
        #sys.stdout.write(f"il reste {stage} essais")
        print(dessinPendu(6-stage))
        
   #-------------------------------------------------------------------------
    if (' '.join(mot_substitue)).rstrip() == (' '.join(mot_mystere).rstrip()):
        return 'Victoire'
    return mot_mystere
def entree_utilisateur(entree,essais): #def miseajour_mot(mot_mystere,mot_trouve,l)
    '''
    actualise la liste des caracteres donnés par l'utilisateur(entree) en supprimant les doublons
    renvoi un message d'erreur si l'utilisateur a déja rentré un caractere precedent(dans les essais)
    '''  
    if entree.isalpha() == False:
        print("\033[31m {}\033[00m" .format(f'veuillez entrer un caractere alphabétique valide \n( à noter que les mots ne contiennent pas d"accent)'))       
        return ''
    if 'guess' in entree:
        return guess()
    entree = entree.lower()
    if len(entree) > 1 : 
        #txt = [item.split('-') for item in essais]
        #txt = [item for l in entree for item in l]
        #txt =[txt.remove(item) for item in txt if item in entree] 
        print("\033[31m {}\033[00m" .format('vous ne pouvez pas entrer plus de 1 carcteres à la fois !'))
        return ''
        # =======================================!!!!!!!!
        '''
        for e in txt:
            essais.extend(list(entree_utilisateur(e,essais))) 
            essais = [essais.remove(e) for e in essais if essais.count(e) > 1]
        '''
        #========================================!!!!!!!!
    if entree not in essais:
        return entree
    print("\033[31m {}\033[00m" .format(f'caractère {entree} déja essayé ! veuillez rentrer un autre caractère'))
    # OU sys.stderr.write('caractère déja essayé ! veuillez rentrer un autre caractère')
    return ''
    #-----------------------------------------------------------------

# ======================= code moteur ============================================
def main():
    """
    execute le code principal 
    None
    """
    taux_reussite = 0
    effectif_victoire = 0
    total = 0
    Re = ''
    difficulte = 0             
    while True:
        try:
            if input(f'voulez vous {Re}jouer au pendu? [o/n]') == 'o':
                print('\n bonne chance ! \n\n ==> petite astuce : commencez par les voyelles ! \n à tout moment,si vous souhaiter tenter de deviner le mot dans son integralité, tapez "guess" pour accéder à la commande dediée \n \n')
                try : 
                    mot = jeu_pendu(difficulté.index(input('quel niveau de difficulté choisissez vous?[facile, moyen, difficile]'))) 
                    cls()
                except ValueError:
                    print('veuillez rentrer un niveau valide')
                    continue
                if mot == 'Victoire':
                    effectif_victoire += 1
                    print(' \n Victoire ! Bien joué ;)')
                else:
                    print(f"Défaite, désole ca sera pour la prochaine fois ;) \n le mot était \033[1m{mot}\033[0m")
                total += 1
                taux_reussite = round(effectif_victoire / total * 100)
                print('votre taux de reussite est de : ', taux_reussite, '%')
                if total > 0 : 
                    Re = 'Re'
            else:
                print('au revoir !')
                break
        except OSError: #si la reponse passe pas, on sait jamais ! 
            print('probleme d"entrée')
            break

#========================================================================================  
def guess():
    '''
    commande utile qui permet de rentrer un mot deviné
    --> Str
    '''
    guess = input('\n vous avez entré la commande GUESS : veuillez entrez votre guess').strip()
    if mot_mystere == (guess+'\n'):
        return list(mot_mystere)
    else:
        print(' \n mauvais mot!\n')
    return ''

def actualisation(i):
    '''
    actualise le mot trouvé par l'utilisateur en prennant le caractere i de 
    la liste mot_mystere en comparaison du caractere fourni par l'utilisateur 
    pour l'afficher, ou le cas contraire mettre un underscore
    --> bool
    '''
    for e in mot_trouve:
                if mot_mystere[i] == e or e == mot_mystere[i]:
                    mot_substitue[i] = mot_mystere[i] 
                    return True
main()
