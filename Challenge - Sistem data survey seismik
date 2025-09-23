survey = {
    "Survey_A": [
    {"trace_id": 1, "receiver": "R1", "offset": 100, "QC_flag": "OK"},
    {"trace_id": 2, "receiver": "R2", "offset": 150, "QC_flag": "OK"},
    {"trace_id": 3, "receiver": "R3", "offset": 200, "QC_flag": "BAD"}
    ],

    "Survey_B": [
    {"trace_id": 4, "receiver": "R1", "offset": 120, "QC_flag": "OK"},
    {"trace_id": 5, "receiver": "R4", "offset": 250, "QC_flag": "OK"},
    {"trace_id": 6, "receiver": "R2", "offset": 300, "QC_flag": "BAD"}
    ],

    "Survey_C": [
    {"trace_id": 7, "receiver": "R5", "offset": 180, "QC_flag": "OK"}
    ]
}

###########################################################################
# Mencari trace dengan QC_flag "BAD" di semua survey
###########################################################################
for nama_survey, daftar_trace in survey.items():
    print("Survey:", nama_survey)
    for trace in daftar_trace:
        if trace["QC_flag"] == "BAD":
            print("Trace ID dengan QC_flag BAD:", trace["trace_id"])
    print(" ")

###########################################################################
# Menghitung total trace di semua survey
###########################################################################
total_trace = sum(len(daftar_trace) for daftar_trace in survey.values())
print("Total trace di seua survey:", total_trace)
print(" ")

###########################################################################
# Mencari survey yang memiliki jumlah trace paling banyak.
###########################################################################
survey_terbanyak = max(survey,key=lambda s: len(s[1]))
print("Survey fengan trace terbanyak:", survey_terbanyak)
print(" ")

###########################################################################
# Membuat set berisi semua receiver unik yang ada di data durvey.
###########################################################################
receivers_unik = set()
for daftar_trace in survey.values():
    for trace in daftar_trace:
        receivers_unik.add(trace["receiver"])
        print("Receiver unik:", receivers_unik)
print(" ")

###########################################################################
# Membuat dictionary yang menetapkan jumlah trace di setiap receiver muncul.
###########################################################################
receiver_count = {}
for daftar_trace in survey.values():
    for trace in daftar_trace:
        receiver = trace["receiver"]
    if receiver in receiver_count:
        receiver_count[receiver] += 1
    else:
        receiver_count[receiver] = 1
        print("Jumlah trace per receiver:", receiver_count)
print (" ")
