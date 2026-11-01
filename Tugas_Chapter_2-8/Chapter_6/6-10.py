favorite_numbers = {
    "Alya": [7, 14],
    "Bima": [2, 12, 22],
    "Citra": [3, 15],
    "Doni": [5, 10],
    "Eka": [9, 19],
}
for name, numbers in favorite_numbers.items():
    print(f"{name}: {', '.join(map(str, numbers))}")
