from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk

# Fungsi untuk merotasi gambar
def rotate_image(angle):
    global image, rotated_image
    rotated_image = image.rotate(angle)
    display_image(rotated_image)

# Fungsi untuk mencerminkan gambar secara horizontal
def mirror_horizontal():
    global image, mirrored_image
    mirrored_image = image.transpose(Image.FLIP_LEFT_RIGHT)
    display_image(mirrored_image)

# Fungsi untuk mencerminkan gambar secara vertikal
def mirror_vertical():
    global image, mirrored_image
    mirrored_image = image.transpose(Image.FLIP_TOP_BOTTOM)
    display_image(mirrored_image)

# Fungsi untuk menggeser gambar
def shift_image(event):
    global image, shifted_image, dx, dy
    dx = int(dx_slider.get())
    dy = int(dy_slider.get())
    shifted_image = image.copy()
    shifted_image = shifted_image.transform(shifted_image.size, Image.AFFINE, (1, 0, dx, 0, 1, dy))
    display_image(shifted_image)

# Fungsi untuk mengatur ulang gambar dan slider ke posisi semula
def reset_image():
    global image, dx, dy
    dx = 0
    dy = 0
    dx_slider.set(0)
    dy_slider.set(0)
    rotate_slider.set(0)
    display_image(image)

# Fungsi untuk menampilkan gambar
def display_image(img):
    img = img.resize((400, 400))
    img_tk = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
    canvas.image = img_tk

# Fungsi untuk mengupload gambar
def upload_image():
    global image, rotated_image, mirrored_image, shifted_image
    filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")])
    if filepath:
        try:
            image = Image.open(filepath)
            image = image.resize((400, 400))
            rotated_image = image.copy()
            mirrored_image = image.copy()
            shifted_image = image.copy()
            display_image(image)
        except:
            messagebox.showerror("Error", "Failed to open the image.")

# Membuat GUI
root = tk.Tk()
root.title("Image Transformations")
root.geometry("600x800")

# Membuat canvas untuk menampilkan gambar
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Tombol untuk mengupload gambar
upload_button = ttk.Button(root, text="Upload Image", command=upload_image)
upload_button.pack(pady=10)

# Slider untuk pergeseran gambar
dx_slider = ttk.Scale(root, from_=-400, to=400, length=300, command=shift_image)
dx_slider.pack()
dx_label = ttk.Label(root, text="Shift X")
dx_label.pack()
dy_slider = ttk.Scale(root, from_=-400, to=400, length=300, command=shift_image)
dy_slider.pack()
dy_label = ttk.Label(root, text="Shift Y")
dy_label.pack()

# Slider untuk merotasi gambar
rotate_slider = ttk.Scale(root, from_=-0, to=360, length=300, command=lambda angle: rotate_image(float(angle)))
rotate_slider.pack()
rotate_label = ttk.Label(root, text="Rotate")
rotate_label.pack()

# Tombol untuk mencerminkan gambar secara horizontal
mirror_horizontal_button = ttk.Button(root, text="Mirror Horizontal", command=mirror_horizontal)
mirror_horizontal_button.pack(pady=5)

# Tombol untuk mencerminkan gambar secara vertikal
mirror_vertical_button = ttk.Button(root, text="Mirror Vertical", command=mirror_vertical)
mirror_vertical_button.pack(pady=5)

# Tombol reset
reset_button = ttk.Button(root, text="Reset", command=reset_image)
reset_button.pack(pady=10)

# Menjalankan GUI
root.mainloop()
