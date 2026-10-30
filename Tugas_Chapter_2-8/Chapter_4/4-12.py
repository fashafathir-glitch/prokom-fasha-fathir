my_foods = ["nasi goreng", "sate", "gado-gado"]
friend_foods = my_foods[:]

my_foods.append("soto")
friend_foods.append("pempek")

print("Makanan favorit saya:")
for food in my_foods:
    print(food)

print("Makanan favorit teman saya:")
for food in friend_foods:
    print(food)