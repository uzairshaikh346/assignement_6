# Assignment:
# Create a custom exception InvalidAgeError. 
# Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.

class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18 years old!")
    
    else:
        print("Access Granted!")


try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print("Invalid Age Error:", e)
except ValueError:
    print("Please enter a valid number.")
