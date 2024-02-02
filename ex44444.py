### ex1 
#Q1
def initialisermat(L,C):
   M=[[0]*C for i in range(L)]
   return M
print(initialisermat(3,3))
##Q2
def affichermat(M):
   for i in range(len(M)):
      for j in range(len(M[0])):
         print(M[i][j],end=" ")
    
L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
##Q3
def sommeelt(M):
  som=0
  for i in range (len(M)):
      for j in range (len(M[i])):
         som+=M[i][j]
  return som 
#Q4
def produitelt(M):
  prod=0
  for i in range (len(M)):
      for j in range (len(M[i])):
         prod+=M[i][j]
  return prod

print(produitelt(L) )
affichermat(L) 
print(sommeelt(L)) 



def sommeligne(M, numL):
  # Calcul de la somme.
  somme = 0
  for i in range(len(M[numL])):
    somme += M[numL][i]

  return somme
def sommediago2(M):
   somme=0
   for i in range (len(M)-1,-1,-1):
      somme+=M[i][i-1]
   return somme 

# Exemple d'utilisation.
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(sommeligne(M,1))
produitelt(L)
print(sommediago2(L))
                
