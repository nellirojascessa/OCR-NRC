import numpy as np
import cv2
from PIL import Image
import pytesseract

img = cv2.imread('image_02.png',0)
norm_img = np.zeros((img.shape[0], img.shape[1]))
norm_img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
norm_img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]
norm_img = cv2.GaussianBlur(img, (1, 1), 0)

#IMAGE ONE
# filename = 'image_01.png'
# img1 = np.array(Image.open(filename))
# text = pytesseract.image_to_string(img1)
# print(text)

#IMAGE TWO
filename = 'image_02.png'
img2 = np.array(Image.open(filename))
text = pytesseract.image_to_string(img2)
print(text)
