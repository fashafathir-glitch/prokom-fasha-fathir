class User:
    def __init__(self, first, last): self.first, self.last = first, last
class Privileges:
    def __init__(self): self.privileges = ["can add post", "can delete post", "can ban user"]
    def show_privileges(self):
        for p in self.privileges: print(p)
class Admin(User):
    def __init__(self, first, last):
        super().__init__(first, last)
        self.privileges = Privileges()
