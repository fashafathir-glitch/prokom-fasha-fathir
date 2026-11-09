class Restaurant:
    def __init__(self, name, cuisine):
        self.name, self.cuisine, self.number_served = name, cuisine, 0
    def set_number_served(self, number): self.number_served = number
    def increment_number_served(self, number): self.number_served += number
r = Restaurant("Warung Nusantara", "Indonesia")
print(r.number_served)
r.number_served = 12
r.set_number_served(20)
r.increment_number_served(5)
print(r.number_served)
