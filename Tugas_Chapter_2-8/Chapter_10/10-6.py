try:
    a = int(input("Angka pertama: "))
    b = int(input("Angka kedua: "))
except ValueError: print("Masukkan angka bulat yang valid.")
else: print("Hasil:", a + b)
