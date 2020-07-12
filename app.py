import cv2
import numpy as np
import pytesseract
from pytesseract import Output
import argparse

pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img =cv2.imread("OCR1.jpg");
img =cv2.resize(img, None, fx=0.7, fy=0.7)


text=pytesseract.image_to_string(img)
# print(text)
print('IEC:',text.split('TEC')[1][0:1])
print('PORT OF LOADING:',text.split('Port of Loading :')[1][0:20])
print('PORT OF DISCHARGE:',text.split('Port of Discharge:')[1][0:6])
print('GROSS WT(KGS):',text.split('Gross Wt(KGS) :')[1][1: 12])
print('COUNTRY OF DEST:',text.split('Country of Dest')[1][1:15])
print('TOTAL PKGS:',text.split('Total Pkgs. :')[1][0:5])
print('LOSSE PCKTS:',text.split('Loose pckts :')[1][1:2])
print('NET WT(KGS):',text.split('Net Wt(KGS) :')[1][0:9])
print('NO. OF CTRS:',text.split('No.of Ctrs. :')[1][0:3])
# text_file=open('Output.txt',"w")
# text_file.write(text)
# text_file.close()


cv2.waitKey(0)
