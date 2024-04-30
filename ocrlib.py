import easyocr
import warnings

warnings.warn("RTX not found. Please use RTX to get super resoultion.")
from typing import OrderedDict 
def recognize_license_plate(image_path):
    
    reader = easyocr.Reader(['en'])
    
    
    result = reader.readtext(image_path)
    
    
    
    
    return result[0][1]


image_path = 'test_2.jpg'
recognized_text = recognize_license_plate(image_path)
print("Recognized License Plate Text:", recognized_text)

input("Please press enter to continue...")