import kalkulator_lib

def buat_salam(nama):
    return (f"Selamat pagi. {nama}!")

nama_user = "Inggrit irwanti"
print(buat_salam(nama_user))

def tampilkan_menu():
    print("\n--- kalkulator sederhana ---")
    print("1. penjumlahan")
    print("2. pengurangan")
    print("3. perkalian")
    print("4. pembagian")
    print("5. pangkat")
    print("6. keluar")

while True:
    tampilkan_menu()
    pilihan = input("pilihan oprasi (1/2/3/4/5/6): ")

    if pilihan == '6':
        print("terima kasih telah menggunakan kalkulator!")
        break

    if pilihan in ['1', '2', '3', '4' '5']:
        try:
            a = float(input("masukan angka pertama: "))
            b = float(input("masukan angka kedua: "))
        except ValueError:
            print("input tidak valid. harap masukan angka. ")
            continue
        hasil = None
        if pilihan == '1':
            hasil = kalkulator_lib.tambah(a, b)
        elif pilihan == '2':
            hasil = kalkulator_lib.kurang(a, b)
        elif pilihan == '3':
            hasil = kalkulator_lib.kali(a, b)
        elif pilihan == '4':
            hasil = kalkulator_lib.bagi(a, b)
        elif pilihan == '5':
            hasil = kalkulator_lib.pangkat(a, b)
        
        print(f"Hasilnya adalah: {hasil}")
    
    else:
        print("pilihan tidak valid. silakan coba lagi.")