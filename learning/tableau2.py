#Impl´ementation avec le module array
# le tableau contient des element de meme type
from array import*
''' T=array('i',range(10))
print(T)
print(type(T))
#declaration du tableau par le module numpy : nom-tab=array([intialisateur],dtype=int)
from numpy import*
T1=array(range(6),dtype=int)
T2=array([-1,4,-9,3,5,7],dtype=int)
print(T1)
print(T2)
#initialition des tableau 
T3=zeros(10,dtype=float)
T4=ones(5,dtype=int)
print(T3)
print(T4)
#(+///-)aditioner ou soustracter les element de meme indice dans deux tableau
print(T1+T2)
#(*)(/) multpler des element des tableau des meme indice (T*i)
print(T1*2)
print(T1*T2) '''
'''Les fonctions pr´ed´efinies
Le module numpy int´egre de nombreuses fonctions pr´ed´efinies qui permettent
d’effectuer diff´erentes op´erations :
det : cette fonction permet de calculer le determinant d’une matrice carr´ee
inv : cette fonction permet de calculer l'inverse d'une matrice.
solve : cette fonction permet de r'esoudre une ´equation d’un syst`eme lin´eaire
eig : cette fonction permet de calculer les valeurs et les vecteurs propres d’une
matrice carr´ee.
traspose : cette fonction permet de calculer la transpos´ee d’une matrice carr´ee.
etc.'''
a=(1,2,3,5,6)
print(a[2:3])
