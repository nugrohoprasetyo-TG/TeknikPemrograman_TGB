import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# Data seismik dummy
# -------------------------------
np.random.seed(0)
data = np.random.randn(200, 100)  # (time, trace)

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.title("Pengaturan Plot")

# 1. Pilihan colormap
cmap = st.sidebar.selectbox(
    "Pilih Colormap",
    ["gray", "seismic", "viridis", "plasma", "inferno"]
)

# 2. Mode scaling
scale_mode = st.sidebar.radio(
    "Mode Scaling",
    ["Auto", "Manual"]
)

# 3. Slider vmin & vmax (hanya aktif jika Manual)
if scale_mode == "Manual":
    vmin = st.sidebar.slider("vmin", float(data.min()), float(data.max()), float(data.min()))
    vmax = st.sidebar.slider("vmax", float(data.min()), float(data.max()), float(data.max()))
else:
    vmin = None
    vmax = None

# 4. Opsi tambahan: simpan gambar
save_plot = st.sidebar.checkbox("Simpan plot sebagai gambar")

# -------------------------------
# Plot Seismik
# -------------------------------
st.title("Interactive Seismic Plot")

fig, ax = plt.subplots(figsize=(8, 5))

if scale_mode == "Auto":
    im = ax.imshow(data, cmap=cmap, aspect="auto")
else:
    im = ax.imshow(data, cmap=cmap, aspect="auto", vmin=vmin, vmax=vmax)

ax.set_xlabel("Trace")
ax.set_ylabel("Time")
ax.set_title("Seismic Section")

plt.colorbar(im, ax=ax, label="Amplitude")

st.pyplot(fig)

# -------------------------------
# Simpan gambar
# -------------------------------
if save_plot:
    fig.savefig("seismic_plot.png", dpi=300)
    st.success("Plot berhasil disimpan sebagai seismic_plot.png")