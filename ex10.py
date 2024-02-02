#Q1:
n=int(input(" Enter un entier n "))
p=int(input(" Enter un entier p "))
fact_n=1

for i in range(1,n+1):
    fact_n=fact_n*i
    i+=1
print(n,"! =",fact_n)

#Q2
fact_p=1
for i in range(1,p+1):
    fact_p=fact_p*i
    i+=1
print(p,"! =",fact_p)
fact_n_p=1
for i in range(1,(n-p)+1):
    fact_n_p=fact_n_p*i
    i+=1
print(n-p,"! =",fact_n_p)

comb = fact_n /fact_p*fact_n_p
print("le nombre de combinaison de p parmi n est :",comb)