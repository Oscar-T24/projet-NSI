import urllib.request
import json
import time
from pprint import pprint
import re

while True:
  #TS = urllib.request.urlopen("https://api.thingspeak.com/channels/1922406/feeds.json?results=1")
  TS = urllib.request.urlopen(" https://api.thingspeak.com/channels/1922406/fields/1.json?api_key=XEPU2C2CXF5SWCMM&results=5") #on peux changer le nombre de variables recues avec reulsts
  response = TS.read()
  data=json.loads(response)
  pprint(data) 
  b = data['channel']['field1']
  print('==========================')
  print(b)
  a = data.values()
  print(type(a))
  a = str(a)
  print(type(a))
  print(len(a))
  valeurfinale = []
  for i in range(120,len(a)):
    if a[i] == 'f' and len(a) - i > 10:
        if a[i+10] != ' ':
                #e = a.index('field1')+10
            e = i+10
            indexfinal = e
            while True:
                if a[indexfinal] == "'":
                    break
                indexfinal +=1
        #print('la valeur a index.9=',a[a.rindex('field1')+10:a.rindex('field1')+e])
            print('la valeur a index.9=',a[e:indexfinal])
            valeurfinale.append(a[e:indexfinal])
    
       
    #print('field trouve à l"index', a.index('field1'))
  print(valeurfinale)
  TS.close()
  '''
  valeur = input('entrer un truc à envoyer')
  with urllib.request.urlopen("https://api.thingspeak.com/update?api_key=EO360EVN7GPAYBBA"+"&field1=%s"%(valeur)) as url:
    s = url.read()
    print('valeur envoyé')
'''
 # faire un code ici qui sépare l'utilisateur de son score
  dictionnaire_leadeboard = {}
  for i in range(len(valeurfinale)):
    strlist = ''
    strlist = re.split('(\d+)', valeurfinale[i])
    dictionnaire_leadeboard[strlist[0]] = strlist[1]
  print(dictionnaire_leadeboard)
#fIL FAUT FAIRE UN TRUC QUI CLASSE LE NIVEAU
# PETIT PROBLEME IL S4AGIT D4UN FEED DONC SEULEMENT LES DEUX DERNIERES VALEURS SONT CONSERVEES
# FAIRE UN SCRIPT QUI COMPARE LE SCORE FINAL DE L'UTILISATEUR AVEC CEUX DES DEUX SCORES LES PLUS RECENTS POUR DIRE S'IL A FAIT MIEUX OU MOINS BIEN