from random import choice
items = list(range(1, 11)) + list("ABCDE")
print("Tiket pemenang:", [choice(items) for _ in range(4)])
