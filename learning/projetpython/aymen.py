def calculer_luminance(image):
    """
    Calcule la luminance moyenne d'une image représentée par une liste de listes.

    Args:
        image (list): Une liste de listes représentant l'image.

    Returns:
        float: La luminance moyenne de l'image.
    """
    hauteur = len(image)
    largeur = len(image[0]) if hauteur > 0 else 0  # Assurez-vous que l'image a au moins une ligne pour éviter une division par zéro

    # Calculer la somme totale des valeurs de luminance dans l'image
    somme_totale = sum(sum(ligne) for ligne in image)

    # Calculer la luminance moyenne
    luminance_moyenne = somme_totale / (hauteur * largeur) if (hauteur * largeur) > 0 else 0

    return luminance_moyenne
print(calculer_luminance("\\C:\\Users\\RPC\\Pictures\\Screenshots\\Screenshot 2023-12-25 221441.png"))