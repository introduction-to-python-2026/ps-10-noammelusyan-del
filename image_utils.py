import numpy as np
from scipy.signal import convolve2d
import cv2

def load_image(file_path):
    image = cv2.imread(file_path)
    if image is None:
        raise FileNotFoundError(f"לא ניתן למצוא או לקרוא את התמונה בנתיב: {file_path}")
    return np.array(image)

def edge_detection(image_array):
    grayscale_img = np.mean(image_array, axis=2)
    kernelY = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
    kernelX = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    edgeX = convolve2d(grayscale_img, kernelX, mode='same')
    edgeY = convolve2d(grayscale_img, kernelY, mode='same')
    edgeMAG = np.sqrt(edgeX**2 + edgeY**2)
    return edgeMAG
