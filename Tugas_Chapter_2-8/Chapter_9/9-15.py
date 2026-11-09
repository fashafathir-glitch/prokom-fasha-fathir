from random import choice
items = list(range(1, 11)) + list("ABCDE")
my_ticket = [2, "B", 7, "D"]
attempts = 0
while True:
    drawn = [choice(items) for _ in range(4)]
    attempts += 1
    if drawn == my_ticket: break
print(f"Menang setelah {attempts:,} percobaan.")
