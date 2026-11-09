from pathlib import Path
name = input("Nama Anda: ").strip()
Path(__file__).with_name("guest.txt").write_text(name + "\n", encoding="utf-8")
print("Nama disimpan.")
