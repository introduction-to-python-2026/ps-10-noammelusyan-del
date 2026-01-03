from PIL import Image
import numpy as np
from scipy.signal import convolve2d

def load_image(path):
   import cv2
import numpy as np

def load_image(file_path):
    """
    קבלת נתיב לקובץ תמונה, קריאתו והמרתו למערך NumPy.
    """
    # קריאת התמונה. כברירת מחדל OpenCV קורא תמונות צבעוניות
    image = cv2.imread(file_path)

    # בדיקה אם התמונה נטענה בהצלחה (למניעת שגיאות אם הנתיב שגוי)
    if image is None:
        raise FileNotFoundError(f"לא ניתן למצוא או לקרוא את התמונה בנתיב: {file_path}")

    # המרת התמונה למערך NumPy (למרות ש-imread כבר מחזיר ndarray)
    image_array = np.array(image)

    return image_array

# --- Instructions for testing the function in Colab ---
# To test the function in Colab, you need to make the image accessible.
# Option 1: Upload the image directly to Colab.
#   1. Click on the folder icon on the left sidebar.
#   2. Click on the 'Upload to session storage' icon and upload your 'kyoto.jpeg' image.
#   3. Update the 'test_path' variable below to point to the uploaded file (e.g., '/content/kyoto.jpeg').
# Option 2: Use a publicly accessible image URL.
#   1. Download the image to Colab using `!wget` command in a new cell (e.g., `!wget -O /content/kyoto.jpeg <URL_TO_IMAGE>`).
#   2. Update the 'test_path' variable below to point to the downloaded file (e.g., '/content/kyoto.jpeg').

# Downloading a sample image for demonstration purposes
!wget -O /content/kyoto.jpeg https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Kinkaku-ji_2005-11-20.jpg/1200px-Kinkaku-ji_2005-11-20.jpg

# Placeholder path - please replace with your actual image path in Colab.
test_path = '/content/kyoto.jpeg'  # Example: if you uploaded it to /content/

try:
    # טעינת התמונה בעזרת הפונקציה
    img_data = load_image(test_path)

    # אימות התוצאה
    print("התמונה נטענה בהצלחה!")
    print(f"סוג האובייקט: {type(img_data)}")
    print(f"מימדי המערך (גובה, רוחב, ערוצי צבע): {img_data.shape}")

    # בדיקה אם מדובר במערך NumPy
    if isinstance(img_data, np.ndarray):
        print("אימות עבר: הפלט הוא אכן NumPy array.")

except Exception as e:
    print(f"שגיאה במהלך הבדיקה: {e}")

def edge_detection(image):
    import numpy as np
from scipy.signal import convolve2d

def edge_detection(image_array):
    # א. המרה לגרייסקייל (Grayscale) על ידי ממוצע של שלושת הערוצים
    # אנחנו מחשבים ממוצע לאורך ציר 2 (ערוצי הצבע)
    grayscale_img = np.mean(image_array, axis=2)

    # ב. יצירת קרנל לזיהוי שינויים אנכיים (Vertical)
    kernelY = np.array([
        [ 1,  2,  1],
        [ 0,  0,  0],
        [-1, -2, -1]
    ])

    # ג. יצירת קרנל לזיהוי שינויים אופקיים (Horizontal)
    kernelX = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ])

    # ד. החלת הקונבולוציה
    # mode='same' מבטיח שהפלט יהיה באותו גובה ורוחב (שימוש ב-Zero Padding)
    edgeX = convolve2d(grayscale_img, kernelX, mode='same')
    edgeY = convolve2d(grayscale_img, kernelY, mode='same')

    # ה. חישוב עוצמת הקצה (Magnitude)
    edgeMAG = np.sqrt(edgeX**2 + edgeY**2)

    return edgeMAG

import matplotlib.pyplot as plt

# 1. טעינת התמונה המקורית (השתמשי בנתיב שלך)
# The original test_path in the previous cell was for a local file, which Colab can't access.
# For testing in Colab, you need to either upload 'kyoto.jpeg' to '/content/'
# or download it from a URL. Let's use the placeholder path for Colab.
test_path = '/content/kyoto.jpeg'

# It's good practice to handle potential FileNotFoundError when loading images
try:
    original_image = load_image(test_path)
except FileNotFoundError as e:
    print(f"Error loading image: {e}")
    print("Please ensure 'kyoto.jpeg' is uploaded to /content/ or update test_path.")
    original_image = None # Set to None to prevent further errors if image not loaded

if original_image is not None:
    # 2. הפעלת פונקציית זיהוי הקצוות
    edges = edge_detection(original_image)

    # 3. הצגת התוצאות להשוואה
    plt.figure(figsize=(12, 6))

    # תמונה מקורית
    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    # OpenCV קורא ב-BGR, אז נהפוך ל-RGB לצורך התצוגה ב-Matplotlib
    plt.imshow(original_image[:, :, ::-1])
    plt.axis('off')

    # תמונת הקצוות
    plt.subplot(1, 2, 2)
    plt.title("Edge Detection (Sobel)")
    plt.imshow(edges, cmap='gray')
    plt.axis('off')

    plt.show()
