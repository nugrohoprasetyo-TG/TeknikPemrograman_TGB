class Sensor:
    def __init__(self, id_sensor, lokasi, jenis):
        self.id_sensor = id_sensor
        self.lokasi = lokasi
        self.jenis = jenis

    def info(self):
        print(f"ID Sensor     : {self.id_sensor}")
        print(f"Lokasi        : {self.lokasi}")
        print(f"Jenis Sensor  : {self.jenis}")


class SensorSeismik(Sensor):
    def __init__(self, id_sensor, lokasi, jenis, frekuensi_sampling):
        super().__init__(id_sensor, lokasi, jenis)
        self.frekuensi_sampling = frekuensi_sampling

    def jumlah_sampel(self, durasi_detik):
        return self.frekuensi_sampling * durasi_detik


sensor1 = SensorSeismik("SS01", "Stasiun A", "Seismik", 100)  

sensor1.info()
print("Frekuensi sampling :", sensor1.frekuensi_sampling, "Hz")

durasi = 10  
print("Jumlah sampel dalam", durasi, "detik =", sensor1.jumlah_sampel(durasi))
