import tqm
import urllib.request
from random import randint
def publier_score(utilisateur, score):
    with urllib.request.urlopen("https://api.thingspeak.com/update?api_key=EO360EVN7GPAYBBA"+"&field1=%s"%(utilisateur+str(score))) as url:
        s = url.read()
        print('==> valeur envoyée au serveur API')
        loop = tqdm(total = 100000, position=0, leave=False)
        for k in range(100000):
            loop.set_description("Loading...".format(k))
            loop.update(1)
        loop.close()
        print(loop)
