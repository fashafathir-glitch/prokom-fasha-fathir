favorite_languages = {"Alya": "Python", "Bima": "JavaScript", "Citra": "Python"}
people = ["Alya", "Doni", "Citra", "Eka"]
for person in people:
    if person in favorite_languages:
        print(f"Terima kasih, {person}, sudah mengikuti polling.")
    else:
        print(f"{person}, silakan ikuti polling bahasa pemrograman favorit.")
