current_users = ["Alya", "Bima", "Citra", "Doni", "Eka"]
new_users = ["alya", "Farah", "Gita", "doni", "Hadi"]
current_lower = [user.lower() for user in current_users]
for username in new_users:
    if username.lower() in current_lower:
        print(f"{username} harus memilih nama pengguna lain.")
    else:
        print(f"{username} tersedia.")
