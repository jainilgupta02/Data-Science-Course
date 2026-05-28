correct_password = input("set your password: ")
attempt = 0
while attempt < 3:
    password = input("enter password: ")
    attempt = attempt + 1
    if password == correct_password:
        print("password is correct!")
        break
    else:
        print("password is incorrect, try again...")

if attempt <= 3 and correct_password == password:
    print("logged in.")
elif attempt >= 3:
    print("\n")
    print("attempt exhausted..")