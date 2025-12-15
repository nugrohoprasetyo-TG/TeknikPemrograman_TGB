class Sensor:
    def __init__(self, id_sensor, lokasi, jenis):
        self.id_sensor = id_sensor
        self.lokasi = lokasi
        self.jenis = jenis

    def info(self):
        print("ID Sensor :", self.id_sensor)
        print("Lokasi    :", self.lokasi)
        print("Jenis     :", self.jenis)


class SensorSeismik(Sensor):
    def __init__(self, id_sensor, lokasi, jenis, frekuensi_sampling):
        super().__init__(id_sensor, lokasi, jenis)
        self.frekuensi_sampling = frekuensi_sampling

    def jumlah_sampel(self, durasi):
        return self.frekuensi_sampling * durasi


sensor1 = SensorSeismik("SS-01", "Lampung", "Seismik", 100)

sensor1.info()
print("Frekuensi Sampling :", sensor1.frekuensi_sampling, "Hz")

durasi_pengukuran = 10 
print("Jumlah sampel :", sensor1.jumlah_sampel(durasi_pengukuran))
