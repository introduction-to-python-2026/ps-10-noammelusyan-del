from PIL import Image
import numpy as np
from scipy.signal import convolve2d
import cv2

def load_image(file_path):
    """
    קבלת נתיב לקובץ תמונה, קריאתו והמרתו למערך NumPy.
    """
    image = cv2.imread(file_path)
    
    # בדיקה אם התמונה נטענה בהצלחה
    if image is None:
        raise FileNotFoundError(f"לא ניתן למצוא או לקרוא את התמונה בנתיב: {file_path}")
    
    # המרה למערך NumPy
    image_array = np.array(image)
    
    return image_array

def edge_detection(image_array):
    """
    ביצוע זיהוי קצוות על מערך תמונה (מבוסס אופרטור סובל).
    """
    # 1. המרה לגרייסקייל על ידי ממוצע הערוצים
    grayscale_img = np.mean(image_array, axis=2)

    # 2. יצירת קרנלים לזיהוי שינויים אנכיים ואופקיים
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

    # 3. החלת קונבולוציה (עם Zero Padding בעזרת mode='same')
    edgeX = convolve2d(grayscale_img, kernelX, mode='same')
    edgeY = convolve2d(grayscale_img, kernelY, mode='same')

    # 4. חישוב עוצמת הקצה (Magnitude)
    edgeMAG = np.sqrt(edgeX**2 + edgeY**2)

    return edgeMAG
