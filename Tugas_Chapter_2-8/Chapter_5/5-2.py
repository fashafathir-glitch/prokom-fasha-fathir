
# 1. Equality dan inequality pada string
print("apple" == "apple")
print("apple" != "Apple")

# 2. Menggunakan lower()
print("Apple".lower() == "apple")
print("JAVA".lower() == "python")

# 3. Pengujian angka
print(7 == 7)
print(7 != 8)
print(9 > 3)
print(2 < 1)
print(5 >= 5)
print(4 <= 2)

# 4. Menggunakan and dan or
print(10 > 5 and 8 > 3)
print(10 > 5 and 8 < 3)
print(10 > 5 or 8 < 3)
print(10 < 5 or 8 < 3)

# 5. Memeriksa apakah item ada dalam list
foods = ["nasi", "ayam", "sayur", "ikan"]

print("nasi" in foods)
print("pizza" in foods)

# 6. Memeriksa apakah item tidak ada dalam list
print("pizza" not in foods)
print("ikan" not in foods)
