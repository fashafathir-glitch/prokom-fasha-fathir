favorite_places = {
    "Alya": ["Bali", "Kyoto"],
    "Bima": ["Gunung Bromo"],
    "Citra": ["Yogyakarta", "Lombok", "Bandung"],
}
for person, places in favorite_places.items():
    print(f"Tempat favorit {person}:")
    for place in places:
        print(f"- {place}")
