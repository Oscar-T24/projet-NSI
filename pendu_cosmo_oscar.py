#code du jeu de pendu
from random import randint
from pendu_initial_eleves import dessinPendu #pour suimplifier la lecture, j'importe les pendus

def jeu_pendu():
    '''
    lance le jeu du pendu et renvoi 'victoire' ou 'défaite'
    tire au hasard un mots parmis ceux de 'mots.txt' et le stocke dans 'mot_mystere'
    la stocke ensuite dans une liste de caractere 'mot_trouve'
    demande à l'utilisateur une lettre
    '''
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
    caracteres_essai = [] 
    mot_substitue = len(mot_mystere)*['']
    old_mot_subsitue = 0
    stage = 6
    while stage != 0 and (' '.join(mot_substitue)).rstrip() != (' '.join(mot_mystere).rstrip()): # condition de jeu : tant que l'utilisateur n'a pas envcore gangé ou perdu
        n = len(caracteres_essai)
        old_mot_substitue = mot_substitue.count('')
        #print('comptt:',old_mot_substitue)
        # ---------------- ENTREE DES CARCATERES --------------------------
        while True:
            old_mot_substitue = mot_substitue.count('')
            caracteres_essai.append(entree_utilisateur(input("entrez un caractère     "),caracteres_essai))
            caracteres_essai = [i for i in caracteres_essai if i != None and i != '']
            print("carctères déja essayés",caracteres_essai)
            if len(caracteres_essai) > n:
                break
        # ---------------------------------------------------------------------
        print('', flush=True)
        for i in range(len(mot_mystere)):
            print("_", end = ''),
            for e in caracteres_essai:
                if mot_mystere[i] == e or e == mot_mystere[i]:                   
                    print(mot_mystere[i].upper(), end = ''),
                    mot_substitue[i] = mot_mystere[i] # cette partie pose probleme
        #print('nouveau compte',mot_substitue.count(''))
                
        #si aucun mot n'a été trouvé comme bon entre temps, alors il n'y aura pas moins de ' ' dans mot_susbtitue
        #print(old_mot_substitue, ' VS' , mot_substitue.count(''))
        if old_mot_substitue == mot_substitue.count(''):
            stage -=1
        print('\n','mot substitué : ',' '.join(mot_substitue))
        #print('\n','mot substitué : ',mot_substitue)
        print("\033[94m {}\033[00m" .format(f"il reste {stage} essais"))
        print(dessinPendu(6-stage))
        
   #---------------------------------------a---------------------------------
    if (' '.join(mot_substitue)).rstrip() == (' '.join(mot_mystere).rstrip()):
        return 'Victoire ! Whooo'
    return f"Défaite, désole ca sera pour la prochaine fois ;) '\n' le mot était \033[1m{mot_mystere}\033[0m"
def entree_utilisateur(entree,essais):
    '''
    actualise la liste des caracteres donnés par l'utilisateur en supprimant les doublons
    renvoi un message d'erreur si l'utilisateur a déja rentré un caractere precedent
    '''
    if entree.lower() not in essais:
        return entree.lower()
    else:
        print("\033[31m {}\033[00m" .format('caractère déja essayé ! veuillez rentrer un autre caractère'))
        return None
    #------------b----------------------------------------------------

def main():
    while True:
        try:
            if input('voulez vous jouer au pendu? [o/n]') == 'o':
                print(jeu_pendu(), flush = True)
            else:
                break
        except OSError: #si la reponse passe pas, on sait jamais ! 
                break
    
main()