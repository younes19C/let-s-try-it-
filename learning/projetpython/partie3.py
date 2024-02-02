
import numpy as np
from partie1 import ouvrirImage
#********************\\ Question1: luminance d'une image //********************#
def luminance(Img):
    return (Img.max()+Img.min())/2

#********************\\ Question2: Contraste d'une image //********************#
def constrast(Img):
    s=0
    for i in Img:
        for j in i:
            s+=(j[0]-luminance(Img))**2
    # au lieu de transformer à deux dimension j'ai pris un j[0] puisque les trois en la meme valeur
    return (1/(len(Img)*len(Img[0])))*s

#********************\\ Question3: Valeur maximale d'un pixel dans l'image //********************#
def profondeur(Img):
    if Img.ndim==2:
        if Img.max()==1:
            return 1
        else: return 8
    else:
        return 24
    #par unité bit

#********************\\ Question4:La matrice représentant l'image A  //********************#
def ouvrir(Img):
    return ouvrirImage(Img)

#********************\\ Question5: luminance d'une image //********************#
