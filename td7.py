"""
#EX1
class Segment:
    def __init__(self, extr1, extr2):
        self.extr1 = extr1
        self.extr2 = extr2
        self.ordonner()

    def ordonner(self):
        if self.extr1 > self.extr2:
            self.extr1, self.extr2 = self.extr2, self.extr1

    def getLongueur(self):
        return self.extr2 - self.extr1

    def appartient(self, x):
        return self.extr1 <= x <= self.extr2

    def Afficher(self):
        return f"SEGMENT[{self.extr1},{self.extr2}]"


# Programme principal TestSegment.py
while True:
    extr1_input = int(input("Entrez la valeur de extr1 : "))
    extr2_input = int(input("Entrez la valeur de extr2 : "))

    segment = Segment(extr1_input, extr2_input)

    print("État de l'objet segment :", segment.Afficher())
    print("Longueur du segment :", segment.getLongueur())

    x = int(input("Entrez la valeur de x pour vérifier son appartenance au segment : "))
    if segment.appartient(x):
        print(f"Le point {x} appartient au segment.")
    else:
        print(f"Le point {x} n'appartient pas au segment.")

    choix = input("Voulez-vous continuer (O/N) ? ")
    if choix.lower() != 'o':
        break """
#ex2 

class Rationnel:
    def __init__(self, numerateur, denominateur=1):
        self.numerateur = numerateur
        self.denominateur = denominateur
        self.simplifier()

    def simplifier(self):
        # Fonction pour simplifier la fraction en divisant par le PGCD
        def pgcd(a, b):
            while b:
                a, b = b, a % b
            return a

        diviseur = pgcd(self.numerateur, self.denominateur)
        self.numerateur //= diviseur
        self.denominateur //= diviseur

    def __repr__(self):
        return f'Rationnel({self.numerateur}, {self.denominateur})'

    def __add__(self, other):
        if isinstance(other, Rationnel):
            nouveau_numerateur = self.numerateur * other.denominateur + other.numerateur * self.denominateur
            nouveau_denominateur = self.denominateur * other.denominateur
            return Rationnel(nouveau_numerateur, nouveau_denominateur)
        else:
            raise TypeError("L'opération n'est pas supportée avec ce type.") 

    # Définir d'autres opérations arithmétiques si nécessaire : soustraction, multiplication, division, etc.
q1 = Rationnel(7, 9)
print(q1)  # Affichera Rationnel(1, 2)

q2 = Rationnel(8,3)
print(q2)  # Affichera Rationnel(3, 2)

q3 = q1 + q2
print(q3)  # Affichera Rationnel(2, 1)
'''
#EX3
#Q1
class Compte:
    """
    Classe de base pour tous les types de comptes bancaires.

    Attributs:
        code: Un identifiant unique pour le compte.
        solde: Le solde actuel du compte.
        nbComptes: Le nombre de comptes associés à ce client.
    

'''
def __init__(self, code, solde):
        """
        Crée un nouveau compte bancaire.

        Args:
            code: L'identifiant du compte.
            solde: Le solde initial du compte.
        """
        self.code = code
        self.solde = solde

def get_code(self):
        """
        Retourne l'identifiant du compte.

        Returns:
            Le code du compte.
        """
        return self.code

def set_code(self, code):
        """
        Met à jour l'identifiant du compte.

        Args:
            code: Le nouveau code du compte.
        """
        self.code = code

def get_solde(self):
        """
        Retourne le solde actuel du compte.

        Returns:
            Le solde du compte.
        """
        return self.solde

def set_solde(self, solde):
        """
        Met à jour le solde actuel du compte.

        Args:
            solde: Le nouveau solde du compte.
        """
        self.solde = solde

def verser(self, montant):
        """
        Verse une somme d'argent sur le compte.

        Args:
            montant: Le montant à verser.
        """
        self.solde += montant

def retirer(self, montant):
        """
        Retire une somme d'argent du compte.

        Args:
            montant: Le montant à retirer.
        """
        self.solde -= montant

def __str__(self):
        """
        Retourne une représentation du compte sous forme de chaîne de caractères.

        Returns:
            Une chaîne de caractères représentant le compte.
        """
        return f"Compte {self.code} : solde = {self.solde}"  

#Q2
from compte import Compte

