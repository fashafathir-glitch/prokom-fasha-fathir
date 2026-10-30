my_pizzas = ["margherita", "pepperoni", "jamur"]
friend_pizzas = my_pizzas[:]
my_pizzas.append("keju")
friend_pizzas.append("nanas")
print("Pizza saya:")
for pizza in my_pizzas:
    print(pizza)
print("Pizza teman:")
for pizza in friend_pizzas:
    print(pizza)
