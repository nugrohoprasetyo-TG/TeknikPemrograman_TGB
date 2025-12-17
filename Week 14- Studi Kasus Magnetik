import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from scipy.interpolate import griddata, NearestNDInterpolator
from scipy.ndimage import uniform_filter

# ==============================
# FUNGSI TREND SURFACE 2D
# ==============================
def polyfit2d(x, y, z, order=1):
    x = x.flatten()
    y = y.flatten()
    z = z.flatten()

    mask = ~np.isnan(z)
    x, y, z = x[mask], y[mask], z[mask]

    G = np.ones((x.size, 1))
    for i in range(1, order + 1):
        for j in range(i + 1):
            G = np.column_stack((G, (x**(i-j)) * (y**j)))

    m, _, _, _ = np.linalg.lstsq(G, z, rcond=None)

    def poly(xi, yi):
        out = m[0]
        idx = 1
        for i in range(1, order + 1):
            for j in range(i + 1):
                out += m[idx] * (xi**(i-j)) * (yi**j)
                idx += 1
        return out

    return poly

# ==============================
# STREAMLIT APP
# ==============================
st.set_page_config(layout="wide")
st.title("Aplikasi Analisis Anomali Magnetik")

# ==============================
# INPUT DATA
# ==============================
uploaded_file = st.file_uploader("Upload file CSV", type="csv")

if uploaded_file is None:
    st.stop()

df_input = pd.read_csv(uploaded_file)

# ==============================
# SIDEBAR - PARAMETER GRID
# ==============================
st.sidebar.header("Parameter Gridding")

x_min, x_max = df_input['x'].min(), df_input['x'].max()
y_min, y_max = df_input['y'].min(), df_input['y'].max()

default_cell = (x_max - x_min) / 50

cell_size = st.sidebar.number_input(
    "Ukuran Sel (meter)",
    min_value=1.0,
    max_value=(x_max - x_min)/5,
    value=float(default_cell),
    step=5.0
)

interp_method = st.sidebar.selectbox(
    "Metode Interpolasi",
    ["linear", "cubic", "nearest"]
)

# ==============================
# SIDEBAR - VISUALISASI
# ==============================
st.sidebar.markdown("---")
st.sidebar.header("Visualisasi")

cmap_option = st.sidebar.selectbox(
    "Colormap",
    ["jet", "viridis", "seismic", "plasma", "inferno", "coolwarm"]
)

scale_mode = st.sidebar.radio(
    "Mode Skala",
    ["Auto Scale", "Manual Scale"],
    horizontal=True
)

if scale_mode == "Manual Scale":
    vmin = st.sidebar.slider("vmin", -500.0, 500.0, -100.0, step=10.0)
    vmax = st.sidebar.slider("vmax", -500.0, 500.0, 100.0, step=10.0)
else:
    vmin, vmax = None, None

# ==============================
# PROSES GRIDDING
# ==============================
xi = np.arange(x_min, x_max + cell_size, cell_size)
yi = np.arange(y_min, y_max + cell_size, cell_size)
X, Y = np.meshgrid(xi, yi)

with st.spinner("Interpolasi data..."):
    T_obs = griddata(
        (df_input['x'], df_input['y']),
        df_input['t_obs'],
        (X, Y),
        method=interp_method
    )

st.sidebar.success(f"Grid: {T_obs.shape[1]} x {T_obs.shape[0]}")

# ==============================
# VISUALISASI DATA
# ==============================
st.subheader("1. Visualisasi Data")

tab1, tab2 = st.tabs(["Peta Kontur", "Scatter Data"])

with tab1:
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    c1 = ax1.contourf(X, Y, T_obs, levels=25, cmap=cmap_option, vmin=vmin, vmax=vmax)
    ax1.scatter(df_input['x'], df_input['y'], c='k', s=5, alpha=0.3)
    ax1.set_aspect('equal')
    fig1.colorbar(c1, ax=ax1, label="nT")
    st.pyplot(fig1)

with tab2:
    fig2, ax2 = plt.subplots(figsize=(8, 6))
    sc = ax2.scatter(
        df_input['x'], df_input['y'],
        c=df_input['t_obs'],
        cmap=cmap_option,
        vmin=vmin, vmax=vmax,
        s=10
    )
    fig2.colorbar(sc, ax=ax2, label="nT")
    st.pyplot(fig2)

# ==============================
# REGIONAL - RESIDUAL
# ==============================
st.subheader("2. Pemisahan Regional & Residual")

mask_nan = np.isnan(T_obs)
if np.any(mask_nan):
    interp_nn = NearestNDInterpolator(
        list(zip(X[~mask_nan], Y[~mask_nan])),
        T_obs[~mask_nan]
    )
    T_filled = interp_nn(X, Y)
else:
    T_filled = T_obs

method_sep = st.selectbox(
    "Metode Pemisahan",
    ["2D Moving Average", "Trend Surface Analysis"]
)

if method_sep == "2D Moving Average":
    window = st.slider("Lebar Window (grid)", 3, 200, 9, step=2)
    Calculated_Regional = uniform_filter(T_filled, size=window)
else:
    order = st.radio("Orde Polinom", [1, 2], horizontal=True)
    poly = polyfit2d(X, Y, T_obs, order=order)
    Calculated_Regional = poly(X, Y)

Calculated_Residual = T_obs - Calculated_Regional

# ==============================
# HASIL AKHIR
# ==============================
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Regional")
    fig_r, ax_r = plt.subplots(figsize=(6, 5))
    cr = ax_r.contourf(X, Y, Calculated_Regional, levels=20,
                       cmap=cmap_option, vmin=vmin, vmax=vmax)
    fig_r.colorbar(cr, ax=ax_r)
    st.pyplot(fig_r)

with col2:
    st.markdown("### Residual")
    valid = Calculated_Residual[~np.isnan(Calculated_Residual)]
    if scale_mode == "Auto Scale" and len(valid) > 0:
        lim = np.percentile(np.abs(valid), 98)
        vmin_r, vmax_r = -lim, lim
    else:
        vmin_r, vmax_r = vmin, vmax

    fig_res, ax_res = plt.subplots(figsize=(6, 5))
    cres = ax_res.contourf(X, Y, Calculated_Residual, levels=20,
                           cmap=cmap_option, vmin=vmin_r, vmax=vmax_r)
    fig_res.colorbar(cres, ax=ax_res)
    st.pyplot(fig_res)

# ==============================
# SIMPAN GAMBAR
# ==============================
if st.button("Simpan Peta Residual"):
    fig_res.savefig("peta_residual.png", dpi=300, bbox_inches="tight")
    st.success("Peta residual berhasil disimpan")
