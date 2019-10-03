import numpy as np
from matplotlib import pyplot as plt
import cv2
from mss import mss
from PIL import Image
import time

mon = {'top': 0, 'left': 0, 'width': 200, 'height': 200}

sct = mss()

im = sct.grab(mon)
img = Image.frombytes('RGB', im.size, im.rgb, decoder_name='raw')
image = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)

plt.ion()
fig = plt.figure()
a = fig.add_subplot(1,2,1)
#a.imshow(image)
b = fig.add_subplot(1,2,2)
#b.imshow(image)
plt.show()

while 1:
    im = sct.grab(mon)
    img = Image.frombytes('RGB', im.size, im.rgb, decoder_name='raw')
    #image = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
    image = np.array(img)
    edges = cv2.Canny(image, 200, 202)
    #cv2.imshow('test', edges)
    a.clear()
    a.imshow(image)
    b.imshow(edges)
    plt.pause(0.01)
    #if cv2.waitKey(25) & 0xFF == ord('q'):
    #    cv2.destroyAllWindows()
    #    break