#code du jeu de pendu
from random import randint

fichier = open("mots.txt",'r')
liste_mots = fichier.readlines()
fichier.close()
mot_mystere = (liste_mots[randint(1,323470)])

mot_trouve = (len(mot_mystere))*["_"]
# rajouter les traits d'unions ...

# print(' '.join(mot_trouve))