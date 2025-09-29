class Sensor:
    def __init__(self, id_sensor, lokasi, jenis):
        self.id_sensor = id_sensor
        self.lokasi = lokasi
        self.jenis = jenis
    
    def info(self):
        return f"Sensor ID: {self.id_sensor}, Lokasi: {self.lokasi}, Jenis: {self.jenis}"
