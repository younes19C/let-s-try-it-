from numpy import*
''' M=[[1,2,3],[4,5,6],[7,8,9]]
print(M)

M2=[[1]*3 for i in range(3)]
print(M2)
A=[[-1,2,3],[6,8,10],[4,-2,0]]
print(A)
print(len(A))
M3=[[2]*3 for i in range(3)]
print(M2+M3)
print(M2*2)
#Les deux op´erateurs - et / n’existent pas.
#l'utilisation du module numpy 
T=array([[0]*3 for i in range(3)],dtype=type)
M1=array([[2,4,6],[1,3,5],[9,7,5]],dtype=int) ; print(M1)
M4=array([[1,2,3],[6,5,4],[7,8,9]],dtype=int) ; print(M4)
#(+)(*)(/)(-)term par term 
print(M1*2)
print(M1+M4)
print(M1*M4)
print(M1-M4)
## l'acces au element du matrice 
print(M[0][0])
'''


# remplisage d'un matrice
def saisirMat(L,C): 
    M=array([[0]*3 for i in range(3)])
    for i in range(len(M)):
        for j in range(len(M[0])):    
            print(f'entrer M[{i}][{j}]')       
            M[i][j]=int(input())
    return M
# print(saisirMat(3,3))
r=array([[8]*3 for i in range(3)])
r[2][1]=5
def AfficherMat(M) :
  for i in range(len(M)) :
    for j in range(len(M[0])) :
      print('M[',i,'][',j,']=',M[i][j])
p=matrix([[1]*3 for i in range(3)])     
AfficherMat(r)
'''import matplotlib.pyplot as plt

#********************\\ Question1:  Afficher Imgage \\********************
def AfficherImg(img,m=255,n=0):
  plt.axis("off") # Pour desactiver les axes 
  plt.imshow(img, interpolation="nearest")
# on a choisi m,n comme valeur pour l'accer au choix des valeurs vmax 
# pour assurer l'accer au choix vmax et vmin ce qui donne le fait de chaoisir noire ,blanc et RGB
plt.show()

#********************\\ Question2: Ouvrir Image \\************************
def ouvrirImage(chemin):
  img=plt.imread(chemin)
  return img

#********************\\ Question3: Sauvegarder Image \\******************
def saveImage(img):
  plt.imsave("image1.png",img)



'''