foods = ("nasi", "ayam bakar", "sayur", "ikan", "buah")

print("Menu awal:")
for food in foods:
    print(food)

try:
    foods[0] = "roti"
except TypeError:
    print("Tuple tidak bisa diubah!")

foods = ("nasi", "ayam goreng", "sayur", "tempe", "buah")

print("Menu baru:")
for food in foods:
    print(food)
    