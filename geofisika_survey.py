from abc import ABC, abstractmethod

# Kelas abstrak
class Survey(ABC):
    def __init__(self, nama_survey, lokasi):
        self.nama_survey = nama_survey
        self.lokasi = lokasi

    @abstractmethod
    def processing(self):
        pass

# Subclass SeismicSurvey
class SeismicSurvey(Survey):
    def processing(self):
        return f"Seismic Survey '{self.nama_survey}' di {self.lokasi}: Melakukan filtering sinyal seismik"

# Subclass GravitySurvey
class GravitySurvey(Survey):
    def processing(self):
        return f"Gravity Survey '{self.nama_survey}' di {self.lokasi}: Melakukan upward continuation"

# Subclass MagnetikSurvey
class MagnetikSurvey(Survey):
    def processing(self):
        return f"Magnetik Survey '{self.nama_survey}' di {self.lokasi}: Membuat peta anomali magnetik"

# Membuat objek
survey1 = SeismicSurvey("Survey A", "Gunung Merapi")
survey2 = GravitySurvey("Survey B", "Lembah Baliem")
survey3 = MagnetikSurvey("Survey C", "Papua")

# Masukkan ke list
daftar_survey = [survey1, survey2, survey3]

# Iterasi dan panggil method processing()
for s in daftar_survey:
    print(s.processing())
