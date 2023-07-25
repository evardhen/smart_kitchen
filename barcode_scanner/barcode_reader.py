from pyzbar import pyzbar
import cv2
import numpy as np

def preprocess_image(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)

    # Binarization: Convert the grayscale image to a binary image
    _, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY_INV)

    # Adaptive Thresholding: Apply adaptive thresholding to improve contrast
    adaptive_threshold_image = cv2.adaptiveThreshold(
        gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV, blockSize=11, C=2
    )

    # Find the angle of rotation using Hough Line Transform
    lines = cv2.HoughLines(adaptive_threshold_image, 1, np.pi / 180, 100)
    if lines is not None:
        for line in lines:
            rho, theta = line[0]
            angle = theta * 180 / np.pi
            if angle > 45:
                angle -= 90

        # Rotate the image to correct the orientation
        rows, cols = gray_image.shape
        rotation_matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
        rotated_image = cv2.warpAffine(gray_image, rotation_matrix, (cols, rows))
    else:
        # If no lines were detected, use the original grayscale image
        rotated_image = gray_image

    return rotated_image


def decode(image):
    # decodes all barcodes from an image
    detectedBarcodes = pyzbar.decode(image)
    if not detectedBarcodes:
        print("Barcode Not Detected or your barcode is blank/corrupted!")
    for obj in detectedBarcodes:
        # print barcode type & data
        print("Type:", obj.type)
        print("Data:", obj.data, "\n")


if __name__ == "__main__":
    barcode_path = "./pictures/test4.jpg"

    # load the image
    img = cv2.imread(barcode_path)
    # processed_image = preprocess_image(img)

    # decode detected barcodes & get the image
    decode(img)