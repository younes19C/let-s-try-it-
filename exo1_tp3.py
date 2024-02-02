L1=[1,2,3]
print(L1[0]) # Cette ligne affichera "1"
print(L1[-1]) # Cette ligne affichera "3"
print(L1) # Cette ligne affiche la liste entière "[1, 2, 3]"
L2=["Ali",20, "casa", 'A']
L2[2] # Cette ligne n'affichera rien car il n'y a pas d'instruction print
L3=L1+L2 # Cette ligne concatene les listes L1 et L2
print(L3) # Cette ligne affiche la nouvelle liste "[1, 2, 3, 'Ali', 20, 'casa', 'A']"
L4=L1*4 # Cette ligne répète la liste L1 quatre fois
L4 # Cette ligne n'affichera rien car il n'y a pas d'instruction print
L5=L1
L5-L1 # Cette ligne généra une erreur, car l'opération de soustraction ne peut pas être utilisée entre des listes
L5*L1 # Cette ligne génère une autre erreur, car l'opération de multiplication ne peut pas être utilisée entre deux listes
L1.append(10) # Cette ligne ajoute 10 à la fin de la liste L1. Maintenant, L1 est "[1, 2, 3, 10]"
L=[]
L=L+[2]
print(L) # Cette ligne affiche la nouvelle liste "[2]"
