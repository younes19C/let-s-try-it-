n = int(input("Donnez la valeur de n:"))
somme = 0
produit = 1
while n > 0:
    somme += n % 10
    produit *= n % 10
    n //= 10
print("La somme de chiffres est :", somme)
print("La produit de chiffres est :", produit)
                
