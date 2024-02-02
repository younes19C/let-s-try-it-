# EXERCICE 1 :
def somme2(a,b):
return a+b
def moyenne(a,b):
return (a+b)/2
a = int(input("entrer a : "))
b = int(input("entrer b : "))
print("la somme est = ", somme2(a,b))
print("la moyenne est = ", moyenne(a,b))


# EXERCICE 4 :
def tablemulti(n):
for i in range(1,11):
print(n,'*', i , '=', n*i)
def tablemultifraction(n,d,f):
for i in range(d,f+1):
print(n,'*', i , '=', n*i)
n = int(input("entrer un nombre :"))
d = int(input("entrer d : "))
f = int(input("entrer f :"))
tablemulti(n)
tablemultifraction(n,d,f)


# EXERCICE 5 :
def pgcd(a,b):
if a==0:
return b
elif b==0:
return a
if a<b:
m=a
else :
m=b
for i in range(1,m+1):
if a%i==0 and b%i==0:
pg=i
return pg
a = int(input("enter un nombre :"))
b = int(input("entrer un nombre :"))
print(f"le pgcd de {a} et {b} est : ", pgcd(a,b))

## EXERCICE 3 :
def Min2(a,b):
if a>b:
return b
else :
return a
def Min3(a,b,c):
m = min(a,b,c)
return m
a = int(input("entrer un nombre : "))
b = int(input("entrer un nombre : "))
c = int(input("entrer un nombre : "))
print(f"le min entre {a} et {b} est : ", Min2(a,b))
print(f"le min entre {a}, {b} et {c} est : ", Min3(a,b,c))


### EXERCICE 2 :
def estpairf(n):
if n%2==0:
return 1
else :
return 0
def estpairp(n):
if n%2==0:
print("le nombre est pair")
else :
print("le nombre est impair")
n=int(input("entrer n : "))
print(estpairf(n))
estpairp(n)