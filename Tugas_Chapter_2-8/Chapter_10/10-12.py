import json
from pathlib import Path
p = Path(__file__).with_name("favorite_number.json")
def favorite_number():
    if p.exists(): return json.loads(p.read_text(encoding="utf-8"))
    number = input("Angka favorit: ")
    p.write_text(json.dumps(number), encoding="utf-8")
    return number
print("Angka favorit:", favorite_number())
