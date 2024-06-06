#LEVEL2-T3
#Task: Password Strength Checker
#Create a Python function that evaluates the strength of a password entered by the user. Implement checks for factors such as length, presence of uppercase and lowercase letters, digits, and special characters.
def password_check(password):
    if len(password) < 6:
        print("Password must be at least 6 characters long!")
        return False
    if not any(c.isupper() for c in password):
        print("Password must contain at least one uppercase letter!")
        return False
    if not any(c.islower() for c in password):
        print("Password must contain at least one lowercase letter!")
        return False
    if not any(c.isdigit() for c in password):
        print("Password must contain at least one digit!")
        return False
    if not any(c in '$@#' for c in password):
        print("Password must contain at least one of the symbols $@#")
        return False
    print("Strong password!")
    return True

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Enter a password: ")
    if password_check(password):
        break
    attempts += 1

if attempts == max_attempts:
    print("Maximum number of attempts reached. Exiting...")
else:
    print("Password accepted!")

