import cv2
from pyzbar.pyzbar import decode

def read_barcodes_from_image(image_path):
    try:
        image = cv2.imread(image_path)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        decoded_objects = decode(gray_image)

        for obj in decoded_objects:
            barcode_data = obj.data.decode('utf-8')
            barcode_type = obj.type
            print(f"Barcode Type: {barcode_type}, Data: {barcode_data}")
        
        if not decoded_objects:
            print("No barcodes found in the image.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    image_path = "path/to/your/image.jpg"  # Replace with the actual path of your image
    read_barcodes_from_image(image_path)
