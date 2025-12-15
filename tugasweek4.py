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

print("Trace ID dengan QC BAD:")
for nama_survey in survey:
    for data in survey[nama_survey]:
        if data["QC_flag"] == "BAD":
            print(data["trace_id"])

total = 0
for nama_survey in survey:
    total += len(survey[nama_survey])

print("\nTotal trace dari semua survey:", total)

terbanyak = ""
jumlah_max = 0

for nama_survey in survey:
    if len(survey[nama_survey]) > jumlah_max:
        jumlah_max = len(survey[nama_survey])
        terbanyak = nama_survey

print("\nSurvey dengan jumlah trace terbanyak:", terbanyak)

receiver_set = set()
for nama_survey in survey:
    for data in survey[nama_survey]:
        receiver_set.add(data["receiver"])

print("\nReceiver unik:", receiver_set)

receiver_jumlah = {}

for nama_survey in survey:
    for data in survey[nama_survey]:
        rcv = data["receiver"]
        if rcv in receiver_jumlah:
            receiver_jumlah[rcv] += 1
        else:
            receiver_jumlah[rcv] = 1

print("\nJumlah trace per receiver:")
for r in receiver_jumlah:
    print(r, "=", receiver_jumlah[r])
