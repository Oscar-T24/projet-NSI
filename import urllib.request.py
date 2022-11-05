import urllib.request

if input('oui ou non') == 'a':
    valeur = input('entrer un truc à envoyer')
    with urllib.request.urlopen("https://api.thingspeak.com/update?api_key=EO360EVN7GPAYBBA"+"&field1=%s"%(valeur)) as url:
        s = url.read()
        print('valeur envoyé')
    
