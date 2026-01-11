import numpy as np
from PIL import Image
from scipy import signal

def load_image(image_path):
    """טעינת תמונה והמרתה למערך נומפי"""
    img = Image.open(image_path)
    return np.array(img)

def edge_detection(image_array):
    """זיהוי קצוות הכולל המרה לגרייסקייל וקונבולוציה"""
    
    # המרה לגרייסקייל אם התמונה צבעונית
    if len(image_array.shape) == 3:
        grayscale = np.mean(image_array, axis=2)
    else:
        grayscale = image_array

    # הגדרת הפילטרים (Sobel Kernels)
    kernelY = np.array([
        [ 1,  2,  1],
        [ 0,  0,  0],
        [-1, -2, -1]
    ])
    
    kernelX = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ])
    
    # ביצוע הקונבולוציה
    edgeX = signal.convolve2d(grayscale, kernelX, mode='same', boundary='fill', fillvalue=0)
    edgeY = signal.convolve2d(grayscale, kernelY, mode='same', boundary='fill', fillvalue=0)
    
    # חישוב עוצמת הקצוות (Magnitude)
    edgeMAG = np.sqrt(edgeX**2 + edgeY**2)
    
    return edgeMAG
    
    
   

