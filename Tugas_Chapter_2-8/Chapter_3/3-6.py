guests = ["B.J. Habibie", "Dewi Sartika", "Ki Hajar Dewantara"]
print("Saya menemukan meja makan yang lebih besar.")
guests.insert(0, "Soekarno")
guests.insert(len(guests) // 2, "Mohammad Hatta")
guests.append("Cut Nyak Dien")
for guest in guests:
    print(f"{guest}, saya mengundang Anda untuk makan malam.")
