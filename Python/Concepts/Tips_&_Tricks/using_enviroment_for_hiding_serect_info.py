
# For Linux/Mac edit the .bash_profile or .bashrc or .bash_aliases file and add ->
# export DB_USER="db_user_name";
# export DB_PASS="pass123";

# For windows - Control Panel -> System and security -> system -> Advanced System settings -> Enviroment Variables button (Add User Variables)


import os

db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASS')

print(db_user, db_password)
