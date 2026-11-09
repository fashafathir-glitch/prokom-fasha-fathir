import json
from pathlib import Path
p = Path(__file__).with_name("user_info.json")
def get_username():
    if p.exists(): return json.loads(p.read_text(encoding="utf-8"))
    name = input("Nama Anda: ")
    p.write_text(json.dumps(name), encoding="utf-8")
    return name
name = get_username()
print(f"Selamat datang kembali, {name}!")
