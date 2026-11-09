class Battery:
    def __init__(self, size=75): self.battery_size = size
    def upgrade_battery(self):
        if self.battery_size != 65: self.battery_size = 65
    def get_range(self):
        ranges = {75: 260, 65: 225}
        print(f"Jarak tempuh sekitar {ranges.get(self.battery_size, 200)} mil.")
class ElectricCar:
    def __init__(self): self.battery = Battery()
car = ElectricCar()
car.battery.get_range()
car.battery.upgrade_battery()
car.battery.get_range()
