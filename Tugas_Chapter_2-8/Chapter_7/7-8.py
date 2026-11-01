sandwich_orders = ["tuna", "pastrami", "ayam", "sayur"]
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"Saya membuat sandwich {sandwich}.")
    finished_sandwiches.append(sandwich)

print("\nSandwich yang sudah dibuat:")
for sandwich in finished_sandwiches:
    print(sandwich)