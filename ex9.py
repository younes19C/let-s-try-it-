#1//
print("solition de lequation du premier order A*X+B=0 ")
A=float(input("veuillez enter le nomber A "))
B=float(input("veuillez enter le nomber B "))
C=float(input("veuillez enter le nomber C "))
if A==0 and B!=0 :
    input("veuillez enter le nomber A a nauveau ")
else :
    X=-B/A
    print("la solution de l'equation ",A,"*X+",B,"=0 est X=",X)

#2//
print("solutions d'une equation de deuxieme degre",A,"X^2+",B,"X +",C,"= 0")
delta=(B*B)-(4*A*C)
if (delta>0):
    print("cette equation admet deux solutions ")
    X1=(-B+sqrt(delta))/2*A
    X2=(-B-sqrt(delta))/2*A
    print("l'ensemble des solution est",X1,X2 )
elif(delta==0):
    print("cette equation admet une solution ")
    X3=(-B)/2*A
    print("la solution est ",X3)
else:
    print("eurrer")
    