def hitung_total(harga, jumlah, diskon=0):
    total = harga * jumlah
    if diskon > 0:
        total -= total * (diskon / 100)
    return total


harga = int(input("Masukkan harga: "))
jumlah = int(input("Masukkan jumlah: "))
diskon = int(input("Masukkan diskon (%): "))

total_bayar = hitung_total(harga, jumlah, diskon)
print("Total belanja:", total_bayar)
