import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy import signal
from skimage.filters import median
from skimage.morphology import ball # נשארים עם ball לפי ההוראות

# 1. הגדרת פונקציות
def load_image(p): 
    return np.array(Image.open(p))

def edge_detection(img_arr):
    if len(img_arr.shape) == 3:
        gray = np.mean(img_arr, axis=2)
    else:
        gray = img_arr
    ky = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
    kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    ex = signal.convolve2d(gray, kx, mode='same', boundary='fill', fillvalue=0)
    ey = signal.convolve2d(gray, ky, mode='same', boundary='fill', fillvalue=0)
    return np.sqrt(ex**2 + ey**2)

# 2. הרצה
filename = 'kyoto.jpeg'
img = load_image(filename)

# המרה לגרייסקייל
gray = np.mean(img, axis=2).astype(np.uint8)

# התיקון כאן: 
# השגיאה קרתה כי ball(3) הוא תלת-מימדי. 
# אנחנו לוקחים רק שכבה אחת ממנו [1] כדי שיהיה דו-מימדי ויתאים לתמונה.
clean = median(gray, ball(3)[1]) 

mag = edge_detection(clean)

# יצירת התמונה הבינארית
threshold = 30
binary = (mag > threshold).astype(np.uint8) * 255

# 3. הצגת התוצאה
plt.figure(figsize=(10, 5))
plt.imshow(binary, cmap='gray')
plt.axis('off')
plt.show()

# 4. שמירה
Image.fromarray(binary).save('my_edges.png')
print("✅ הסתיים בהצלחה! התמונה נוצרה.")
