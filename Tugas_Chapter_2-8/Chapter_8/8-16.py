# 1. Import seluruh modul
import greeting_functions
greeting_functions.greet_user("fasha")

# 2. Import fungsi tertentu
from greeting_functions import greet_user
greet_user("fasha")

# 3. Import fungsi dengan alias
from greeting_functions import greet_user as gu
gu("fasha")

# 4. Import modul dengan alias
import greeting_functions as gf
gf.greet_user("fasha")

# 5. Import seluruh fungsi dari modul
from greeting_functions import *
greet_user("fasha")