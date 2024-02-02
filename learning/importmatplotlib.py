import matplotlib.pyplot as plt
import numpy as np
def AfficherImg(img, m=1, n=0):
    plt.axis("off")  # Disable axes
    plt.imshow(img, interpolation="nearest")
    plt.show()
    plt.figure(facecolor='black')
img = np.array([[1,1],[1,1]])
AfficherImg(img)