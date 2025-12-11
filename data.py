data = [
    {"survey": "A", "trace_id": 1, "QC_flag": "GOOD", "receiver": "R01"},
    {"survey": "A", "trace_id": 2, "QC_flag": "BAD", "receiver": "R02"},
    {"survey": "B", "trace_id": 3, "QC_flag": "BAD", "receiver": "R01"},
    {"survey": "B", "trace_id": 4, "QC_flag": "GOOD", "receiver": "R03"},
    {"survey": "B", "trace_id": 5, "QC_flag": "GOOD", "receiver": "R01"},
]

bad_traces = [row["trace_id"] for row in data if row["QC_flag"] == "BAD"]
print("Trace QC BAD:", bad_traces)

total_trace = len(data)
print("Total trace:", total_trace)

survey_count = {}
for row in data:
    nama = row["survey"]
    survey_count[nama] = survey_count.get(nama, 0) + 1

survey_terbanyak = max(survey_count, key=survey_count.get)
print("Survey dengan trace terbanyak:", survey_terbanyak)

receiver_unik = {row["receiver"] for row in data}
print("Receiver unik:", receiver_unik)

receiver_count = {}
for row in data:
    r = row["receiver"]
    receiver_count[r] = receiver_count.get(r, 0) + 1

print("Jumlah trace per receiver:", receiver_count)
