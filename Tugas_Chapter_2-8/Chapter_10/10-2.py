from pathlib import Path
p = Path(__file__).with_name("learning_python.txt")
for line in p.read_text(encoding="utf-8").splitlines(): print(line.replace("Python", "C"))
