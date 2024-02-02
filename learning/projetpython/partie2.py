
#**************\\  Les images Noir et blanc //**************#
import numpy as np
from partie1 import *
#**************\\  Création  d'une image noir //**************#
def image_noire(h, l):
    img=np.zeros((h,l))
    return img
#**************\\ Création  d'une image blanche //**************#
def image_blanche(h,l):
    img=np.ones((h,l))
    return img
#**************\\  Création  d'une image noir et blanc //**************#
def creerImgBlancNoir(h,l):
    img=np.array([[(i+j)%2 for i in range(l)]for j in range(h)])
    return img
#**************\\  Construction du negative d'une image //**************#
def negatif(Img):
    img=np.array([[1-j for j in i] for i in Img])
    return img
# img=np.array[[0,0][0,0][0,0]]
# AfficherImg(image_noire(10,10))
# AfficherImg(image_blanche(10,10))
# AfficherImg(creerImgBlancNoir(10,10))
AfficherImg(negatif(creerImgBlancNoir(10,10)))
