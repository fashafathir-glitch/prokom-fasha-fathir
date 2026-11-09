class User:
    def __init__(self, first, last):
        self.first, self.last, self.login_attempts = first, last, 0
    def increment_login_attempts(self): self.login_attempts += 1
    def reset_login_attempts(self): self.login_attempts = 0
u = User("Fasha", "Ubaidillah")
for _ in range(4): u.increment_login_attempts()
print(u.login_attempts)
u.reset_login_attempts()
print(u.login_attempts)
