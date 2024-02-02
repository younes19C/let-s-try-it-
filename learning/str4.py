#Une chaˆıne de caract`eres en python est une suite de caractere non modifiable et ordonner
# syntaxe
ch='hi its me '
ch1="I love you "
print(ch1[0:6])
print(ch[0])
#nom=str(input("what's your name "))
#print(nom)
#print(type(nom ))
#Les operateurs : +, * et in
# concatiner 2 strings
print(ch+ch1)
#l'operateur * permet de reputer une string n fois (ch1*2)
print(ch1*10)
# in
print('hi' in ch)
# parcourir un string 
for i in ch :
    print(i)

#Les fonctions pr´ed´efinies sur les chaˆınes
'''retourner la taille d’une chaˆıne : len
comparer deux chaˆınes de caract`eres : cmp
calculer le nombre d’occurence d’un caract`ere : count
conversion de majuscules vers minuscules (resp min vers maj)
upper et lower
d´ecoupage en chaˆınes plus petites : split
recherche de mots, etc.).
'''
#count 
ch2='Morocco'
ch2.count('o')
#chr(n) : affiche un caract`ere `a partir de son code num´erique (ASCII) n
print(chr(65))
#ord(’A’) donne le code ascii d'un caractere
print(ord('9'))

#max(chaine) renvoie le caract`ere dont le code num´erique est le plus ´elev´e
max('maroc')
#>>>’r’
#min(chaine) renvoie le caract`ere dont le code num´erique est le moins ´elev´e
min('maroc')
#’a’
#max(ch1,ch2) renvoie la chaˆıne qui se classe alphab´etiquement apr`es l’autre
max('Ali','Ahmed')
#’Ali’
#min(ch1,ch2) renvoie la chaˆıne qui se classe alphab´etiquement avant l’autre
min('Ali','Ahmed')
# ’Ahmed’
#ch.upper() metre une chaine de caractere on gras 
print(ch1.upper())
#ch.lower() metre une chaine de caractere on muniscules
print(ch1.lower())

