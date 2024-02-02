from matplotlib import pyplot as plt 

#********** \\ Question 1 : AfficherImg // *********
def AfficherImg(img, m=1, n=0): 
    plt.axis("off")  # pour désactiver les axes 
    plt.imshow(img, cmap='gray', interpolation="nearest", vmax=m, vmin=n) 
    plt.show()


#********** \\ Question 2: ouvrir Image //*********
def ouvrirImage(chemin): 
    img=plt.imread(chemin) 
    return img 

#*********\\ Question 3 : save Image //************ 
def saveImage(img): 
    plt.imsave("image1.png",img) 


