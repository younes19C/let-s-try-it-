from numpy import *
import array as arr
""" ##T2=array('i',[4,5,8])
my_array = arr.array("i", [1, 2, 3, 4, 5])
## T1=array([-1,2,5],dtype=int)
## print(T1)
my_array[0]=10
##mprint(my_array)
for element in my_array:
    print(element)
T5 = arr.array('f',range(10))
for element in T5:
    print(element)
T = zeros(10, dtype = float)
print(T)
def AfficherMat(M):
    for ligne in M:
        print(ligne)
def SommeElt(M):
    som=0
    for i in range(len(M)):
        for j in range(len(M[0])):
            som+=M[i][j]
    return som 


Mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
AfficherMat(Mat)
print(SommeElt(Mat))"""
def sommeligne(M, numL):
  """
  Calcule la somme des coefficients de la ligne de numéro numL d'une matrice M.

  Args:
    M: La matrice.
    numL: Le numéro de la ligne.

  Returns:
    La somme des coefficients de la ligne de numéro numL.
  """

  

  # Calcul de la somme.
  somme = 0
  for i in range(len(M[numL])):
    somme += M[numL][i]

  return somme


# Exemple d'utilisation.
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
x = sommeligne(M, 2)
print(x)