import numpy as np
from PIL import Image

def load_image(image_path):
    # קריאת התמונה הצבעונית
    img = Image.open(image_path)

    # המרה למערך NumPy
    image_array = np.array(img)

    # החזרת המערך
    return image_array

    # 1. כאן את מכניסה את הנתיב לתמונה שלך:
# my_path = r'C:\Users\user\Documents\רפואה בישראל\לימודים שנה א\פייתון\kyoto.jpeg'
# To fix the FileNotFoundError, you need to upload the image to your Colab environment.
# For example, if you upload 'kyoto.jpeg' to the /content/ directory, use the path below.
# You can upload files using the file browser on the left sidebar or with `from google.colab import files; uploaded = files.upload()`.
my_path = '/content/kyoto.jpeg'

# קריאה לפונקציה
image_result = load_image(my_path)

# הדפסת התוצאה
print("Type of result:", type(image_result))
print("Array shape:", image_result.shape)
def load_image(image_path):
    # קריאת התמונה הצבעונית
    img = Image.open(image_path)
    
    # הצגת התמונה בחלון חדש (או בתוך הקולאב) כדי לוודא שהיא נטענה
    img.show() 
    
    # המרה למערך NumPy
    image_array = np.array(img)
    
    return image_array

# 1. הנתיב שלך (זכרי להעלות את הקובץ לסרגל הצד אם את בקולאב)
my_path = 'kyoto.jpeg' 

import numpy as np                 # לחישובים מתמטיים ומערכים
from PIL import Image              # לטעינה ופתיחה של תמונות
from scipy import signal           # בשביל פונקציית הקונבולוציה (convolve2d)
import matplotlib.pyplot as plt    # (אופציונלי) כדי להציג את התמונות על המסך

def edge_detection(image_array):
    # א. המרה לגרייסקייל על ידי ממוצע של שלושת ערוצי הצבע
    # אנחנו מחשבים ממוצע על ציר 2 (ערוצי הצבע)
    grayscale = np.mean(image_array, axis=2)
    
    # ב. יצירת קרנל (פילטר) לזיהוי שינויים אנכיים - kernelY
    kernelY = np.array([
        [ 1,  2,  1],
        [ 0,  0,  0],
        [-1, -2, -1]
    ])
    
    # ג. יצירת קרנל (פילטר) לזיהוי שינויים אופקיים - kernelX
    kernelX = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ])
    
    # ד. הרצת הקונבולוציה (Apply filters)
    # mode='same' מבטיח שהתוצאה תהיה באותו גודל של התמונה המקורית
    # boundary='fill', fillvalue=0 מבצע zero padding
    edgeX = signal.convolve2d(grayscale, kernelX, mode='same', boundary='fill', fillvalue=0)
    edgeY = signal.convolve2d(grayscale, kernelY, mode='same', boundary='fill', fillvalue=0)
    
    # ה. חישוב עוצמת הקצוות (Magnitude) לפי הנוסחה
    edgeMAG = np.sqrt(edgeX**2 + edgeY**2)
    
    # ו. החזרת המערך המייצג את הקצוות
    return edgeMAG
    import matplotlib.pyplot as plt

# 1. הרצת פונקציית זיהוי הקצוות על המערך שקיבלנו מהשלב הקודם
edge_result = edge_detection(image_result)

# 2. אימות נתונים
print("Edge detection finished!")
print(f"Result shape: {edge_result.shape}") # צריך להיות זהה לגובה ולרוחב המקורי

# 3. תצוגה ויזואלית של התוצאה
plt.figure(figsize=(10, 5))

# הצגת המקור
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image_result)
plt.axis('off')

# הצגת הקצוות (משתמשים במפת צבעים אפורה)
plt.subplot(1, 2, 2)
plt.title("Edge Detection (Sobel)")
plt.imshow(edge_result, cmap='gray')
plt.axis('off')

plt.show()
