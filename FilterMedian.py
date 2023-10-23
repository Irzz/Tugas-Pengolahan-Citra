import numpy as np
import cv2

def median_filter(img, kernel_size):
    height, width = img.shape

    # Setengah dari nilai kernel_size
    offset = kernel_size // 2

    # Membuat matriks kosong sebagai wadah
    filtered_img = np.zeros_like(img)

    for y in range(offset, height - offset):
        for x in range(offset, width - offset):
            # Mencari nilai disekitar pixel
            window = img[y - offset:y + offset + 1, x - offset:x + offset + 1]
            # Menghitung nilai median
            median_value = np.median(window)
            filtered_img[y, x] = median_value

    # Mengembalikan fungsi median_filter
    return filtered_img

if __name__ == "__main__":
    # Path dari gambar
    img_path = "Image/boneka2.jpg"

    # Mengubah gambar menjadi grayscale
    original_img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    # Mendefinisikan tipe kernel
    kernel_size = 3

    # Mengaplikasikan fungsi median_filter kepada gambar
    filtered_img = median_filter(original_img, kernel_size)

    # Tampilkan gambar asli dan hasil filter median
    cv2.imshow("Original Image", original_img)
    cv2.imshow("Median Filtered Image", filtered_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
