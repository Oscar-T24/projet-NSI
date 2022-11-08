from unicodedata import name
import urllib.request
import json
import time
from pprint import pprint
import re
from PARSING import publier_score
from random import randint

from PARSING import publier_score
def lecture_serveur_TS():
  #TS = urllib.request.urlopen("https://api.thingspeak.com/channels/1922406/feeds.json?results=1")
  TS = urllib.request.urlopen(" https://api.thingspeak.com/channels/1922406/fields/1.json?api_key=XEPU2C2CXF5SWCMM&results=10") #on peux changer le nombre de variables recues avec reulsts
  response = TS.read()
  data=json.loads(response)
  #pprint(data) 
  b = data['channel']['field1']
  #print('==========================')
  #print(b)
  a = data.values()
  #print(type(a))
  a = str(a)
  #print(type(a))
  #print(len(a))
  valeurfinale = []
  for i in range(120,len(a)-5):
    if a[i:i+6] == 'field1' and len(a) - i > 10:     
        if a[i+10] != ' ':
                #e = a.index('field1')+10
            e = i+10
            indexfinal = e
            while True:
                if a[indexfinal] == "'":
                    break
                indexfinal +=1
        #print('la valeur a index.9=',a[a.rindex('field1')+10:a.rindex('field1')+e])
            #print('la valeur a index.9=',a[e:indexfinal])
            valeurfinale.append(a[e:indexfinal])
    
       
    #print('field trouve à l"index', a.index('field1'))
  #print(valeurfinale)
  TS.close()
  '''
  valeur = input('entrer un truc à envoyer')
  with urllib.request.urlopen("https://api.thingspeak.com/update?api_key=EO360EVN7GPAYBBA"+"&field1=%s"%(valeur)) as url:
    s = url.read()
    print('valeur envoyé')
'''
 # faire un code ici qui sépare l'utilisateur de son score
  dictionnaire_leadeboard2 = {}
  nometscore = []
  for i in range(len(valeurfinale)):
    strlist = ''
    strlist = re.split('(\d+)', valeurfinale[i]) # PROBLEME ICI
    strlist.pop(2)
    print(strlist)
    nometscore.append(strlist)
    #ajouter un script qui supprime les doublons
    #dictionnaire_leadeboard[strlist[0]] = strlist[1] #JUSTE POUR LE MOMEBT

  doublon = [] # liste avec les noms qui sont presents plus d'une fois

  for i in range(len(nometscore)): # parcourir la liste entiere
    occurence = 0 # reinitialiser le nb d'occurence à chaque changement
    for e in range(len(nometscore)):
      if nometscore[e][0] == nometscore[i][0]:
        occurence += 1
    if occurence > 1 and nometscore[i][0] not in doublon:
      print('doublon trouve : user = ',nometscore[i][0], 'de score ', nometscore[i][1])
      doublon.append(nometscore[i][0])
  print(doublon) # AFFICHER LES INDICES DES DOUBLONS

  # =================ALGORITHME DE TRI : LISTE DES NOMS DOUBLONS========================
  maximum = 0 
  maximum_conflit = []
  maximum_conflit = [doublon[:]]
  for i in range(len(doublon)):
    for e in range(len(nometscore)):
      if nometscore[e][0] == doublon[i]:
        if int(nometscore[e][1]) > maximum:
          maximum = int(nometscore[e][1])
          maximum_conflit[i].append(int(maximum))
          maximum_conflit[i][1] = maximum_conflit[i][-1]
  print('elements conflictuels avec meir maximum',maximum_conflit)
  #==========format de maximum_conflit : [[utilisateur, score max]]
  #================================================================

  '''
  doublon = list(set(doublon))
  liste_sans_doublon = []

  for i in range(len(nometscore)):
    if i not in doublon:
      liste_sans_doublon.append(nometscore[i])
  '''
  #print(liste_sans_doublon)
  '''
  while len(doublon) > 2:
    print(doublon)
    doublon.pop(0)
    nometscore.pop(doublon[0])
    doublon.pop(0)
  '''
  
  #print('noms utilisateurs suivis de leur score = ',dictionnaire_leadeboard)
  '''
  for key, value in dictionnaire_leadeboard.items():
    print(valeurfinale.count(key))# ne marche pas car il faudrait trouver une fonction qui regarde si le mot est contenu dans le codage userscore
  '''
  liste_finale = []
  for i in range(len(nometscore)):
    for e in range(len(maximum_conflit)):
      if maximum_conflit[e][0] == nometscore[i][0]:
        liste_finale.append(maximum_conflit[e])
      else:
        liste_finale.append(nometscore[i])

  for i in range(len(liste_finale)):
    dictionnaire_leadeboard2[liste_finale[i][0]] = liste_finale[i][1]
  #dictionnaire_leadeboard = dict(sorted(dictionnaire_leadeboard2.items(), key=lambda item: item[1], reverse= True))
  #print(dictionnaire_leadeboard2)
  
  print('\n<=============Classement des scores récents classés par nombre de point========================>')
  for key, value in dictionnaire_leadeboard2.items():
    if int(value) > 0:
      print(key, ':', value)
  return 
# IL FAUT FAIRE UN TRUC QUI CLASSE LE NIVEAU
# PETIT, PROBLEME IL S'AGIT D'UN FEED DONC SEULEMENT LES DEUX DERNIERES VALEURS SONT CONSERVEES
# FAIRE UN SCRIPT QUI COMPARE LE SCORE FINAL DE L'UTILISATEUR AVEC CEUX DES DEUX SCORES LES PLUS RECENTS POUR DIRE S'IL A FAIT MIEUX OU MOINS BIEN
if __name__ == '__main__': # si le code est executé à part(= environnement de test) ou importé(= jeu)
  while True : 
    publier_score('onathan',randint(2,98))
    lecture_serveur_TS()
