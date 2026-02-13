
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

df = pd.read_csv("survey_gravitasi.csv", sep=r'\s+', engine='python')

print("📊 Informasi Data:")
print(df.info())
print("\n📈 Statistik Deskriptif:")
print(df.describe())

print("\n🔍 Jumlah data kosong per kolom:")
print(df.isnull().sum())

if df['Anomali_Gravitasi_mGal'].isnull().sum() > 0:
    df['Anomali_Gravitasi_mGal'] = df['Anomali_Gravitasi_mGal'].fillna(df['Anomali_Gravitasi_mGal'].mean())
    print("\nNilai kosong telah diisi dengan rata-rata anomali gravitasi.\n")


plt.figure(figsize=(6,5))
plt.scatter(df['X'], df['Y'], c='blue', edgecolor='k')
plt.title('Sebaran Titik Survei Gravitasi')
plt.xlabel('Koordinat Timur (X, meter)')
plt.ylabel('Koordinat Utara (Y, meter)')
plt.grid(True)
plt.savefig('sebaran_titik.png')
print("Plot sebaran titik disimpan sebagai 'sebaran_titik.png'")


x_min, x_max = df['X'].min(), df['X'].max()
y_min, y_max = df['Y'].min(), df['Y'].max()

grid_x, grid_y = np.meshgrid(
    np.linspace(x_min, x_max, 100),
    np.linspace(y_min, y_max, 100)
)


points = np.column_stack((df['X'], df['Y']))
values = df['Anomali_Gravitasi_mGal']

grid_linear = griddata(points, values, (grid_x, grid_y), method='linear')
grid_cubic = griddata(points, values, (grid_x, grid_y), method='cubic')

fig, axs = plt.subplots(1, 2, figsize=(14,6))

cont1 = axs[0].contourf(grid_x, grid_y, grid_linear, cmap='coolwarm', levels=20)
axs[0].scatter(df['X'], df['Y'], c='black', s=10)
axs[0].set_title('Peta Anomali Gravitasi (Interpolasi Linear)')
axs[0].set_xlabel('Koordinat Timur (m)')
axs[0].set_ylabel('Koordinat Utara (m)')
fig.colorbar(cont1, ax=axs[0], label='Anomali Gravitasi (mGal)')

cont2 = axs[1].contourf(grid_x, grid_y, grid_cubic, cmap='coolwarm', levels=20)
axs[1].scatter(df['X'], df['Y'], c='black', s=10)
axs[1].set_title('Peta Anomali Gravitasi (Interpolasi Cubic)')
axs[1].set_xlabel('Koordinat Timur (m)')
axs[1].set_ylabel('Koordinat Utara (m)')
fig.colorbar(cont2, ax=axs[1], label='Anomali Gravitasi (mGal)')

plt.tight_layout()
plt.savefig('peta_anomali.png')
print("Plot peta anomali disimpan sebagai 'peta_anomali.png'")


max_idx = df['Anomali_Gravitasi_mGal'].idxmax()
min_idx = df['Anomali_Gravitasi_mGal'].idxmin()

anomali_max = df.loc[max_idx]
anomali_min = df.loc[min_idx]

print("🧭 Anomali Positif Terkuat (densitas tinggi):")
print(anomali_max, "\n")

print("🕳️ Anomali Negatif Terkuat (densitas rendah):")
print(anomali_min, "\n")

print("✅ Rekomendasi titik pengeboran dapat difokuskan di area sekitar anomali positif untuk eksplorasi mineral padat,")
print("atau area anomali negatif jika targetnya adalah rongga atau zona low-density (misal gas, garam, atau sedimen lunak).")
