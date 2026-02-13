import konversi

# Input Celcius → Fahrenheit
c = float(input("Masukkan suhu Celcius: "))
print("Suhu dalam Fahrenheit =", round(konversi.c_to_f(c), 2))

# Input Fahrenheit → Celcius
f = float(input("Masukkan suhu Fahrenheit: "))
print("Suhu dalam Celcius =", round(konversi.f_to_c(f), 2))
