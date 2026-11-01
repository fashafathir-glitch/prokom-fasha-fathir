# Versi 1: kondisi while
answer = ""
while answer != "quit":
    answer = input("Masukkan topping (quit untuk berhenti): ")
    if answer != "quit":
        print(f"Menambahkan {answer}.")

# Versi 2: active variable
active = True
while active:
    answer = input("Masukkan topping (quit untuk berhenti): ")
    if answer == "quit":
        active = False
    else:
        print(f"Menambahkan {answer}.")

# Versi 3: break
while True:
    answer = input("Masukkan topping (quit untuk berhenti): ")
    if answer == "quit":
        break
    print(f"Menambahkan {answer}.")
