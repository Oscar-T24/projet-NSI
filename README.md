# Projet NSI Cosmo - Oscar

Notre projet est un jeu du pendu qui se joue dans le terminal.

## Principe

Le jeu du pendu consiste à choisir un mot et à le faire deviner à son adversaire en un nombre limité de propositions de lettres. Dans le jeu que vous allez programmer, l’ordinateur devra choisir un mot au hasard et demander des lettres à l’utilisateur, en affichant après chaque proposition l’état du pendu et les lettres du mot déjà devinées (en utilisant des tirets pour les lettres inconnues).

## Prérequis

Nous vous recommendons plusieurs choses avant avant de telecharger et lancer votre code:
- vérifier que votre python supporte la librairie urllib(native sur python > 3.6) :
# Si le code bloque sur la biblioteque urllib sur Mac OS 
     ==> Executer le fichier sur  
    ```bash
Machintosh HD > Applications > Pyhton 3.xx > Install Certificates.command
    ```
     Ce fichier debloque la decouverte ssl non certifié
# il sera aussi necessaire d'installer la librairie tqdm nécessaire pour la barre de chargement
     pour cela, executez pip/brew(/etc) install tqdm 
    ```bash
pip install tqdm
    ```
     et vous etes bon !

## Utilisation

Notez qu'actuellement notre code s'execute au mieux sur 
* Powershell(pour windows)
* et sur visual Studio dans les autres systemes d'exploitations

ATTENTION : 
- le code ne s'executera pas correctement sur le terminal(Mac OS) et sur la console de IDLE(qui n'affichera pas les codes de sorties ANSII necessaires pour la mise en forme de la sortie)

Notre code principal importe directement le fichier pendu in

## Reference 

Si vous souhaitez obtenir tous les fichiers que nous avons utilisés(à savoir, les tests et documentation) vous pouvez visiter notre page github du projet du pendu à l'addresse suivante : 




