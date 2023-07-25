import cv2
import pytesseract

image = cv2.imread("./pictures/test2.jpg")
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Perform OCR on the entire image
custom_config = r'--oem 3 --psm 6 outputbase digits'  # Specify OCR options (psm 6 for treating the image as a single block of text with uniform font size)
numbers_detected = pytesseract.image_to_string(image, config=custom_config)

print(numbers_detected)

