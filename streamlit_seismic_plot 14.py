import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Visualisasi Seismik - Pertemuan 14")

# -----------------------------
# Data dummy (contoh)
# -----------------------------
data = np.random.randn(100, 100)

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.header("Pengaturan Plot")

# 1. Pilihan colormap
cmap_option = st.sidebar.selectbox(
    "Pilih Colormap",
    ["seismic", "viridis", "jet", "coolwarm", "plasma"]
)

# 2. Mode skala
scale_mode = st.sidebar.radio(
    "Mode Skala",
    ["Auto", "Manual"]
)

# 3. vmin & vmax (dipakai kalau Manual)
vmin = st.sidebar.slider("vmin", -5.0, 5.0, -2.0)
vmax = st.sidebar.slider("vmax", -5.0, 5.0, 2.0)

# -----------------------------
# PLOT
# -----------------------------
fig, ax = plt.subplots()

if scale_mode == "Auto":
    im = ax.imshow(data, cmap=cmap_option)
else:
    im = ax.imshow(data, cmap=cmap_option, vmin=vmin, vmax=vmax)

plt.colorbar(im, ax=ax)
ax.set_title("Peta Anomali Seismik")

st.pyplot(fig)

# -----------------------------
# OPSI TAMBAHAN (SIMPAN GAMBAR)
# -----------------------------
if st.sidebar.button("Simpan Gambar"):
    plt.savefig("plot_pertemuan_14.png", dpi=300)
    st.success("Gambar berhasil disimpan!")
