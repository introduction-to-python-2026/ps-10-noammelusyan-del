from skimage.filters import median
from skimage.morphology import disk
from PIL import Image

# נבדוק אם התמונה נטענה בהצלחה לפני שנמשיך
if original_image is not None:
    
    # 1. המרה לגרייסקייל (לצורך סינון הרעשים)
    gray_img = np.mean(original_image, axis=2).astype(np.uint8)
    
    # 2. סינון רעשים בעזרת מסנן חציוני (Median Filter)
    # disk(3) מגדיר את רדיוס הסינון
    clean_image = median(gray_img, disk(3))
    
    # 3. הרצת זיהוי קצוות על התמונה הנקייה
    # נהפוך את התמונה הנקייה חזרה ל-3 ערוצים כדי שפונקציית edge_detection תעבוד
    clean_3channel = np.stack([clean_image]*3, axis=-1)
    edge_mag = edge_detection(clean_3channel)
    
    # 4. יצירת תמונה בינארית (Thresholding)
    # נבחר סף (למשל 50). כל מה שמעל 50 יהיה לבן, כל מה שמתחת שחור
    threshold = 50 
    edge_binary = (edge_mag > threshold).astype(np.uint8) * 255
    
    # 5. הצגת התוצאה הסופית
    plt.figure(figsize=(6, 6))
    plt.title("Final Binary Edge Image")
    plt.imshow(edge_binary, cmap='gray')
    plt.axis('off')
    plt.show()
    
    # 6. שמירה לקובץ PNG
    final_image = Image.fromarray(edge_binary)
    final_image.save('kyoto_edges.png')
    print("התמונה נשמרה בהצלחה בשם kyoto_edges.png")
