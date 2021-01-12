from PIL import Image
import pytesseract

image_path = '../data/input/test.png'
text = pytesseract.image_to_string(Image.open(image_path), lang='chi_sim')
print(text)