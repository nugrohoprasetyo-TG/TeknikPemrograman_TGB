# Kelas induk
class Sensor:
    def __init__(self, id_sensor, lokasi, jenis):
        self.id_sensor = id_sensor
        self.lokasi = lokasi
        self.jenis = jenis

    def info(self):
        return f"Sensor ID: {self.id_sensor}, Lokasi: {self.lokasi}, Jenis: {self.jenis}"

# Kelas turunan
class SensorSeismik(Sensor):
    def __init__(self, id_sensor, lokasi, jenis, frekuensi, sensitivitas):
        super().__init__(id_sensor, lokasi, jenis)
        self.frekuensi = frekuensi
        self.sensitivitas = sensitivitas

    def info(self):
        base_info = super().info()
        return f"{base_info}, Frekuensi: {self.frekuensi} Hz, Sensitivitas: {self.sensitivitas}"

# Contoh penggunaan
sensor1 = Sensor("S001", "Gunung Merapi", "Umum")
print(sensor1.info())

sensor2 = SensorSeismik("SS001", "Gunung Merapi", "Seismik", 50, 0.98)
print(sensor2.info())
