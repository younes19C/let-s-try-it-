import numpy as np 
l=int(input('entrer la largeur '))
h=int(input('entrer la hauteur '))
M=np.array([[(i + j) % 2 for i in range(l)] for j in range(h)])
# print(M,'\n')

N =np.array([[1 - j for j in i] for i in M ])
print(N)
l=(M.max() + M.min())/2
# print(l)
# Importation de la bibliothèque numpy
# Définition d'une matrice de 8*8
TT= np.array([[1, 2, 3, 4, 5, 6, 7, 8],
                     [9, 10, 11, 12, 13, 14, 15, 16],
                     [17, 18, 19, 20, 21, 22, 23, 24],
                     [25, 26, 27, 28, 29, 30, 31, 32],
                     [33, 34, 35, 36, 37, 38, 39, 40],
                     [41, 42, 43, 44, 45, 46, 47, 48],
                     [49, 50, 51, 52, 53, 54, 55, 56]])
# Affichage de la matrice
print(TT)
t = [TT[i][::-1] for i in range(len(TT))]
print(" le flip horizantale est\n",t)

import numpy as np

# Création des images
img1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
img2 = np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]])

# Superposition des images
img3 = poserV(img1, img2)

# Affichage de la nouvelle image
print(img3)