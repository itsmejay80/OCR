from pdf2image import convert_from_path
pages=convert_from_path('E:\\Code\\OCR-Project\\OCR_1.pdf')

for page in pages:
    page.save('E:\\Code\\OCR-Project\\OCR1.jpg', 'JPEG')