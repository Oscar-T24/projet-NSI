import urllib.request
from random import randint
utilisateur = input('entrez votre nom d"utilisateur')
score = randint(0,200)
with urllib.request.urlopen("https://api.thingspeak.com/update?api_key=EO360EVN7GPAYBBA"+"&field1=%s"%(utilisateur+str(score))) as url:
    s = url.read()
    print('valeur envoyée au servceur API')
    
