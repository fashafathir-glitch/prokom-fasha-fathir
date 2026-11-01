sandwich_orders = [
    "pastrami", "tuna", "pastrami",
    "ayam", "pastrami", "sayur"
]

print("Deli kehabisan pastrami.")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"Sandwich {sandwich} sudah dibuat.")
    finished_sandwiches.append(sandwich)

print("\nDaftar sandwich yang selesai:")
for sandwich in finished_sandwiches:
    print(sandwich)