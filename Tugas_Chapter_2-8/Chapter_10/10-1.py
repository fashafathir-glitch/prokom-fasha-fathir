from pathlib import Path
p = Path(__file__).with_name("learning_python.txt")
contents = p.read_text(encoding="utf-8")
print(contents)
for line in contents.splitlines(): print(line)
