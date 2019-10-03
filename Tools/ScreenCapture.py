import numpy as np
from matplotlib import pyplot as plt
import cv2
from mss import mss
from PIL import Image

mon = {'top': 0, 'left': 0, 'width': 200, 'height': 200}

sct = mss()

while 1:
    im = sct.grab(mon)
    img = Image.frombytes('RGB', im.size, im.rgb, decoder_name='raw')
    image = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
    edges = cv2.Canny(image, 200, 202)
    cv2.imshow('Image', image)
    cv2.imshow('Edges', edges)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break