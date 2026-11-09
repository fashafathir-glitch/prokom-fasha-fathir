class Restaurant:
    def __init__(self, name, cuisine): self.name, self.cuisine = name, cuisine
    def describe_restaurant(self): print(f"{self.name} menyajikan {self.cuisine}.")
