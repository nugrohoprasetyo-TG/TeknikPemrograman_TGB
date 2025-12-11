from abc import ABC, abstractmethod

class Survey(ABC):
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def processing(self):
        pass


class SeismicSurvey(Survey):
    def processing(self):
        print(f"[{self.nama}] Processing: Melakukan filtering sinyal seismik...")


class GravitySurvey(Survey):
    def processing(self):
        print(f"[{self.nama}] Processing: Menghitung upward continuation data gravitasi...")


class MagnetikSurvey(Survey):
    def processing(self):
        print(f"[{self.nama}] Processing: Membuat anomaly mapping data magnetik...")


survey_list = [
    SeismicSurvey("Survey Seismik 01"),
    GravitySurvey("Survey Gravitasi 01"),
    MagnetikSurvey("Survey Magnetik 01")
]

for s in survey_list:
    s.processing()
