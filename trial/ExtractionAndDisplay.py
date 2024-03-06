import numpy as np
import cv2
from PIL import Image
import pytesseract
from pytesseract import Output

img = cv2.imread('image_03.png',0) #CHANGE THIS
norm_img = np.zeros((img.shape[0], img.shape[1]))
norm_img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
norm_img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]
norm_img = cv2.GaussianBlur(img, (1, 1), 0)

#IMAGE ONE
filename = 'image_03.png' #CHANGE THIS
image = cv2.imread(filename)

#dictionary
# DICT = {'level': [1, 2, 3, 4, 5, 5, 5],
#         'page_num': [1, 1, 1, 1, 1, 1, 1],
#         'block_num': [0, 1, 1, 1, 1, 1, 1],
#         'par_num': [0, 0, 1, 1, 1, 1, 1],
#         'line_num': [0, 0, 0, 1, 1, 1, 1],
#         'word_num': [0, 0, 0, 0, 1, 2, 3],
#         'left': [0, 26, 26, 26, 26, 110, 216],
#         'top': [0, 63, 63, 63, 63, 63, 63],
#         'width': [300, 249, 249, 249, 77, 100, 59],
#         'height': [150, 25, 25, 25, 25, 19, 19],
#         'conf': ['-1', '-1', '-1', '-1', 97, 96, 96],
#         'text': ['', '', '', '', 'Testing', 'Tesseract', 'OCR']}

results = pytesseract.image_to_data(image,output_type=Output.DICT)

for i in range(0, len(results["text"])):
   x = results["left"][i]
   y = results["top"][i]

   w = results["width"][i]
   h = results["height"][i]

   text = results["text"][i]
   conf = int(results["conf"][i])

   if conf > 70:
       text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
       cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
       cv2.putText(image, text, (x, y - 10),
cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 200), 2)


window_name = 'image'
cv2.imshow(window_name, image)
cv2.waitKey(0)
