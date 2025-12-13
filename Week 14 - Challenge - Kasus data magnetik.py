import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.ndimage import uniform_filter
from scipy.interpolate import griddata, NearestNDInterpolator

st.set_page_config(page_title="Analisis Magnetik 2D", layout="wide")

st.title("Pengolahan Data Magnetik 2D")
st.markdown("""
Aplikasi ini melakukan:
- **Gridding data magnetik 2D**
- **Pemisahan anomali Regional & Residual**
- Kontrol **colormap**, **scaling**, dan **visualisasi**
""")

def get_dummy_dataframe(grid_size=50):
    x = np.linspace(0, 1000, grid_size)
    y = np.linspace(0, 1000, grid_size)
    X, Y = np.meshgrid(x, y)

    regional = 0.05 * X + 0.02 * Y + 4500
    r = np.sqrt((X - 500)**2 + (Y - 500)**2 + 50**2)
    residual = 5000 * (50 / r)**3
    noise = np.random.normal(0, 1, X.shape)

    total = regional + residual + noise

    df = pd.DataFrame({
        "x": X.flatten(),
        "y": Y.flatten(),
        "t_obs": total.flatten()
    })

    return df.sample(frac=0.8).reset_index(drop=True)

def polyfit2d(x, y, z, order=1):
    x = x.flatten()
    y = y.flatten()
    z = z.flatten()

    mask = ~np.isnan(z)
    x, y, z = x[mask], y[mask], z[mask]

    if order == 1:
        A = np.c_[np.ones_like(x), x, y]
    else:
        A = np.c_[np.ones_like(x), x, y, x**2, x*y, y**2]

    C, *_ = np.linalg.lstsq(A, z, rcond=None)

    if order == 1:
        return lambda xi, yi: C[0] + C[1]*xi + C[2]*yi
    else:
        return lambda xi, yi: (
            C[0] + C[1]*xi + C[2]*yi +
            C[3]*xi**2 + C[4]*xi*yi + C[5]*yi**2
        )

st.sidebar.header("Input Data")

mode = st.sidebar.radio("Sumber Data", ["Data Dummy", "Upload CSV"])
df_input = None

if mode == "Data Dummy":
    grid_size = st.sidebar.slider("Ukuran Grid Dummy", 20, 100, 50, step=10)
    df_input = get_dummy_dataframe(grid_size)

else:
    file = st.sidebar.file_uploader("Upload CSV (x, y, t_obs)", type=["csv"])
    if file:
        df_input = pd.read_csv(file)

if df_input is None:
    st.stop()

st.sidebar.markdown("---")
st.sidebar.subheader("Visualisasi")

cmap_list = [
    "jet", "viridis", "plasma", "inferno",
    "magma", "cividis", "seismic", "RdBu"
]

selected_cmap = st.sidebar.selectbox(
    "Pilih Colormap",
    cmap_list,
    index=0
)

scale_mode = st.sidebar.radio(
    "Mode Scaling",
    ["Auto Scale", "Manual Scale"]
)

vmin, vmax = None, None
if scale_mode == "Manual Scale":
    vmin = st.sidebar.slider("vmin", -5000.0, 5000.0, -1000.0, step=50.0)
    vmax = st.sidebar.slider("vmax", -5000.0, 5000.0, 1000.0, step=50.0)

st.sidebar.markdown("---")
st.sidebar.subheader("Gridding")

x_min, x_max = df_input.x.min(), df_input.x.max()
y_min, y_max = df_input.y.min(), df_input.y.max()

cell_size = st.sidebar.number_input(
    "Ukuran Grid (m)",
    min_value=1.0,
    max_value=(x_max - x_min) / 5,
    value=(x_max - x_min) / 50
)

interp_method = st.sidebar.selectbox(
    "Interpolasi",
    ["linear", "cubic", "nearest"]
)

xi = np.arange(x_min, x_max + cell_size, cell_size)
yi = np.arange(y_min, y_max + cell_size, cell_size)
X, Y = np.meshgrid(xi, yi)

T_obs = griddata(
    (df_input.x, df_input.y),
    df_input.t_obs,
    (X, Y),
    method=interp_method
)

st.subheader("1. Anomali Magnetik Observasi")

fig, ax = plt.subplots(figsize=(10, 6))
im = ax.contourf(
    X, Y, T_obs, levels=25,
    cmap=selected_cmap,
    vmin=vmin if scale_mode == "Manual Scale" else None,
    vmax=vmax if scale_mode == "Manual Scale" else None
)
fig.colorbar(im, ax=ax, label="nT")
ax.set_aspect("equal")
st.pyplot(fig)

mask_nan = np.isnan(T_obs)
if np.any(mask_nan):
    nn = NearestNDInterpolator(
        (X[~mask_nan], Y[~mask_nan]),
        T_obs[~mask_nan]
    )
    T_filled = nn(X, Y)
else:
    T_filled = T_obs

method = st.selectbox("Metode Pemisahan", ["2D Moving Average", "Trend Surface Analysis"])
if method == "2D Moving Average":
    window = st.slider("Window (grid)", 3, 200, 9, step=2)
    Regional = uniform_filter(T_filled, size=window)
else:
    order = st.radio("Orde Polinomial", [1, 2], horizontal=True)
    Regional = polyfit2d(X, Y, T_obs, order)(X, Y)

Residual = T_obs - Regional

col1, col2 = st.columns(2)
with col1:
    st.markdown("### Regional")
    fig_r, ax_r = plt.subplots(figsize=(6, 5))
    im_r = ax_r.contourf(
        X, Y, Regional, levels=20,
        cmap=selected_cmap,
        vmin=vmin if scale_mode == "Manual Scale" else None,
        vmax=vmax if scale_mode == "Manual Scale" else None
    )
    fig_r.colorbar(im_r, ax=ax_r)
    st.pyplot(fig_r)

with col2:
    st.markdown("### Residual")
    fig_res, ax_res = plt.subplots(figsize=(6, 5))
    im_res = ax_res.contourf(
        X, Y, Residual, levels=20,
        cmap="seismic",
        vmin=vmin if scale_mode == "Manual Scale" else None,
        vmax=vmax if scale_mode == "Manual Scale" else None
    )
    fig_res.colorbar(im_res, ax=ax_res)
    st.pyplot(fig_res)
