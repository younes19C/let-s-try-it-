from random import randint
n = randint(1, 1000)
for i in range(5):
    var = int(input("Entrez un nombre:"))
    if var < n:
        print(var, "est plus petite")
    elif var > n:
        print(var, "est plus grande ")
    if var == n:
        print("bravo !")
        break