from pdf2image import convert_from_path
import pytesseract
import os

# Path to your PDF
pdf_path = '/Users/julioalonzom/Desktop/coding-projects/digitalizing_books'

# Convert PDF to list of images
pages = convert_from_path(pdf_path, 300)  # 300 DPI is a good resolution for OCR

# Iterate over each page, apply OCR, and save the text
for i, page in enumerate(pages):
    text = pytesseract.image_to_string(page, lang='eng')  # Use the appropriate language code
    with open(f'output_page_{i}.txt', 'w') as file:
        file.write(text)
