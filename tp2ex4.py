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