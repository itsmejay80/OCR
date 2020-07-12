import cv2
import numpy as np
import pytesseract
from pytesseract import Output
import argparse

pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img =cv2.imread("OCR2.jpg");
img =cv2.resize(img, None, fx=0.7, fy=0.7)
img2=cv2.bilateralFilter(img,9,75,75)
gray=cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

text=pytesseract.image_to_string(gray)

print('CTR NO:',text.split('Date')[1][2:13])
print('SIZE:',text.split('Date')[1][14:17])
print('SEAL NO:',text.split('Date')[1][17:30])
print('DATE:',text.split('Date')[1][31:41])

text_file=open('Output2.txt',"w")
text_file.write(text)
text_file.close()


cv2.waitKey(0)