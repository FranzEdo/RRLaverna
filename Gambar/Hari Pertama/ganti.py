import os

# Ganti dengan path folder Anda
folder_path = r'D:\WEB LAVERNA\Gambar\Hari Pertama'

# Mengambil semua file gambar
files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.png'))]

for count, file in enumerate(files, start=1):
    old_file = os.path.join(folder_path, file)
    new_file = os.path.join(folder_path, f'image_{count}.jpg')  # Ubah ekstensi sesuai kebutuhan
    os.rename(old_file, new_file)