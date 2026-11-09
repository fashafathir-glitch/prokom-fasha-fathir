class Restaurant:
    def __init__(self, name, cuisine): self.name, self.cuisine = name, cuisine
    def describe_restaurant(self): print(f"{self.name}: {self.cuisine}")
for r in [Restaurant("Warung Pagi","Indonesia"), Restaurant("Sushi Kita","Jepang"), Restaurant("Pasta Corner","Italia")]:
    r.describe_restaurant()
