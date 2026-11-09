from user_module import User
from admin_privileges_module import Admin
u = User("Siti", "Aminah")
print(u.first, u.last)
Admin("Fasha", "Ubaidillah").privileges.show_privileges()
