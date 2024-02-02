k=int(input("enter un entier  n  "))
somme =0
if k!=0 :
    for i in range(1,k+1):
        somme=somme+(1/i)
    print(somme)
else :
    print("Erreur")