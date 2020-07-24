import cv2
import numpy as np
import pytesseract
from pytesseract import Output
import argparse

pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img =cv2.imread('test.jpg')
img =cv2.resize(img, None, fx=0.7, fy=0.7)


text=pytesseract.image_to_string(img)