def dessinPendu(index):
        """ renvoie le dessin du pendu d'indice donné """
        tab = ['''

       +---+
       |   |
           |
           |
           |
           |
     =========''', '''
 
       +---+
       |   |
       O   |
           |
           |
           |
    =========''', '''
 
       +---+
       |   |
       O   |
       |   |
           |
           |
     =========''', '''
    
       +---+
       |   |
       O   |
      /|   |
           |
           |
     =========''', '''
  
       +---+
       |   |
       O   |
      /|\  |
           |
           |
     =========''', '''
  
       +---+
       |   |
       O   |
      /|\  |
      /    |
           |
     =========''', '''
 
       +---+
       O   |
      /|\  |
      / \  |
           |
     =========''']

        return tab[index]
        


# Ouverture du fichier, liste_mots contient la liste des mots du fichier
# Attention, les mots sont suivis du caractère retour à la ligne
'''
fichier = open("mots.txt",'r')
liste_mots = fichier.readlines()
fichier.close()
'''
