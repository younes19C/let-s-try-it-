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