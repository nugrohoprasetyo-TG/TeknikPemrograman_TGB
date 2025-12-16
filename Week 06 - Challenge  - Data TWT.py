import csv

with open("data_seismik.txt") as f:
    data = [row for row in csv.DictReader(f)]

if data:
    twt_min = min(float(row["twt"]) for row in data)
    for d in data:
        try:
            twt = float(d["twt"])
            d["twt"] = round((twt - twt_min) / (600 - twt_min),3)
        except (ValueError, KeyError):
            with open("data_seismik.csv", "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=["shot", "receiver", "twt"])
                writer.writeheader()
                writer.writerows(data)
                
print("Hasil tersimpan di 'data_seismik.csv'")
