#1 q1
from numpy import *
def initialertab(n):
    T=[]
    for i in range(n):
        T=T+[0]
    return T
from random import randint
def initialertableau(n):
    T=[]
    for i in range (n):
        T=T+[randint(0,100)]
    return T
print(initialertab(9))   
def ajoutedebut(L,x):
    L=[x]+L
    return L
L=[1,2,3,4,5,6,7,8]
print(ajoutedebut(L,4))
def ajoutfin(L,x):
    L=L+[x]
    return L
print(ajoutfin(L,10))
def ajoutmilieu(L,x,p):
    L[p:p]=[x]
    return L
print(ajoutmilieu(L,12,5))
print(L[5:5])
def makelist(n,x):
    L=[]
    for i in range(n+1):
        L=n*[x]
    return L
print(makelist(9,2))
def listpuis2(n):
    L=[]
    for i in range (n):
        L=L+[2**i]
    return L

print(listpuis2(4))

      

