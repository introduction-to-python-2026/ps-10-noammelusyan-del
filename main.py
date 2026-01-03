import numpy as np
from image_utils import load_image, edge_detection  # ייבוא הפונקציות מהקובץ השני
from skimage.filters import median
from skimage.morphology import disk
from PIL import Image

def main():
    # 1. טעינת התמונה המקורית
    # ב-GitHub, ודאי שהתמונה נמצאת באותה תיקייה עם הקוד
    input_path = 'kyoto.jpeg' 
    
    try:
        original_img = load_image(input_path)
        print("Image loaded successfully.")
        
        # 2. הכנת התמונה (המרה לאפור לצורך סינון)
        gray_img = np.mean(original_img, axis=2).astype(np.uint8)
        
        # 3. ניקוי רעשים (Noise Suppression)
        clean_image = median(gray_img, disk(3))
        
        # 4. זיהוי קצוות (Edge Detection)
        # הפונקציה שלך מצפה ל-3 ערוצים, אז נשכפל את התמונה הנקייה
        clean_3channel = np.stack([clean_image]*3, axis=-1)
        edge_mag = edge_detection(clean_3channel)
        
        # 5. יצירת תמונה בינארית (Thresholding)
        threshold = 50 
        edge_binary = (edge_mag > threshold).astype(np.uint8) * 255
        
        # 6. שמירת התוצאה
        output_image = Image.fromarray(edge_binary)
        output_image.save('edge_detected_image.png')
        print("Edge detection completed. Result saved as edge_detected_image.png")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
