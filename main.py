import numpy as np
from image_utils import load_image, edge_detection
from skimage.filters import median
from skimage.morphology import disk
from PIL import Image

def main():
    input_path = 'kyoto.jpeg' # ודאי שהקובץ ב-GitHub נקרא בדיוק ככה
    try:
        original_img = load_image(input_path)
        print("Image loaded successfully.")
        
        gray_img = np.mean(original_img, axis=2).astype(np.uint8)
        clean_image = median(gray_img, disk(3))
        
        clean_3channel = np.stack([clean_image]*3, axis=-1)
        edge_mag = edge_detection(clean_3channel)
        
        threshold = 50 
        edge_binary = (edge_mag > threshold).astype(np.uint8) * 255
        
        output_image = Image.fromarray(edge_binary)
        output_image.save('edge_detected_image.png')
        print("Edge detection completed. Result saved as edge_detected_image.png")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
