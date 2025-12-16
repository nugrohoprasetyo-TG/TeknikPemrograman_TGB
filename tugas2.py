def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

celcius = float(input("Masukkan suhu dalam Celcius: "))
fahrenheit = c_to_f(celcius)
print("Celcius ke Fahrenheit =", fahrenheit)

f = float(input("\nMasukkan suhu dalam Fahrenheit: "))
c = f_to_c(f)
print("Fahrenheit ke Celcius =", c)
