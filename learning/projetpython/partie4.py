#********************\\ La partie4 //********************#
import numpy as np 
from partie3 import*
#********************\\ Question1: Inverse d'une image //********************#
def inverser(img):
    inv=np.array([[255-j for j in i] for i in img])
    return inv
#*******\\ Question6: la transformée d'une image  par la symétrie d’axe vertical //*********#
def flipH(img):
    t=[]
    for i in range(len(img)):
        t=t+[img[i][::-1]]
    return t
#********************\\ Question2: Poser vertical d'une image //********************#    
def poserV(img1,img2):
    img3=[]
    if profondeur(img1)==profondeur(img2):
        if len(img1[0])==len(img2[0]):
            img3+=list(img1)+list(img2)
            np.array(img3)
    return img3
#********************\\ Question3: Poser une image sur une autre //********************#
def poserH(img1, img2):
    img3=[[[0] for i in range(len(img1[0])+len(img2[0]))]for j in range(len(img1))]
    if profondeur(img1)==profondeur(img2):
        if len(img1)==len(img2):
            for i in range(len(img1)):
                img3[i]= list(img1[i])+list(img2[i])
    return np.array(img3)

