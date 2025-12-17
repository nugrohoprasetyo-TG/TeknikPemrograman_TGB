import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("Peta Anomali Magnetik")

# ================================
# DATA CONTOH (SIMULASI GRID)
# ================================
np.random.seed(0)
nx, ny = 50, 50

anomali_observasi = np.random.normal(0, 50, (nx, ny))
anomali_regional = np.random.normal(0, 30, (nx, ny))
anomali_residual = anomali_observasi - anomali_regional

# ================================
# SIDEBAR - KONTROL
# ================================
st.sidebar.header("Pengaturan Visualisasi")

# 1. Pilihan Colormap
cmap = st.sidebar.selectbox(
    "Pilih Colormap",
    ["seismic", "jet", "viridis", "plasma", "inferno", "gray"]
)

# 2. Mode Skala
mode_skala = st.sidebar.radio(
    "Mode Skala",
    ["Auto", "Manual"]
)

# 3. Slider vmin & vmax
vmin = st.sidebar.slider(
    "Nilai Minimum (vmin)",
    float(anomali_observasi.min()),
    float(anomali_observasi.max()),
    float(anomali_observasi.min())
)

vmax = st.sidebar.slider(
    "Nilai Maksimum (vmax)",
    float(anomali_observasi.min()),
    float(anomali_observasi.max()),
    float(anomali_observasi.max())
)

# 4. Opsi Tambahan
simpan_gambar = st.sidebar.checkbox("Simpan Plot sebagai Gambar")

# ================================
# FUNGSI PLOTTING
# ================================
def plot_peta(data, judul, filename=None):
    fig, ax = plt.subplots(figsize=(5, 4))

    if mode_skala == "Auto":
        im = ax.imshow(data, cmap=cmap)
    else:
        im = ax.imshow(data, cmap=cmap, vmin=vmin, vmax=vmax)

    ax.set_title(judul)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    plt.colorbar(im, ax=ax, label="Anomali (nT)")
    st.pyplot(fig)

    if simpan_gambar and filename:
        fig.savefig(filename, dpi=300)

# ================================
# TAMPILKAN PETA
# ================================
col1, col2, col3 = st.columns(3)

with col1:
    plot_peta(anomali_observasi, "Anomali Magnetik Observasi", "anomali_observasi.png")

with col2:
    plot_peta(anomali_regional, "Anomali Magnetik Regional", "anomali_regional.png")

with col3:
    plot_peta(anomali_residual, "Anomali Magnetik Residual", "anomali_residual.png")

if simpan_gambar:
    st.success("Semua peta berhasil disimpan sebagai file gambar.")
