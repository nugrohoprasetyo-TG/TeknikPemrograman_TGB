from abc import ABC, abstractmethod

class Survey(ABC):
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def processing(self):
        pass


class SeismicSurvey(Survey):
    def processing(self):
        print(self.nama, ": melakukan filtering data seismik")


class GravitySurvey(Survey):
    def processing(self):
        print(self.nama, ": melakukan upward continuation")


class MagnetikSurvey(Survey):
    def processing(self):
        print(self.nama, ": melakukan anomaly mapping")


survey1 = SeismicSurvey("Survey Seismik A")
survey2 = GravitySurvey("Survey Gravitasi B")
survey3 = MagnetikSurvey("Survey Magnetik C")

daftar_survey = [survey1, survey2, survey3]

for s in daftar_survey:
    s.processing()
