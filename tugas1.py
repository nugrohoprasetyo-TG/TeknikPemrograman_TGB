def hitung_total(harga, jumlah, diskon=0):
    total = harga * jumlah
    if diskon > 0:
        total -= total * diskon / 100
    return total


harga = int(input("Masukkan harga barang: "))
jumlah = int(input("Masukkan jumlah barang: "))
diskon = int(input("Masukkan diskon (%): "))

print("Total harga:", hitung_total(harga, jumlah, diskon))
