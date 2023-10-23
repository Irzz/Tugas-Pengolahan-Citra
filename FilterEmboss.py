import numpy as np
import cv2

def filter_emboss(image):
    # Penggunaan kernel #3
    kernel = np.array([[-2, -1, 0],
                       [-1,  1, 1],
                       [ 0,  1, 2]])
    
    height, width = image.shape
    filtered_image = np.zeros_like(image)
    
    # Perulangan untuk melakukan konvolusi
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            subimage = image[y-1:y+2, x-1:x+2]
            pixel_value = np.sum(kernel * subimage)
            filtered_image[y, x] = np.clip(pixel_value, 0, 255)
    
    # Mengembalikan fungsi filter_emboss
    return filtered_image

if __name__ == "__main__":
    # Path dari gambar
    img_path = "Image/sidikjari.png" 

    # Mengubah gambar menjadi grayscale
    original_image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    # Mengaplikasikan fungsi filter_emboss kepada gambar
    filtered_image = filter_emboss(original_image)

    # Menampilkan original_image dan filtered_image
    cv2.imshow("Original Image", original_image)
    cv2.imshow("Emboss Filtered Image", filtered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
