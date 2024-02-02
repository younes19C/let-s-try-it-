def suite(n):
    u=1
    for i in range(1,n+1) :
     u=u*u+3
    return u 
a=int(input("entrez un entier : "))
def rang(a):
   n=0
   while true :
        if(suite(n)>a):
            return n 
        n+=1
print(rang(a))  






