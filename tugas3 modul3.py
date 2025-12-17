import random

# ================================
# KELAS DASAR
# ================================
class Sensor:
    def __init__(self, sensor_id, lokasi):
        self.id = sensor_id
        self.lokasi = lokasi
        self.status = "NONAKTIF"
        self.data = []

    def aktifkan_sensor(self):
        self.status = "AKTIF"

    def nonaktifkan_sensor(self):
        self.status = "NONAKTIF"

    def rekam_data(self):
        pass  # Akan dioverride di kelas turunan

    def rata_rata(self):
        if len(self.data) == 0:
            return 0
        return sum(self.data) / len(self.data)


# ================================
# KELAS TURUNAN SENSOR SEISMIK
# ================================
class SensorSeismik(Sensor):
    def __init__(self, sensor_id, lokasi, jenis_gelombang):
        super().__init__(sensor_id, lokasi)
        self.jenis_gelombang = jenis_gelombang

    def rekam_data(self):
        if self.status == "AKTIF":
            nilai = random.uniform(0.1, 5.0)  # amplitudo seismik
            self.data.append(nilai)


# ================================
# KELAS TURUNAN SENSOR GRAVITASI
# ================================
class SensorGravitasi(Sensor):
    def __init__(self, sensor_id, lokasi, resolusi):
        super().__init__(sensor_id, lokasi)
        self.resolusi = resolusi

    def rekam_data(self):
        if self.status == "AKTIF":
            nilai = random.uniform(9.7, 9.9)  # nilai gravitasi
            self.data.append(nilai)


# ================================
# PROGRAM UTAMA
# ================================

# List of object untuk menyimpan semua sensor
daftar_sensor = [
    SensorSeismik("SS01", "Lokasi A", "P-Wave"),
    SensorSeismik("SS02", "Lokasi B", "S-Wave"),
    SensorGravitasi("SG01", "Lokasi C", "0.01 mGal"),
    SensorGravitasi("SG02", "Lokasi D", "0.05 mGal")
]

# Aktifkan semua sensor
for sensor in daftar_sensor:
    sensor.aktifkan_sensor()

# Rekam data (simulasi pembacaan)
for _ in range(5):
    for sensor in daftar_sensor:
        sensor.rekam_data()

# ================================
# LAPORAN DALAM BENTUK TABEL3
# ================================
print("\nLAPORAN SENSOR")
print("-" * 75)
print(f"{'ID Sensor':<10} {'Lokasi':<12} {'Status':<10} {'Jumlah Data':<12} {'Rata-rata':<12}")
print("-" * 75)

for sensor in daftar_sensor:
    print(f"{sensor.id:<10} {sensor.lokasi:<12} {sensor.status:<10} "
          f"{len(sensor.data):<12} {sensor.rata_rata():<12.3f}")

print("-" * 75)