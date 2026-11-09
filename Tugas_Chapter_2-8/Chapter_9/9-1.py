class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name, self.cuisine_type = restaurant_name, cuisine_type
    def describe_restaurant(self): print(f"{self.restaurant_name} menyajikan {self.cuisine_type}.")
    def open_restaurant(self): print(f"{self.restaurant_name} sekarang buka.")
r = Restaurant("Warung Nusantara", "masakan Indonesia")
print(r.restaurant_name, r.cuisine_type)
r.describe_restaurant()
r.open_restaurant()
