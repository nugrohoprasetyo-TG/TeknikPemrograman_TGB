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
