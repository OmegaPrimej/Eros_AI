try:
    x = 5 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

try:
    raise ValueError("Invalid value")
except ValueError as e:
    print(e)

class CustomError(Exception):
    pass

try:
    raise CustomError("Something went wrong")
except CustomError as e:
    print(e)
