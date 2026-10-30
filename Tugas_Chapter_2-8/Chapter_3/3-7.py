guests = ["Soekarno", "B.J. Habibie", "Mohammad Hatta", "Dewi Sartika", "Ki Hajar Dewantara", "Cut Nyak Dien"]
print("Maaf, meja baru tidak tersedia; hanya dua tamu yang dapat diundang.")
while len(guests) > 2:
    removed = guests.pop()
    print(f"Maaf {removed}, undangan dibatalkan.")
for guest in guests:
    print(f"{guest}, undangan makan malam tetap berlaku.")
del guests[:]
print("Daftar tamu akhir:", guests)
