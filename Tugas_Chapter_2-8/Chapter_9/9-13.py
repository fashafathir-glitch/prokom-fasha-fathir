from random import randint
class Die:
    def __init__(self, sides=6): self.sides = sides
    def roll_die(self): print(randint(1, self.sides))
for sides in (6, 10, 20):
    print(f"Dadu {sides} sisi:")
    die = Die(sides)
    for _ in range(10): die.roll_die()
