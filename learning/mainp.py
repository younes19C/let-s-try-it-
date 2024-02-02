# Définissez vos fonctions ici, telles que ouvrir_image(), afficher_noir(), afficher_blanc(), etc.

def menu():
    print("Que souhaitez-vous faire ?")
    print("1. Ouvrir une image")
    print("2. Afficher l'image en noir")
    print("3. Afficher l'image en blanc")
    print("4. Afficher l'image en noir et blanc")
    print("5. Inverser les couleurs de l'image")
    print("6. Sauvegarder l'image")
    print("7. Quitter")
    choix = input("Entrez le numéro de votre choix : ")
    return choix
commande=in

def main():

    # Initialisez l'image d'origine
    img = ouvrir("lena.jpg")

    # Afficher l'image d'origine
    AfficherImg(img)

    # Demandez à l'utilisateur d'entrer une commande
    print("Entrez une commande :")
    commande = input()

    # Exécutez la commande
    while commande != "quit":

        # Traitez la commande
        if commande == "luminance":
            lum = luminance(img)
            print("Luminance moyenne :", lum)
        elif commande == "contrast":
            cont = constrast(img)
            print("Contraste :", cont)
        elif commande == "image_noire":
            h = int(input("Entrez la hauteur de l'image :"))
            l = int(input("Entrez la largeur de l'image :"))
            img_noire = image_noire(h, l)
            AfficherImg(img_noire)
        elif commande == "image_blanche":
            h = int(input("Entrez la hauteur de l'image :"))
            l = int(input("Entrez la largeur de l'image :"))
            img_blanche = image_blanche(h, l)
            AfficherImg(img_blanche)
        elif commande == "damier":
            h = int(input("Entrez la hauteur de l'image :"))
            l = int(input("Entrez la largeur de l'image :"))
            img_damier = creerImgBlancNoir(h, l)
            AfficherImg(img_damier)
        elif commande == "negatif":
            img_negatif = negatif(img)
            AfficherImg(img_negatif)
        elif commande == "sym_h":
            img_sym_h = symetrieH(img)
            AfficherImg(img_sym_h)
        elif commande == "sym_v":
            img_sym_v = symetrieV(img)
            AfficherImg(img_sym_v)
        elif commande == "gris":
            img_gris = grayscale(img)
            AfficherImg(img_gris)
        elif commande == "pose":
            img_pose = poserH(img, ouvrir("baboon.png"))
            AfficherImg(img_pose)
        else:
            print("Commande inconnue")

        # Demandez à l'utilisateur d'entrer une nouvelle commande
        print("Entrez une commande :")
        commande = input()


if __name__ == "__main__":
    main()
