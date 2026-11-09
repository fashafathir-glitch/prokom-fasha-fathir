class Restaurant:
    def __init__(self, name, cuisine): self.name, self.cuisine = name, cuisine
class IceCreamStand(Restaurant):
    def __init__(self, name):
        super().__init__(name, "es krim")
        self.flavors = ["vanila", "cokelat", "stroberi", "matcha"]
    def show_flavors(self):
        for flavor in self.flavors: print(flavor)
IceCreamStand("Gelato Ceria").show_flavors()
