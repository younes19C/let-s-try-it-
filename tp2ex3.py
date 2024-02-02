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
ch="Il fait beau"