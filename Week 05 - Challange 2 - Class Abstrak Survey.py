from abc import ABC, abstractmethod

class Survey(ABC):
    def __init__(self, lokasi):
        self.lokasi = lokasi
    @abstractmethod
    def metode(self):
        pass
    @abstractmethod
    def processing(self):
        pass
    def info(self):
        return f"Survey di lokasi: {self.lokasi}"
    
class SeismicSurvey(Survey):
    def __init__(self, lokasi, frekuensi_sampling):
        super().__init__(lokasi)
        self.frekuensi_sampling = frekuensi_sampling
    def metode(self):
        return f"Metode Seismik, fs={self.frekuensi_sampling} Hz"
    def processing(self):
        return "Filtering data seismik"

class GravitySurvey(Survey):
    def __init__(self, lokasi, sensivitas):
        super().__init__(lokasi)
        self.sensivitas = sensivitas
    def metode(self):
        return f"Metode gravitasi, sensivitas={self.sensivitas} mGal"
    def processing(self):
        return "Upward continuation pada gravitasi"

class MagnetikSurvey(Survey):
    def __init__(self, lokasi, resolusi):
        super().__init__(lokasi)
        self.resolusi = resolusi
    def metode(self):
        return f"Metode magnetik, resolusi={self.resolusi} nT"
    def processing(self):
        return "Anomaly maping pada data magnetik"
