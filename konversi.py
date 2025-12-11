# file: konversi.py
# berisi fungsi konversi sekaligus program utama

def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9


# Program utama
if __name__ == "__main__":
    print("=== Program Konversi Suhu ===")
    print("1. Celcius ke Fahrenheit")
    print("2. Fahrenheit ke Celcius")

    pilih = input("Pilih jenis konversi (1/2): ")

    if pilih == "1":
        c = float(input("Masukkan nilai Celcius: "))
        hasil = c_to_f(c)
        print(f"Hasil konversi: {hasil:.2f}°F")

    elif pilih == "2":
        f = float(input("Masukkan nilai Fahrenheit: "))
        hasil = f_to_c(f)
        print(f"Hasil konversi: {hasil:.2f}°C")

    else:
        print("Pilihan tidak valid.")
