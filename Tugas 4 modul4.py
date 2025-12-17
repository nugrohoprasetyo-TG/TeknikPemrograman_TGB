# =========================================
# ANALISIS DATA MIKROSEISMIK
# =========================================

import pandas as pd
import numpy as np

# -----------------------------------------
# 1. Membaca & Inspeksi Data
# -----------------------------------------
file_path = "data_mikroseismik.csv"

data = pd.read_csv(file_path)

print("=== INFO DATA ===")
print(data.info())

print("\n=== DESKRIPSI DATA ===")
print(data.describe())

# -----------------------------------------
# 2. Data Cleaning
# -----------------------------------------

# Hapus data dengan magnitudo tidak wajar (<= 0)
data = data[data["Magnitudo"] > 0]

# Cek nilai NaN
print("\nJumlah data hilang per kolom:")
print(data.isna().sum())

# Hapus baris yang memiliki NaN
data = data.dropna()

# -----------------------------------------
# 3. Konversi Tipe Data Waktu
# -----------------------------------------
data["Waktu_UTC"] = pd.to_datetime(data["Waktu_UTC"])

# -----------------------------------------
# 4. Feature Engineering: Jarak Horizontal
# -----------------------------------------
# Titik pusat monitoring (0,0)
data["Jarak_Horizontal_m"] = np.sqrt(
    data["X_m"]**2 + data["Y_m"]**2
)

# -----------------------------------------
# 5. Analisis Statistik & Kriteria
# -----------------------------------------

# Magnitudo terbesar & terkecil
gempa_terbesar = data.loc[data["Magnitudo"].idxmax()]
gempa_terkecil = data.loc[data["Magnitudo"].idxmin()]

# Kedalaman rata-rata
kedalaman_rata2 = data["Z_m"].mean()

# Distribusi kedalaman
gempa_dangkal = data[data["Z_m"] > -1600]
gempa_dalam = data[data["Z_m"] <= -1600]

# Gempa dalam radius < 500 m
gempa_dekat = data[data["Jarak_Horizontal_m"] < 500]

# -----------------------------------------
# OUTPUT HASIL ANALISIS
# -----------------------------------------
print("\n=== HASIL ANALISIS ===")

print("\nGempa dengan Magnitudo Terbesar:")
print(gempa_terbesar)

print("\nGempa dengan Magnitudo Terkecil:")
print(gempa_terkecil)

print(f"\nKedalaman Rata-rata Gempa: {kedalaman_rata2:.2f} m")

print("\nDistribusi Kedalaman:")
print(f"Jumlah gempa dangkal (Z > -1600 m): {len(gempa_dangkal)}")
print(f"Jumlah gempa dalam   (Z <= -1600 m): {len(gempa_dalam)}")

print(f"\nJumlah gempa dalam radius < 500 m: {len(gempa_dekat)}")
