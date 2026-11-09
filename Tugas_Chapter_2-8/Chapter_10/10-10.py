from pathlib import Path
p = Path(__file__).with_name("learning_python.txt")
try: text = p.read_text(encoding="utf-8")
except FileNotFoundError: print("File teks tidak ditemukan.")
else: print("Jumlah kemunculan kata the:", text.lower().count("the "))
