#code du jeu de pendu
from random import randint
from pendu_initial_eleves import dessinPendu #pour suimplifier la lecture, j'importe les pendus

fichier = open("mots.txt",'r')
liste_mots = fichier.readlines()
fichier.close()
mot_mystere = (liste_mots[randint(1,323470)])
mot_trouve = []

for i in mot_mystere[0:-1]: # j'ajoute le -1 pour pas que le nombre d'underscore depasse le nombre de caracteres
    if i == '-':
        mot_trouve.append("-")
    else:
        mot_trouve.append('_')
# rajouter les traits d'unions s'ils existent(car ce ne sont pas des caracteres)...
print(' '.join(mot_trouve))


def jeu_pendu():
    '''
    lance le jeu du pendu et renvoi 'victoire' ou 'défaite'
    tire au hasard un mots parmis ceux de 'mots.txt' et le stocke dans 'mot_mystere'
    la stocke ensuite dans une liste de caractere 'mot_trouve'
    demande à l'utilisateur une lettre
    '''
    caracteres_essai = [] 
    mot_substitue = []
    stage = 7
    while stage != 0: # condition de jeu : tant que l'utilisateur n'a pas envcore gangé ou perdu
        n = len(caracteres_essai)
        # ---------------- ENTREE DES CARCATERES --------------------------
        while True:
            caracteres_essai.append(entree_utilisateur(input("entrez un caractère     "),caracteres_essai))
            caracteres_essai = [i for i in caracteres_essai if i != None and i != '']
            print("carctères déja essayés",caracteres_essai)
            if len(caracteres_essai) > n:
                break
        # ---------------------------------------------------------------------
            print('', flush=True)
        for i in range(len(mot_mystere)):
            print("_", end = ''),
            for e in caracteres_essai:
                if mot_mystere[i] == e or e == mot_mystere[i]:
                    mot_substitue.insert(i,mot_mystere[i])
                    print(mot_mystere[i].upper(), end = ''),
        print('\n','mot substitué : ',' '.join(mot_substitue))
        print("\033[94m {}\033[00m" .format(f"il reste {stage} essais"))
        print(dessinPendu(7-stage))
        stage -= 1
   #---------------------------------------a---------------------------------
    # A FAIRE  : CONDITION QUI VERIFIE SI L'UTILISATEUR A GAGNE OU PAS
def entree_utilisateur(entree,essais):
    '''
    actualise la liste des caracteres donnés par l'utilisateur en supprimant les doublons
    renvoi un message d'erreur si l'utilisateur a déja rentré un caractere precedent
    '''
    if entree.lower() not in essais:
        return entree.lower()
    else:
        print("\033[31m {}\033[00m" .format('caractère déja essayé ! veuillez rentrer un autre caractère'))
        return None
    #------------b----------------------------------------------------
jeu_pendu()