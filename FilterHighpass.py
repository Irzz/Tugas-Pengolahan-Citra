import numpy as np
import cv2

def highpass_filter(image, kernel):
    kernel = np.ones((kernel_size, kernel_size), dtype=np.float32) * -1
    center = kernel_size // 2
    kernel[center, center] = kernel_size * kernel_size - 1

    # Memanjangkan ukuran gambar
    image_padded = np.pad(image, (kernel.shape[0]//2, kernel.shape[1]//2), mode='constant')

    # Membuat matriks kosong sebagai wadah
    filtered_image = np.zeros_like(image, dtype=np.float32)

    # Perulangan untuk melakukan konvolusi
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            # Mencari bagian gambar yang sesuai dengan kernel
            region = image_padded[y:y+kernel.shape[0], x:x+kernel.shape[1]]
            result = np.sum(region * kernel)
            filtered_image[y, x] = result

    # Mengembalikan fungsi highpass_filter
    return filtered_image

# Path dari gambar
img_path = 'Image/boneka.jpg'

# Mengubah gambar menjadi grayscale
original_image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

# Mendefinisikan tipe kernel
kernel_size = 2

# Mengaplikasikan fungsi kepada gambar
filtered_image = highpass_filter(original_image, kernel_size)

# Mengkonversi hasil agar dapat ditampilkan opencv
filtered_image_display = cv2.normalize(filtered_image, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

# Menampilkan original_image dan filtered_image
cv2.imshow('Original image', original_image)
cv2.imshow('High-Pass Filter Result', filtered_image_display)
cv2.waitKey(0)
cv2.destroyAllWindows()
