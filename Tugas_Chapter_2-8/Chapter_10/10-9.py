from pathlib import Path
for name in ("cats.txt", "dogs.txt"):
    try: text = Path(__file__).with_name(name).read_text(encoding="utf-8")
    except FileNotFoundError: pass
    else: print(f"Isi {name}:\n{text}")
