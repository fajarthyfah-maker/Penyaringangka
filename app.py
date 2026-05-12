import streamlit as st
import re

# Judul Aplikasi
st.set_page_config(page_title="Penyaring Angka 4D", layout="centered")
st.title("🔢 Penyaring Angka 4 Digit")

# Area Input
input_teks = st.text_area("Masukkan angka (format bebas, contoh: 1028*1029):", height=200)

# Sidebar untuk Pengaturan Filter
st.sidebar.header("Pengaturan Filter")

# Filter 3D Belakang
filter_3d = st.sidebar.text_input("Hapus 3D Belakang (Contoh: 409)", help="Menghapus angka yang berakhiran 3 digit ini")

# Filter 2D Belakang
filter_2d = st.sidebar.text_input("Hapus 2D Belakang (Contoh: 28)", help="Menghapus angka yang berakhiran 2 digit ini")

# Opsi Potong Jadi 3D (Hapus angka depan)
potong_depan = st.sidebar.checkbox("Ubah semua angka menjadi 3 digit (Hapus angka depan)")

# Tombol Proses
if st.button("Proses Angka"):
    if input_teks:
        # 1. Ekstrak semua 4 digit angka menggunakan regex
        angka_list = re.findall(r'\b\d{4}\b', input_teks)
        total_awal = len(angka_list)
        
        # 2. Proses Filter 3D Belakang
        if filter_3d:
            angka_list = [n for n in angka_list if not n.endswith(filter_3d)]
            
        # 3. Proses Filter 2D Belakang
        if filter_2d:
            angka_list = [n for n in angka_list if not n.endswith(filter_2d)]
            
        # 4. Proses Potong Angka Depan (Jadi 3 Digit)
        if potong_depan:
            angka_list = [n[1:] for n in angka_list]
            
        # 5. Output dengan tanda bintang (*)
        hasil_akhir = "*".join(angka_list)
        
        # Tampilkan Hasil
        st.success(f"Berhasil memproses! Dari {total_awal} angka, tersisa {len(angka_list)} angka.")
        st.text_area("Hasil Output:", value=hasil_akhir, height=200)
        
        # Tombol Download
        st.download_button("Download Hasil (.txt)", hasil_akhir, file_name="hasil_saring.txt")
    else:
        st.warning("Silakan masukkan angka terlebih dahulu.")
