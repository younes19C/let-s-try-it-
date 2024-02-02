n=int(input("entrer un entier "))
####Q1####
def puiss(n):
    return 2*n
####Q2###

def sommepuiss2(n):
    s=1
    for i in  range(1,n+1):
        s=s+puiss2(i)
    return s
####q3###
def fact(n):
    if n==0 :
        return 1
    else :
        return n*fact(n-1)
###Q4### 
def sommefact(n):
    sf =1
    for i in range (1,n+1):
        sf+=(-1)*i/fact(i)
    return sf
def sommefrac(n):
    return sommepuiss2(n)/sommefact(n)
