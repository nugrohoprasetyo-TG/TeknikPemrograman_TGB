@@ -0,0 +1,165 @@
import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

    #####=============#####
        # KELAS UTAMA
    #####=============#####
class PengeluaranApp:
    FILE_NAME = "pengeluaran.csv"

    def __init__(self):
        self.prepare_csv()
        self.df = self.load_data()

    #####==============#####
        # FILE HANDLING
    #####==============#####
    def prepare_csv(self):
        if not os.path.exists(self.FILE_NAME):
            df = pd.DataFrame(columns=["ID", "Tanggal", "Kategori", "Jumlah", "Catatan"])
            df.to_csv(self.FILE_NAME, index=False)

    def load_data(self):
        return pd.read_csv(self.FILE_NAME)

    def save_data(self):
        self.df.to_csv(self.FILE_NAME, index=False)

    #####===================#####
        # MAIN UI STREAMLIT
    #####===================#####
    def run(self):
        st.title("💰 Aplikasi Pelacak Pengeluaran")

        menu = st.sidebar.selectbox(
            "Menu",
            [
                "Tambah Data",
                "Lihat Data",
                "Hapus Data",
                "Visualisasi Kategori",
                "Visualisasi Tren Tanggal"
            ]
        )

        if menu == "Tambah Data":
            self.tambah_data()

        elif menu == "Lihat Data":
            self.lihat_data()

        elif menu == "Hapus Data":
            self.hapus_data()

        elif menu == "Visualisasi Kategori":
            self.plot_by_kategori()

        elif menu == "Visualisasi Tren Tanggal":
            self.plot_by_tanggal()

    #####=============#####
        # TAMBAH DATA
    #####=============#####
    def tambah_data(self):
        st.subheader("Tambah Pengeluaran Baru")

        tanggal = st.date_input("Tanggal")
        kategori = st.text_input("Kategori")
        jumlah = st.number_input("Jumlah (Rp)", min_value=0.0, step=500.0)
        catatan = st.text_area("Catatan")

        if st.button("💾 Simpan Data"):
            new_id = 1 if self.df.empty else self.df["ID"].max() + 1

            self.df.loc[len(self.df)] = [
                new_id,
                str(tanggal),
                kategori,
                jumlah,
                catatan,
            ]

            self.save_data()
            st.success("Data berhasil ditambahkan!")

    #####===========#####
        # LIHAT DATA
    #####===========#####
    def lihat_data(self):
        st.subheader("📄 Daftar Pengeluaran")

        if self.df.empty:
            st.info("Belum ada data.")
        else:
            st.dataframe(self.df)

    #####===========#####
        # HAPUS DATA
    #####==========#####
    def hapus_data(self):
        st.subheader("🗑 Hapus Data Pengeluaran")

        if self.df.empty:
            st.info("Tidak ada data yang bisa dihapus.")
            return

        pilih_id = st.selectbox("Pilih ID yang akan dihapus:", self.df["ID"])

        if st.button("Hapus"):
            self.df = self.df[self.df["ID"] != pilih_id]
            self.save_data()
            st.success("Data berhasil dihapus!")

    #####===============================#####
        # VISUALISASI TOTAL PER KATEGORI
    #####===============================#####
    def plot_by_kategori(self):
        st.subheader("📊 Total Pengeluaran per Kategori")

        if self.df.empty:
            st.info("Belum ada data untuk divisualisasikan.")
            return

        kategori_sum = self.df.groupby("Kategori")["Jumlah"].sum()

        fig, ax = plt.subplots(figsize=(8, 5))
        ax.bar(kategori_sum.index, kategori_sum.values)
        ax.set_title("Total Pengeluaran per Kategori")
        ax.set_xlabel("Kategori")
        ax.set_ylabel("Jumlah (Rp)")
        plt.xticks(rotation=30)

        st.pyplot(fig)

    #####==============================#####
        # VISUALISASI TREND PER TANGGAL
    #####==============================#####
    def plot_by_tanggal(self):
        st.subheader("📈 Tren Pengeluaran Harian")

        if self.df.empty:
            st.info("Belum ada data untuk divisualisasikan.")
            return

        df = self.df.copy()
        df["Tanggal"] = pd.to_datetime(df["Tanggal"])
        df_sorted = df.sort_values("Tanggal")

        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(df_sorted["Tanggal"], df_sorted["Jumlah"], marker="o")
        ax.set_title("Tren Pengeluaran Harian")
        ax.set_xlabel("Tanggal")
        ax.set_ylabel("Jumlah (Rp)")
        plt.xticks(rotation=30)

        st.pyplot(fig)


    #####==================#####
        # JALANKAN APP
    #####==================#####
if __name__ == "__main__":
    app = PengeluaranApp()
    app.run()