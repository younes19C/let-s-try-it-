####Q1##
def est_amstrong(n)
    s=0
    num=n
    while (n>0):
        mod =n%10 
        n=n/10
        s+=mod*3
    if s== num :
        return True 
    else:
        return False 
###Q2~
def liste_amstrong(m):
    for i in range (m+1):
        if est_amstrong(i)<= m:
            print(i)
