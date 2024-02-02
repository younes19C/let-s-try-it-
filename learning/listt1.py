import copy 

''' def ChekMotPass(Dict,login,passwd):
  # Vérification de la présence de l'identifiant dans le dictionnaire.
  if login not in Dict:
    return False

  # Vérification du mot de passe.
  return Dict[login] == passwd
d={"younes":"chami","aymane":"dalouch"}
print(ChekMotPass(d,"younes","chami"))
import calendar as cl 
year=2023
month=3
x=cl.month(year,month )
print(x)


# les liste 
L1 = [1, 2, [5, 6, 7]]
L2 = L1; print(L1, L2)
L2[2][0] = 10.5
print(L1, L2)
# creation d'une liste sont changer L1 par l'importation du module copy 

L1 = [1, 2, [5, 6, 7]]
L2 = copy.deepcopy(L1)
L2[2][0] = 3.2
print(L1, L2)

# l'utulisation de la fonction range(debut,fin,pas)
L=list(range(10))
print(L)

L3=[i for i in range(1,13,2)]
print(L3)
print(L3[3:6])

L4=[6,2,7,-10,56,13]
print(len(L4))
print(min(L4))
print(max(L4))
print(sum(L4))
del(L4[2])
print(L4)
print(len(L4))
L5=L+L4
print(L5)
#list*i permet de rotourner une liste contient i copie de la list 
L6=L*2
print(L6)
# les fonction pre definit 
# append pour ajouter un element a la fin du list 
L.append(10)
print(L)
#Modifie L en inserant x dans la position de l’indice i
L.insert(0,11)
print(L)
seq=[10,20,30]
L.extend(seq) # None Modifie L en lui ajoutant les ´el´ements de l’it´erable seq.
print(L)
print(L.count(10)) #int retourne le nombre d’occurrences de x dans la liste L

print(L.index(10))#int retourne l’indice du premier ´el´ement de L ´egale `a x(ValueError si x n’existe pas)

print(L.index(10,2)) #int retourne l’indice de la ni`eme occurrence de x dans L
print(L)
print(L.pop()) #item renvoie le dernier ´el´ement et le supprime de la liste

L.remove(0) #None supprime la premi`ere occurrence de x dans L
print(L)
L.reverse() #None Modifie L en renversant l’ordre de ses ´el´ements
print(L)
L.sort()    #  None Modifie L en triant par ordre croissant ses ´el´ements
print(L) 
k=(1,2,3,4,5,6,7,8,9,0,'a','b')
print(type(k))
print(k[0:len(k):1],end=" ") 
'''
from array import *
from numpy import* 
C=['a','b','c']
d=array(C,dtype=str)
print(d,' \n')

l=[0,2,4] 
m=array(l,dtype=int)
n=array([1,3,5],dtype=int)
print(l+n)
e=array('i',range(5))
    






