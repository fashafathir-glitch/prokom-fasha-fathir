prompt = "Masukkan usia (ketik 'quit' untuk selesai): "
while True:
    answer = input(prompt)
    if answer.lower() == "quit":
        break
    age = int(answer)
    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15
    if price == 0:
        print("Tiket gratis.")
    else:
        print(f"Harga tiket: ${price}.")
