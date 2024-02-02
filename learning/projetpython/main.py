from partie1 import*
from partie2 import*
from partie3 import*
from partie4 import*
from partie5 import*
  

def demander_dimensions():
    hauteur = int(input("Entrez la hauteur de l'image : "))
    largeur = int(input("Entrez la largeur de l'image : "))
    return hauteur, largeur

def afficher_menu_partie1():
    print("------ Partie 1 et 2 - Les images Noir et blanc ------")
    print("1. Créer une image noire")
    print("2. Créer une image blanche")
    print("3. Créer une image noir-blanc")
    print("4. Créer une image négatif")
    print("0. Quitter")

def afficher_menu_partie2():
    print("------ Partie 3 - Les images en niveau de gris ------")
    print("1. Afficher une image")
    print("2. Ouvrir une image depuis un fichier")
    print("3. Sauvegarder l'image actuelle")
    print("4. Calculer la luminance")
    print("5. Calculer le contraste")
    print("6. Inverser les couleurs")
    print("7. Flip horizontal")
    print("8. Poser verticalement")
    print("9. Poser horizontalement")
    print("0. Quitter")

def afficher_menu_partie3():
    print("------ Partie 4 - Images en couleur et opérations diverses ------")
    print("1. Initialiser une image RGB aléatoire")
    print("2. Effectuer une symétrie horizontale")
    print("3. Effectuer une symétrie verticale")
    print("4. Convertir une image RGB en niveaux de gris")
    print("0. Quitter")

def main():
    img = None

    while True:
        print("\n------ Menu principal ------")
        print("1. Partie 1 et  - Les images Noir et blanc")
        print("2. Partie 3 - Les images en niveau de gris")
        print("3. Partie 4 - Images en couleur et opérations diverses")
        print("0. Quitter")

        choix_principal = input("Entrez votre choix (0-3) : ")

        if choix_principal == "0":
            print("Programme terminé.")
            break
        elif choix_principal == "1":
            while True:
                afficher_menu_partie1()
                choix_partie1 = input("Entrez votre choix pour la Partie 1 (0-4) : ")

                if choix_partie1 == "0":
                    print("Partie 1 terminée.")
                    break
                elif choix_partie1 in ["1", "2", "3", "4"]:
                    hauteur, largeur = demander_dimensions()
                    if choix_partie1 == "1":
                        img = image_noire(hauteur, largeur)
                    elif choix_partie1 == "2":
                        img = image_blanche(hauteur, largeur)
                    elif choix_partie1 == "3":
                        img = creerImgBlancNoir(hauteur, largeur)
                    elif choix_partie1 == "4":
                        img = creerImgBlancNoir(hauteur, largeur)
                        img = negatif(img)
                    AfficherImg(img)
        elif choix_principal == "2":
            while True:
                afficher_menu_partie2()
                choix_partie2 = input("Entrez votre choix pour la Partie 2 (0-9) : ")

                if choix_partie2 == "0":
                    print("Partie 2 terminée.")
                    break
                elif choix_partie2 == "1":
                    if img is not None:
                        AfficherImg(img)
                    else:
                        print("Aucune image à afficher. Veuillez d'abord créer ou ouvrir une image.")
                elif choix_partie2 == "2":
                    chemin = input("Entrez le chemin de l'image : ")
                    img = ouvrirImage(chemin)
                    AfficherImg(img)
                elif choix_partie2 == "3":
                    if img is not None:
                        nom_fichier = input("Entrez le nom du fichier de sauvegarde (avec extension) : ")
                        saveImage(img, nom_fichier)
                        print("Image sauvegardée.")
                    else:
                        print("Aucune image à sauvegarder. Veuillez d'abord créer ou ouvrir une image.")
                elif choix_partie2 == "4":
                    if img is not None:
                        print("Luminance de l'image : ", luminance(img))
                    else:
                        print("Aucune image à traiter. Veuillez d'abord créer ou ouvrir une image.")
                elif choix_partie2 == "5":
                    if img is not None:
                        print("Contraste de l'image : ", constrast(img))
                    else:
                        print("Aucune image à traiter. Veuillez d'abord créer ou ouvrir une image.")
                elif choix_partie2 == "6":
                    if img is not None:
                        img = inverser(img)
                        print("Image inversée.")
                        AfficherImg(img)
                    else:
                        print("Aucune image à inverser. Veuillez d'abord créer ou ouvrir une image.")
                elif choix_partie2 == "7":
                    if img is not None:
                        img = flipH(img)
                        print("Image flip horizontalement.")
                        AfficherImg(img)
                    else:
                        print("Aucune image à traiter. Veuillez d'abord créer ou ouvrir une image.")
                elif choix_partie2 == "8":
                    if img is not None:
                        img2 = ouvrir(creerImgBlancNoir(hauteur, largeur))
                        img = poserV(img, img2)
                        print("Images posées verticalement.")
                        AfficherImg(img)
                    else:
                        print("Aucune image à traiter. Veuillez d'abord créer ou ouvrir une image.")
                elif choix_partie2 == "9":
                    if img is not None:
                        img2 = ouvrir(creerImgBlancNoir(hauteur, largeur))
                        img = poserH(img, img2)
                        print("Images posées horizontalement.")
                        AfficherImg(img)
                    else:
                        print("Aucune image à traiter. Veuillez d'abord créer ou ouvrir une image.")
        elif choix_principal == "3":
            while True:
                afficher_menu_partie3()
                choix_partie3 = input("Entrez votre choix pour la Partie 3 (0-4) : ")

                if choix_partie3 == "0":
                    print("Partie 3 terminée.")
                    break
                elif choix_partie3 == "1":
                    hauteur, largeur = demander_dimensions()
                    img = initImageRGB(hauteur, largeur)
                    print("Image RGB initialisée.")
                    AfficherImg(img)
                elif choix_partie3 == "2":
                    if img is not None:
                        img = symetrieH(img)
                        print("Symétrie horizontale effectuée.")
                        AfficherImg(img)
                    else:
                        print("Aucune image à traiter. Veuillez d'abord créer ou ouvrir une image.")
                elif choix_partie3 == "3":
                    if img is not None:
                        img = symetrieV(img)
                        print("Symétrie verticale effectuée.")
                        AfficherImg(img)
                    else:
                        print("Aucune image à traiter. Veuillez d'abord créer ou ouvrir une image.")
                elif choix_partie3 == "4":
                    if img is not None:
                        img_gray = grayscale(img)
                        print("Conversion en niveaux de gris effectuée.")
                        AfficherImg(img_gray)
                    else:
                        print("Aucune image à traiter. Veuillez d'abord créer ou ouvrir une image.")

if __name__ == "__main__":
    main()



