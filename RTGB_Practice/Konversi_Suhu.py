unit = input("Apakah temperatur dalam Celcius atau Fahrenheit (C/F): ")
temp = float(input("Masukkan suhu: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"Temperatur dalam Fahrenheit adalah: {temp}F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"Temperatur dalam Celcius adalah: {temp}C")
else: 
   print(f"pengukuran {unit} tidak valid")