import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#image = mpimg.imread("test.png")
image = cv2.imread("test.png")
fig = plt.figure()
ax = plt.axes([0,0,1,1])
plt.imshow(image, interpolation="nearest", aspect='auto')
DPI = fig.get_dpi()
fig.set_size_inches(image.shape[1]/float(DPI),image.shape[0]/float(DPI))
plt.axis("off")   # turns off axes
plt.axis("tight")  # gets rid of white border
plt.axis("image")  # square up the image instead of filling the "figure" space
plt.show()
fig.savefig("out.png")
