#CHALLENGE 13

import streamlit as st
import segyio
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# ------------------------------
# FUNGSI BACA HEADER
# ------------------------------
def read_segy_data_header(segy_path, segy_byte_locs, length=4, signed=True):
    """
    Membaca nilai dari beberapa byte location pada trace header SEG-Y.

    Parameters
    ----------
    segy_path : str
        Path ke file SEG-Y.
    segy_byte_locs : iterable of int
        Daftar byte location (1-based) pada trace header (1–240).
        Misal: [181, 185, 189].
    length : int, optional
        Panjang field dalam byte (default 4 byte).
    signed : bool, optional
        Jika True nilai dianggap signed integer, jika False unsigned.

    Returns
    -------
    values : np.ndarray
        Array dengan shape (n_traces, n_locs), berisi nilai dari byte locations.
        Kolom ke-j berkorespondensi dengan segy_byte_locs[j].
    header_df : pandas.DataFrame
        DataFrame dengan kolom "byte_<loc>" untuk setiap loc di segy_byte_locs.
    """
    segy_byte_locs = list(segy_byte_locs)  # pastikan bisa diindeks

    with segyio.open(segy_path, "r", ignore_geometry=True) as f:
        n_traces = f.tracecount
        n_locs = len(segy_byte_locs)

        # Siapkan array penampung
        values = np.zeros((n_traces, n_locs), dtype=np.int32)
        data_segy =[]
        for i in range(n_traces):
            h = f.header[i]       # Trace header
            buf = h.buf           # bytearray 240 byte

            for j, byte_pos in enumerate(segy_byte_locs):
                start = byte_pos - 1          # konversi ke 0-based index
                raw = bytes(buf[start:start+length])
                values[i, j] = int.from_bytes(raw, byteorder="big", signed=signed)
            data_segy.append(f.trace[i])

    # Buat DataFrame header yang rapi
    col_names = [f"byte_{loc}" for loc in segy_byte_locs]
    header_df = pd.DataFrame(values, columns=col_names)

    return np.array(data_segy).T, header_df

if "df_header" not in st.session_state:
    st.session_state.df_header = None

if "data_segy" not in st.session_state:
    st.session_state.data_segy = None

# ------------------------------
# STREAMLIT APP
# ------------------------------
st.title("📌 Streamlit Viewer — Post-Stack SEG-Y")

st.write("Aplikasi sederhana untuk loading SEG-Y post-stack, membaca header CDP/CDP-X/CDP-Y, dan memplot data.")

# Upload SEG-Y
uploaded = st.file_uploader("Upload File SEG-Y", type=["sgy", "segy"])


if uploaded is not None:
    st.success("File berhasil di-upload!")

    # simpan file sementara
    tmp_path = "temp_uploaded.sgy"
    with open(tmp_path, "wb") as f:
        f.write(uploaded.read())

    # Input byte location
    st.subheader("Masukkan Lokasi Byte (1-based index, sesuai SEG-Y Spec)")
    col1, col2, col3 = st.columns(3)
    byte_cdp   = col1.number_input("Byte CDP (awal)", value=9)
    byte_cdp_x = col2.number_input("Byte CDP-X (awal)", value=73)
    byte_cdp_y = col3.number_input("Byte CDP-Y (awal)", value=77)

    btn_load = st.button("Loading Segy to Memory", type="primary")

    if btn_load:
        byte_locs = [byte_cdp, byte_cdp_x, byte_cdp_y]   # misal CDP, CDP-X, CDP-Y by byte location
        segy_path = tmp_path
        vals, header_df = read_segy_data_header(segy_path, byte_locs)
        st.session_state.df_header = header_df
        st.session_state.data_segy = vals
        st.info("Loading Sukses!")

    if st.session_state.data_segy is not None:
        with st.expander("Header View"):
            st.write(st.session_state.df_header)
        
        with st.expander("Segy Data"):
            st.write("Ploting Data!")

            st.write(f"Index Min CDP : {0}, Index Max CDP : {st.session_state.data_segy.shape[1]}")

            cdp_min = st.number_input("CDP Min : ", 0)
            cdp_max = st.number_input("CDP Max : ", 500)
            data = st.session_state.data_segy[:, cdp_min:cdp_max]

            btn_plot = st.button("Plot")

            if btn_plot:
                # Seismic colormap untuk Plotly (approx)
                seismic_colors = [
                    [0.0, "blue"],
                    [0.5, "white"],
                    [1.0, "red"],
                ]

                fig = px.imshow(
                    data,
                    color_continuous_scale=seismic_colors,
                    aspect="auto",
                    origin="lower",   # data tetap dibaca dari bawah
                )

                # Membalik sumbu Y
                fig.update_yaxes(autorange="reversed")

                fig.update_layout(
                    height=600,
                    xaxis_title="Trace",
                    yaxis_title="Time Sample",
                )

                st.plotly_chart(fig, use_container_width=True)

                btn_load = True
