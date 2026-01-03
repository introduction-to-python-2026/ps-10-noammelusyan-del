import cv2
import numpy as np
from scipy.signal import convolve2d

def load_image(file_path):
    """קריאת תמונה והמרתה למערך NumPy"""
    image = cv2.imread(file_path)
    if image is None:
        raise FileNotFoundError(f"לא ניתן למצוא את הקובץ בנתיב: {file_path}")
    return np.array(image)

def edge_detection(image_array):
    """ביצוע זיהוי קצוות בשיטת סובל"""
    # המרה לגרייסקייל
    grayscale_img = np.mean(image_array, axis=2)

    # הגדרת קרנלים (Kernels)
    kernelY = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
    kernelX = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

    # קונבולוציה
    edgeX = convolve2d(grayscale_img, kernelX, mode='same')
    edgeY = convolve2d(grayscale_img, kernelY, mode='same')

    # חישוב עוצמת הקצה
    edgeMAG = np.sqrt(edgeX**2 + edgeY**2)
    return edgeMAG

import numpy as np
from image_utils import load_image, edge_detection
from skimage.filters import median
from skimage.morphology import disk
from PIL import Image

def main():
    # 1. טעינת התמונה המקורית
    input_path = 'original_image.jpg' # ודאי שהשם תואם לקובץ שהעלית ל-GitHub
    original_img = load_image(input_path)
    
    # 2. המרה לאפור לצורך סינון רעשים
    gray_img = np.mean(original_img, axis=2).astype(np.uint8)
    
    # 3. דיכוי רעשים (Noise Suppression)
    clean_image = median(gray_img, disk(3))
    
    # 4. זיהוי קצוות (Edge Detection)
    # נמיר חזרה ל-3 ערוצים כדי להתאים לפונקציה המקורית
    clean_3channel = np.stack([clean_image]*3, axis=-1)
    edge_mag = edge_detection(clean_3channel)
    
    # 5. הפיכה לתמונה בינארית (Thresholding)
    threshold = 50 # ניתן לשנות לפי הצורך
    edge_binary = (edge_mag > threshold) * 255
    edge_binary = edge_binary.astype(np.uint8)
    
    # 6. שמירת התמונה התוצאתית
    output_image = Image.fromarray(edge_binary)
    output_image.save('edge_detected_image.png')
    print("תהליך הסתיים בהצלחה. התמונה נשמרה בשם edge_detected_image.png")

if __name__ == "__main__":
    main()
