# Projet NSI Cosmo - Oscar

Notre projet est un jeu du pendu qui se joue dans le terminal.

## Principe

Le jeu du pendu consiste à choisir un mot et à le faire deviner à son adversaire en un nombre limité de propositions de lettres. Dans le jeu que vous allez programmer, l’ordinateur devra choisir un mot au hasard et demander des lettres à l’utilisateur, en affichant après chaque proposition l’état du pendu et les lettres du mot déjà devinées (en utilisant des tirets pour les lettres inconnues).

## Prérequis

Nous vous recommendons plusieurs choses avant avant de telecharger et lancer votre code:
- Vérifier que votre python supporte la librairie [urllib](https://docs.python.org/3/library/urllib.html) (native sur python > 3.6)
- Si le code bloque sur la biblioteque urllib sur Mac OS, executez le fichier (double click) qui se trouve dans:
```  
Machintosh HD > Applications > Pyhton 3.xx > Install Certificates.command
```   
Ce fichier commande debloque la decouverte ssl non certifié

- Il sera aussi necessaire d'installer la librairie tqdm nécessaire pour la barre de chargement. 

Pour cela, utiliez le package manager [pip](https://pip.pypa.io/en/stable/) pour installer [tqdm](https://pypi.org/project/tqdm/) grâce a votre terminal

```bash
pip install tqdm
```
et vous etes bon !

## Utilisation

Notez qu'actuellement notre code s'execute au mieux sur:
* [Powershell](https://learn.microsoft.com/en-us/powershell/) (pour windows)
* Et [Visual Studio Code](https://code.visualstudio.com/) (pour les autres systemes d'exploitations)

1. Telechargez le fichier suivant https://github.com/Oscar-T24/projet-NSI/tree/main/Main. 
2. Une fois le telechargement du fichier .zip finit, ouvrez le et et vous devriez avoir un fichie nommé "Main".
2.1 Si ce n'est pas le cas, renommez ainsi



ATTENTION : 
- le code ne s'executera pas correctement sur le terminal(Mac OS) et sur la console de IDLE(qui n'affichera pas les codes de sorties ANSII necessaires pour la mise en forme de la sortie)

Notre code principal importe directement le fichier pendu in

## Reference 

Si vous souhaitez obtenir tous les fichiers que nous avons utilisés(à savoir, les tests et documentation) vous pouvez visiter notre page github du projet du pendu à l'addresse suivante : 

https://github.com/Oscar-T24/projet-NSI



