from pathlib import Path
p = Path(__file__).with_name("guest_book.txt")
while True:
    name = input("Nama (q untuk selesai): ").strip()
    if name.lower() == "q": break
    with p.open("a", encoding="utf-8") as f: f.write(name + "\n")
