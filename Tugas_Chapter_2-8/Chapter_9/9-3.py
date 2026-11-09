class User:
    def __init__(self, first, last, age, city, job):
        self.first, self.last, self.age, self.city, self.job = first, last, age, city, job
    def describe_user(self): print(self.first, self.last, self.age, self.city, self.job)
    def greet_user(self): print(f"Halo, {self.first.title()}!")
for u in [User("andi","saputra",20,"Yogyakarta","Mahasiswa"), User("siti","aminah",21,"Bandung","Desainer")]:
    u.describe_user()
    u.greet_user()
