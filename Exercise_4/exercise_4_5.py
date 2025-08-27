no_tries = 5
username = "james"
password = "bond"

while no_tries != 0:
    username_input = input("username: ")
    password_input = input("password: ")
    if username_input == username and password_input == password:
        print("Welcome")
        break
    else:
        print("Incorrect username or password. \nTry again.")
        no_tries -= 1

if no_tries == 0:
    print("Access denied")