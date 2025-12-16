# ================================
# 1. QC Data Seismik
# ================================
def qc_seismik(data, ambang_offset):
    laporan = {}

    for survey, traces in data.items():
        ok_count = 0
        bad_count = 0

        for trace in traces:
            if trace["offset"] > ambang_offset:
                trace["QC_flag"] = "BAD"
                bad_count += 1
            else:
                trace["QC_flag"] = "OK"
                ok_count += 1

        laporan[survey] = {
            "Total_OK": ok_count,
            "Total_BAD": bad_count
        }

    return laporan


# ================================
# 2. Statistik Gravitasi
# ================================
def statistik_gravitasi(data):
    rata_rata_survey = {}
    semua_nilai = []

    for survey, nilai in data.items():
        rata_rata = sum(nilai) / len(nilai)
        rata_rata_survey[survey] = rata_rata
        semua_nilai.extend(nilai)

    nilai_min = min(semua_nilai)
    nilai_max = max(semua_nilai)

    return rata_rata_survey, nilai_min, nilai_max


# ================================
# 3. Analisis Magnetik
# ================================
def analisis_magnetik(data):
    semua_nilai = []

    for nilai in data.values():
        semua_nilai.extend(nilai)

    nilai_unik = set(semua_nilai)
    nilai_urut = sorted(nilai_unik)

    return nilai_urut


# ================================
# CONTOH DATA & PEMANGGILAN FUNGSI
# ================================

# Data seismik
data_seismik = {
    "Survey_A": [
        {"trace_id": 1, "offset": 800},
        {"trace_id": 2, "offset": 1200},
        {"trace_id": 3, "offset": 600}
    ],
    "Survey_B": [
        {"trace_id": 1, "offset": 1500},
        {"trace_id": 2, "offset": 900}
    ]
}

# Data gravitasi
data_gravitasi = {
    "Survey_A": [9.81, 9.79, 9.82],
    "Survey_B": [9.76, 9.80, 9.78]
}

# Data magnetik
data_magnetik = {
    "Survey_A": [120, 125, 130, 120],
    "Survey_B": [128, 130, 135]
}

# Menjalankan fungsi
laporan_qc = qc_seismik(data_seismik, ambang_offset=1000)
rata_rata, grav_min, grav_max = statistik_gravitasi(data_gravitasi)
hasil_magnetik = analisis_magnetik(data_magnetik)

# Menampilkan hasil
print("Laporan QC Seismik:")
print(laporan_qc)

print("\nStatistik Gravitasi:")
print("Rata-rata per survey:", rata_rata)
print("Nilai terendah:", grav_min)
print("Nilai tertinggi:", grav_max)

print("\nAnalisis Magnetik:")
print("Nilai magnetik unik terurut:", hasil_magnetik)
