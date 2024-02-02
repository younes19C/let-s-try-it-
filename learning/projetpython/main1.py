from partie1 import*
from partie2 import*
from partie3 import*
from partie4 import*
from partie5 import*

# Fonction pour afficher le menu principal
def afficher_menu_principal():
    print("Menu Principal")
    print("1. Les images Noir et blanc")
    print("2. Les images en niveau de gris")
    print("3. Les images en couleur (RGB)")
    print("4. Quitter")
    choix_principal = input("Choisissez une option : ")
    return choix_principal

# Fonction principale
def main():
    choix_principal = afficher_menu_principal()

    while choix_principal != "4":
        if choix_principal == "1":
            # Menu pour les images Noir et blanc
            print("Sous-menu - Les images Noir et blanc")
            print("1. Créer une image noire")
            print("2. Créer une image blanche")
            print("3. Créer une image noir et blanc")
            print("4. Créer le négatif d'une image")
            choix_partie1 = input("Choisissez une option : ")

            if choix_partie1 == "1":
                # Créer une image noire
                h = int(input("Hauteur de l'image noire : "))
                l = int(input("Largeur de l'image noire : "))
                img = image_noire(h, l)
                AfficherImg(img)
                print("Image noire créée avec succès!")

            elif choix_partie1 == "2":
                # Créer une image blanche
                h = int(input("Hauteur de l'image blanche : "))
                l = int(input("Largeur de l'image blanche : "))
                img = image_blanche(h, l)
                AfficherImg(img)
                print("Image blanche créée avec succès!")

            elif choix_partie1 == "3":
                # Créer une image noir et blanc
                h = int(input("Hauteur de l'image noir et blanc : "))
                l = int(input("Largeur de l'image noir et blanc : "))
                img = creerImgBlancNoir(h, l)
                AfficherImg(img)
                print("Image noir et blanc créée avec succès!")

            elif choix_partie1 == "4":
                # Créer le négatif d'une image
                chemin = input("Chemin de l'image : ")
                img = ouvrir(chemin)
                img_negatif = negatif(img)
                AfficherImg(img_negatif)
                print("Négatif de l'image créé avec succès!")

            else:
                print("Option invalide. Veuillez réessayer.")

        elif choix_principal == "2":
            # Menu pour les images en niveau de gris
            print("Sous-menu - Les images en niveau de gris")
            print("1. Calculer la luminance d'une image")
            print("2. Calculer le contraste d'une image")
            print("3. Afficher la profondeur d'une image")
            print("4. Ouvrir une image")
            choix_partie2 = input("Choisissez une option : ")

            if choix_partie2 == "1":
                # Calculer la luminance d'une image
                chemin = input("Chemin de l'image : ")
                img = ouvrir(chemin)
                lum = luminance(img)
                print("Luminance de l'image : ", lum)

            elif choix_partie2 == "2":
                # Calculer le contraste d'une image
                chemin = input("Chemin de l'image : ")
                img = ouvrir(chemin)
                contr = constrast(img)
                print("Contraste de l'image : ", contr)

            elif choix_partie2 == "3":
                # Afficher la profondeur d'une image
                chemin = input("Chemin de l'image : ")
                img = ouvrir(chemin)
                prof = profondeur(img)
                print("Profondeur de l'image : ", prof, " bits par pixel")

            elif choix_partie2 == "4":
                # Ouvrir une image
                chemin = input("Chemin de l'image : ")
                img = ouvrir(chemin)
                AfficherImg(img)

            else:
                print("Option invalide. Veuillez réessayer.")

        elif choix_principal == "3":
            # Menu pour les images en couleur (RGB)
            print("Sous-menu - Les images en couleur (RGB)")
            print("1. Initialiser une image RGB")
            print("2. Effectuer la symétrie horizontale d'une image RGB")
            print("3. Effectuer la symétrie verticale d'une image RGB")
            print("4. Convertir une image RGB en niveaux de gris")
            choix_partie3 = input("Choisissez une option : ")

            if choix_partie3 == "1":
                # Initialiser une image RGB
                h = int(input("Hauteur de l'image RGB : "))
                l = int(input("Largeur de l'image RGB : "))
                img_rgb = initImageRGB(h, l)
                AfficherImg(img_rgb)
                print("Image RGB créée avec succès!")

            elif choix_partie3 == "2":
                # Effectuer la symétrie horizontale d'une image RGB
                chemin = input("Chemin de l'image RGB : ")
                img_rgb = ouvrir(chemin)
                img_symH = symetrieH(img_rgb)
                AfficherImg(img_symH)
                print("Symétrie horizontale de l'image RGB réalisée avec succès!")

            elif choix_partie3 == "3":
                # Effectuer la symétrie verticale d'une image RGB
                chemin = input("Chemin de l'image RGB : ")
                img_rgb = ouvrir(chemin)
                img_symV = symetrieV(img_rgb)
                AfficherImg(img_symV)
                print("Symétrie verticale de l'image RGB réalisée avec succès!")

            elif choix_partie3 == "4":
                # Convertir une image RGB en niveaux de gris
                chemin = input("Chemin de l'image RGB : ")
                img_rgb = ouvrir(chemin)
                img_gris = grayscale(img_rgb)
                AfficherImg(img_gris)
                print("Conversion de l'image RGB en niveaux de gris réalisée avec succès!")

            else:
                print("Option invalide. Veuillez réessayer.")

        else:
            print("Option invalide. Veuillez réessayer.")

        choix_principal = afficher_menu_principal()

    print("Programme terminé.")

# Appeler la fonction principale
if __name__ == "__main__":
    main()






