import urllib.request
from random import randint
def publier_score(utilisateur, score):
    with urllib.request.urlopen("https://api.thingspeak.com/update?api_key=EO360EVN7GPAYBBA"+"&field1=%s"%(utilisateur+str(score))) as url:
        s = url.read()
        print('==> valeur envoyée au serveur API')
        
