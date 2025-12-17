import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("Visualisasi Data Seismik")

# ================================
# DATA CONTOH (SIMULASI)
# ================================
np.random.seed(42)
n_trace = 50
n_time = 200
data_seismik = np.random.normal(0, 1, (n_trace, n_time))

# ================================
# SIDEBAR - KONTROL
# ================================
st.sidebar.header("Pengaturan Plot")

# 1. Pilihan Colormap
cmap = st.sidebar.selectbox(
    "Pilih Colormap",
    ["seismic", "gray", "viridis", "plasma", "inferno"]
)

# 2. Mode Skala
mode_skala = st.sidebar.radio(
    "Mode Skala Amplitudo",
    ["Auto", "Manual"]
)

# 3. Slider vmin & vmax (Manual)
vmin = st.sidebar.slider(
    "vmin", float(data_seismik.min()), float(data_seismik.max()), -1.0
)
vmax = st.sidebar.slider(
    "vmax", float(data_seismik.min()), float(data_seismik.max()), 1.0
)

# 4. Opsi Tambahan
invert_time = st.sidebar.checkbox("Balik Sumbu Waktu")
trace_min, trace_max = st.sidebar.slider(
    "Pilih Rentang Trace",
    0, n_trace - 1, (0, n_trace - 1)
)

save_plot = st.sidebar.checkbox("Simpan Plot sebagai Gambar")

# ================================
# PEMILIHAN DATA
# ================================
data_plot = data_seismik[trace_min:trace_max + 1, :]

# ================================
# PLOTTING
# ================================
fig, ax = plt.subplots(figsize=(10, 6))

if mode_skala == "Auto":
    im = ax.imshow(
        data_plot.T,
        aspect="auto",
        cmap=cmap
    )
else:
    im = ax.imshow(
        data_plot.T,
        aspect="auto",
        cmap=cmap,
        vmin=vmin,
        vmax=vmax
    )

# Balik sumbu waktu jika dipilih
if invert_time:
    ax.invert_yaxis()

ax.set_xlabel("Trace")
ax.set_ylabel("Waktu")
ax.set_title("Penampang Seismik")

plt.colorbar(im, ax=ax, label="Amplitudo")

st.pyplot(fig)

# ================================
# SIMPAN GAMBAR
# ================================
if save_plot:
    fig.savefig("plot_seismik.png", dpi=300)
    st.success("Plot berhasil disimpan sebagai plot_seismik.png")
