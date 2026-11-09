import json
from pathlib import Path
p = Path(__file__).with_name("favorite_number.json")
if p.exists(): print("Angka favorit:", json.loads(p.read_text(encoding="utf-8")))
else:
    number = input("Angka favorit Anda: ")
    p.write_text(json.dumps(number), encoding="utf-8")
    print("Angka disimpan.")
