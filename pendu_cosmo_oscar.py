#code du jeu de pendu
# ATTENTION LA MISE EN FORME DU CODE NE FONCTIONNE QUE SUR LINUX, MAC(quelque soit l'editeur)
# WINDOWS ==> utiliser VScode 
"""
mot_mystere : STRING , mot tiré au hasard

"""
import os
os.system("") # sur windows, pour activer les séquences de sortie ANSI(mise en forme)
from random import randint
from pendu_initial_eleves import dessinPendu #pour suimplifier la lecture, j'importe les pendus
difficulté = ['facile','moyen','difficile']
def jeu_pendu(niveau):
    '''
    lance le jeu du pendu et renvoi 'victoire' ou 'défaite'
    tire au hasard un mots parmis ceux de 'mots.txt' et le stocke dans 'mot_mystere'
    la stocke ensuite dans une liste de caractere 'mot_trouve'
    demande à l'utilisateur une lettre
    None
    '''
    fichier = open("mots.txt",'r')
    
    liste_mots = fichier.readlines()
    fichier.close()
    mot_mystere = (liste_mots[randint(1,323470)])
    while len(mot_mystere) > (niveau+4)*(niveau+2) or len(mot_mystere) < (niveau+2)*(niveau+2):
        mot_mystere = (liste_mots[randint(1,323470)])
    # ====== FAIRE UNE BPUCLE WHILE QUI REGARDE LE NOMBRE DE DISPARITE ENTRE CARACTERES EN FONCTION DE LA DIFFICULT2
    mot_trouve = []

    for i in mot_mystere[0:-1]: # j'ajoute le -1 pour pas que le nombre d'underscore depasse le nombre de caracteres
        if i == '-':
            mot_trouve.append("-")
        else:
            mot_trouve.append('_')
    # rajouter les traits d'unions s'ils existent(car ce ne sont pas des caracteres)...
    print(' '.join(mot_trouve))
    #print(' '.join(mot_mystere))
    caracteres_essai = [] 
    mot_substitue = len(mot_mystere)*['']
    old_mot_subsitue = 0
    stage = 6#+(2-niveau)
    while stage != 0 and (' '.join(mot_substitue)).rstrip() != (' '.join(mot_mystere).rstrip()): # condition de jeu : tant que l'utilisateur n'a pas envcore gangé ou perdu
        n = len(caracteres_essai)
        old_mot_substitue = mot_substitue.count('')
        #print('comptt:',old_mot_substitue)
        # ---------------- ENTREE DES CARACTERES --------------------------
        while True:
            old_mot_substitue = mot_substitue.count('')
            caracteres_essai.extend(list(entree_utilisateur(input("entrez un caractère     "),caracteres_essai)))
            caracteres_essai = [i for i in caracteres_essai if i != '']
            
            print("carctères déja essayés : ",caracteres_essai)
            if len(caracteres_essai) > n:
                break
        # ---------------------------------------------------------------------
        print('', flush=False)
        for i in range(len(mot_mystere)):
            print("_", end = ''),
            for e in caracteres_essai:
                if mot_mystere[i] == e or e == mot_mystere[i]:                   
                    print(mot_mystere[i].upper(), end = ''),
                    mot_substitue[i] = mot_mystere[i] 
        #print('nouveau compte',mot_substitue.count(''))
                
        #si aucun mot n'a été trouvé comme bon entre temps, alors il n'y aura pas moins de ' ' dans mot_susbtitue
        #print(old_mot_substitue, ' VS' , mot_substitue.count(''))
        if old_mot_substitue == mot_substitue.count(''):
            stage -=1
        print('\n','mot substitué : ',' '.join(mot_substitue))
        #print('\n','mot substitué : ',mot_substitue)
        print("\033[94m {}\033[00m" .format(f"il reste {stage} essais"))
        print(dessinPendu(6-stage))
        
   #-------------------------------------------------------------------------
    if (' '.join(mot_substitue)).rstrip() == (' '.join(mot_mystere).rstrip()):
        return 'Victoire'
    return mot_mystere
def entree_utilisateur(entree,essais):
    '''
    actualise la liste des caracteres donnés par l'utilisateur(entree) en supprimant les doublons
    renvoi un message d'erreur si l'utilisateur a déja rentré un caractere precedent(dans les essais)
    '''  
    txt = []
    entree = entree.lower()
    if len(entree) > 1:
        txt = [item.split('-') for item in essais]
        txt = [item for l in entree for item in l]
        if txt not in essais:
            return txt
    if entree not in essais:
        return entree
    print("\033[31m {}\033[00m" .format('caractère déja essayé ! veuillez rentrer un autre caractère',Flush=False))
    return ''
    #-----------------------------------------------------------------

# ======================= code moteur ============================================
def main():
    """
    execute le code principal 
    None
    """
    taux_reussite = 0
    effectif_victoire = 0
    total = 0
    Re = ''
    difficulte = 0             
    while True:
        try:
            if input(f'voulez vous {Re}jouer au pendu? [o/n]') == 'o':
                print('\n bonne chance ! \n\n ==> petite astuce : commencez par les voyelles ! ')
                mot = jeu_pendu(difficulté.index(input('quel niveau de difficulté choisissez vous?[facile, moyen, difficile]'))) 
                if mot == 'Victoire':
                    effectif_victoire += 1
                else:
                    print(f"Défaite, désole ca sera pour la prochaine fois ;) \n le mot était \033[1m{mot}\033[0m")
                total += 1
                taux_reussite = round(effectif_victoire / total * 100)
                print('votre taux de reussite est de : ', taux_reussite, '%')
                if total > 0 : 
                    Re = 'Re'
                else:
                    break
        except OSError: #si la reponse passe pas, on sait jamais ! 
            break

#========================================================================================  
main()
