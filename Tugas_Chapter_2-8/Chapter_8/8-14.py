def make_car(manufacturer, model, **details):
    details["manufacturer"] = manufacturer
    details["model"] = model
    return details
car = make_car("subaru", "outback", color="biru", tow_package=True)
print(car)
