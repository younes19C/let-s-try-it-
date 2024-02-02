import matplotlib.pyplot as plt

def AfficherImg(img, m=1, n=0):
    plt.axis("off")  # Disable axes
    plt.imshow(img, cmap='gray', interpolation="nearest", vmax=m, vmin=n)
    plt.show()

img1 = plt.imread("C:\\Users\\RPC\\Desktop\\Screenshot\\yyyy.png")
AfficherImg(img1)