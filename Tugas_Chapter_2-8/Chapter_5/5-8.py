usernames = ["admin", "alya", "bima", "citra", "doni"]
for username in usernames:
    if username == "admin":
        print("Halo admin, apakah Anda ingin melihat laporan status?")
    else:
        print(f"Halo {username.title()}, terima kasih sudah masuk kembali.")
