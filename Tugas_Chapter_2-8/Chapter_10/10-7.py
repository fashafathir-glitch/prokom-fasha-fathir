while True:
    a = input("Angka pertama (q untuk keluar): ")
    if a.lower() == "q": break
    b = input("Angka kedua: ")
    if b.lower() == "q": break
    try: print("Hasil:", int(a) + int(b))
    except ValueError: print("Input harus angka. Coba lagi.")
