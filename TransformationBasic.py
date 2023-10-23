from PIL import Image
import math

def rotate_image(image, angle):
    # mendapatkan ukuran gambar
    width, height = image.size

    # menghitung sudut rotasi dalam radian
    rad = math.radians(angle)

    #menghitung panjang diagonal gambar
    diagonal = math.ceil(math.sqrt(width ** 2 + height ** 2))

    # menghitung posisi tengah gambar
    cx = width // 2
    cy = height // 2

    # membuat matriks kosong sebagai penampung gambar
    rotated_image = Image.new('RGB', (diagonal, diagonal))

    # logika untuk memutar gambar
    for x in range(width):
        for y in range(height):
            # menghitung posisi pixel pada gambar yang sudah diputar
            a = math.cos(rad) * (x - cx) - math.sin(rad) * (y - cy) + diagonal // 2
            b = math.sin(rad) * (x - cx) + math.cos(rad) * (y - cy) + diagonal // 2

            # memeriksa posisi pixel apakah sudah berada pada gambar yang telah diputar
            if 0 <= a < diagonal and 0 <= b < diagonal:
                pixel = image.getpixel((x, y))
                rotated_image.putpixel((int(a), int(b)), pixel)

    # mengembalikan proses dalam fungsi pada variabel
    return rotated_image

def mirror_image(image):
    # mendapatkan ukuran gambar
    width, height = image.size
    
    # membuat matriks kosong sebagai penampung gambar
    mirrored_image = Image.new(image.mode, image.size)
    
    # logika untuk pencerminan gambar
    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            mirrored_image.putpixel((width - 1 - x, y), pixel)
    
    # mengembalikan proses dalam fungsi pada variabel
    return mirrored_image

def shift_image(image, dx, dy):
    # mendapatkan ukuran gambar
    width, height = image.size

    # membuat matriks kosong sebagai penampung gambar
    shifted_image = Image.new(image.mode, (width, height))

    # logika untuk pergeseran gambar
    for x in range(width):
        for y in range(height):
            if 0 <= x + dx < width and 0 <= y + dy < height:
                pixel = image.getpixel((x + dx, y + dy))
                shifted_image.putpixel((x, y), pixel)

    # mengembalikan proses dalam fungsi pada variabel
    return shifted_image

# memasukkan path dari gambar
img_path = 'Image\R.jpg'

# membukan gambar dari path
image = Image.open(img_path)
image = image.resize((700, 500))

# menampilkan original image
image.show()

# memutar gambar dan menampilkannya
rotated_image = rotate_image(image, 75)
rotated_image.show()

# menjalankan fungsi pencerminan gambar dan menampilkannya
mirrored_image = mirror_image(image)
mirrored_image.show()

# menjalankan fungsi pergeseran gambar
shifted_image = shift_image(image, -350, -250)
shifted_image.show()