class CompteSimple(Compte):
    """
    Représente un compte bancaire courant.

    Attributs:
        code: Un identifiant unique pour le compte.
        solde: Le solde actuel du compte.
        nbComptes: Le nombre de comptes associés à ce client.
        decouvert: Le montant du découvert autorisé pour le compte.
    """

    def __init__(self, code, solde, decouvert):
        """
        Crée un nouveau compte bancaire courant.

        Args:
            code: L'identifiant du compte.
            solde: Le solde initial du compte.
            decouvert: Le montant du découvert autorisé pour le compte.
        """
        super().__init__(code, solde)
        self.decouvert = decouvert

    def retirer(self, montant):
        """
        Retire une somme d'argent du compte.

        Args:
            montant: Le montant à retirer.

        Returns:
            True si le retrait a réussi, False sinon.
        """
        if montant <= self.solde + self.decouvert:
            self.solde -= montant
            return True
        else:
            return False

    def __str__(self):
        """
        Retourne une représentation du compte sous forme de chaîne de caractères.

        Returns:
            Une chaîne de caractères représentant le compte.
        """
        return f"Compte Simple {self.code} : solde = {self.solde}, découvert = {self.decouvert}"
#Q3
from compte import Compte

class CompteEpargne(Compte):
    """
    Représente un compte bancaire d'épargne.

    Attributs:
        code: Un identifiant unique pour le compte.
        solde: Le solde actuel du compte.
        nbComptes: Le nombre de comptes associés à ce client.
        taux: Le taux d'intérêt appliqué au compte.
    """

    def __init__(self, code, solde, taux):
        """
        Crée un nouveau compte bancaire d'épargne.

        Args:
            code: L'identifiant du compte.
            solde: Le solde initial du compte.
            taux: Le taux d'intérêt appliqué au compte.
        """
        super().__init__(code, solde)
        self.taux = taux

    def calculer_interets(self):
        """
        Calcule les intérêts du compte.

        Returns:
            Le montant des intérêts.
        """
        return self.solde * self.taux

    def __str__(self):
        """
        Retourne une représentation du compte sous forme de chaîne de caractères.

        Returns:
            Une chaîne de caractères représentant le compte.
        """
        return f"Compte Epargne {self.code} : solde = {self.solde}, taux = {self.taux}"
#Q4from compte import Compte

class ComptePayant(Compte):
    """
    Représente un compte bancaire payant.

    Attributs:
        code: Un identifiant unique pour le compte.
        solde: Le solde actuel du compte.
        nbComptes: Le nombre de comptes associés à ce client.
        frais: Les frais mensuels facturés pour le compte.
    """

    def __init__(self, code, solde, frais):
        """
        Crée un nouveau compte bancaire payant.

        Args:
            code: L'identifiant du compte.
            solde: Le solde initial du compte.
            frais: Les frais mensuels facturés pour le compte.
        """
        super().__init__(code, solde)
        self.frais = frais

    def calculer_frais(self):
        """
        Calcule les frais du compte.

        Returns:
            Le montant des frais.
        """
        return self.frais

    def __str__(self):
        """
        Retourne une représentation du compte sous forme de chaîne de caractères.

        Returns:
            Une chaîne de caractères représentant le compte.
        """
        return f"Compte Payant {self.code} : solde = {self.solde}, frais = {self.frais}"
#Q5
from compte import Compte, CompteSimple, CompteEpargne, ComptePayant

def main():
    # Création d'un compte courant
    compte_courant = CompteSimple("1234567890", 1000, 500)

    # Affichage du solde du compte
    print(compte_courant.get_solde())
    # 1000

    # Retrait d'une somme d'argent sur le compte
    compte_courant.retirer(200)

    # Affichage du nouveau solde du compte
    print(compte_courant.get_solde())
    # 800

    # Création d'un compte d'épargne
    compte_epargne = CompteEpargne("9876543210", 1000, 0.05)

    # Affichage du solde du compte
    print(compte_epargne.get_solde())
    # 1000

    # Calcul des intérêts
    interets = compte_epargne.calculer_interets()

    # Affichage des intérêts
    print(interets)
    # 50

    # Création d'un compte payant
    compte_payant = ComptePayant("0123456789", 1000, 10)

    # Affichage du solde du compte
    print(compte_payant.get_solde())
    # 1000

    # Calcul des frais
    frais = compte_payant.calculer_frais()

    # Affichage des frais
    print(frais)
    # 10

if __name__ == "__main__":
    main()
