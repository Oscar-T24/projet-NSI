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
print(' '.join(mot_mystere))


def jeu_pendu():
    '''
    lance le jeu du pendu et renvoi 'victoire' ou 'défaite'
    tire au hasard un mots parmis ceux de 'mots.txt' et le stocke dans 'mot_mystere'
    la stocke ensuite dans une liste de caractere 'mot_trouve'
    demande à l'utilisateur une lettre
    '''
    caracteres_essai = ['a'] 
    caracteres_essai.append(entree_utilisateur(input("entrez un caractère"),caracteres_essai))

def entree_utilisateur(entree,essais):
    '''
    actualise la liste des caracteres donnés par l'utilisateur en supprimant les doublons
    renvoi un message d'erreur si l'utilisateur a déja rentré un caractere precedent
    '''
    if entree not in essais:
        return entree
    else:
        print('caractère déja essayé ! veuillez rentrer un autre caractère')

jeu_pendu()