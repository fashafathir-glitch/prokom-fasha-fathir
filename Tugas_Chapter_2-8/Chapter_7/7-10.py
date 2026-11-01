responses = {}
polling_active = True
while polling_active:
    name = input("Siapa nama Anda? ")
    place = input("Ke mana Anda ingin berlibur? ")
    responses[name] = place
    repeat = input("Apakah orang lain ingin menjawab? (ya/tidak) ")
    if repeat.lower() != "ya":
        polling_active = False
print("\nHasil polling:")
for name, place in responses.items():
    print(f"{name} ingin berlibur ke {place}.")
