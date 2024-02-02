def masque(s, L):

  for i in L:
    if i < 0:
      raise ValueError("Les éléments du tuple L doivent être positifs")
  masque = ""
  for i in range(len(s)):
    if i in L:
      masque += s[i]

  return masque
print(masque("what the fuck ",(3,2,4,5,8,10)))
### ex 2
#q1
def FirstPosiTab(T):
  
  

  max = T[0]
  

  pos = 0

  

  for i in range(len(T)):
    
    if T[i] > max:
     
      max = T[i]
      pos = i

  return (max, pos)
T=(1,2,3,5,9,10)
print(FirstPosiTab(T))
#q2
""" def AllPosiTab(T):
  
  Prend un tableau T de nombres réels, et retourne un tuple contenant le plus grand élément et une liste de toutes les positions ce cette valeur maximale.

  Exemple :
  >>> AllPosiTab([1, 2, 3, 4, 5])
  (5, [4])


  # Initialise le maximum

  max = T[0]
  # Initialise la liste des positions du maximum

  positions = []

  # Parcourt le tableau T

  for i in range(len(T)):
    # Si T[i] est égal à max
    if T[i] == max:
      # Ajoute la position i à la liste des positions
      positions.append(i)

  # Retourne le tuple contenant le maximum et la liste des positions

  return (max, positions)
#Q3
def max2(L):
  # Vérifie que la longueur de la liste est supérieure ou égale à 2

  if len(L) < 2:
    raise ValueError("La longueur de la liste doit être supérieure ou égale à 2")

  # Initialise les deux maximums

  max1 = L[0]
  max2 = L[1]

  # Parcourt la liste L

  for i in range(2, len(L)):
    # Si L[i] est plus grand que max1
    if L[i] > max1:
      # Met à jour max1 et max2
      max2 = max1
      max1 = L[i]
    elif L[i] > max2:
      # Met à jour max2
      max2 = L[i]

  # Retourne le tuple contenant les deux maximums

  return (max1, max2)
## EX3
def ListeToTuple(L):

  # Convertit la liste L en tuple

  T = tuple(L)

  # Retourne le tuple T

  return T
#q2
def StrToTuple(s):

  # Convertit la chaîne de caractères s en tuple

  T = tuple(s)

  # Retourne le tuple T

  return T
#Q3
def TupleToList(T):

  # Convertit le tuple T en liste

  L = list(T)

  # Retourne la liste L

  return L
#q4
def TupleToStr(T):

  # Convertit le tuple T en chaîne de caractères

  s = ""
  for i in T:
    s += i

  # Retourne la chaîne de caractères s

  return s """
def MinToMajLigne(src):
  """
  Convertit tous les caractères de la chaîne src en majuscule en utilisant le code ASCII.

  Args:
    src: La chaîne à convertir.

  Returns:
    La nouvelle chaîne en majuscule.
  """

  new_str = ""
  for c in src:
    # Calcul du code ASCII du caractère.
    code_ascii = ord(c)

    # Si le code ASCII est compris entre 97 et 122, il s'agit d'une lettre minuscule.
    if 97 <= code_ascii <= 122:
      # Ajout de la lettre majuscule correspondante.
      new_str += chr(code_ascii - 32)
    else:
      # Ajout du caractère tel quel.
      new_str += c
  return new_str
print(MinToMajLigne("YOUnes chami" ))