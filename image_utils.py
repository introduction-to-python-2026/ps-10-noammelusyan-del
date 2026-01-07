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
import numpy as np
from PIL import Image
from scipy import signal

def load_image(image_path):
    """טעינת תמונה והמרתה למערך נומפי"""
    img = Image.open(image_path)
    return np.array(img)

def edge_detection(image_array):
    """זיהוי קצוות הכולל המרה לגרייסקייל וקונבולוציה"""
    
    # --- זה השינוי הקריטי שמונע את ה-AxisError ---
    if len(image_array.shape) == 3:
        # אם התמונה צבעונית (3 ערוצים), נחשב ממוצע
        grayscale = np.mean(image_array, axis=2)
    else:
        # אם התמונה כבר בשחור-לבן (ערוץ 1), נשתמש בה כמו שהיא
        grayscale = image_array
    # ----------------------------------------------

    # הגדרת הפילטרים (Kernels)
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
    
    # ביצוע הקונבולוציה (לפי ההוראות: zero padding וגודל זהה למקור)
    edgeX = signal.convolve2d(grayscale, kernelX, mode='same', boundary='fill', fillvalue=0)
    edgeY = signal.convolve2d(grayscale, kernelY, mode='same', boundary='fill', fillvalue=0)
    
    # חישוב עוצמת הקצוות (Magnitude)
    edgeMAG = np.sqrt(edgeX**2 + edgeY**2)
    
    return edgeMAG

    
    
   

