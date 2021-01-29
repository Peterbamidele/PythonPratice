from utils import *

celsius = int(input("Enter your temperature in celsius: "))


def celsius_to_fahrenheit(Temperature):
    fahrenheit = add(32, Multiply(Temperature, 1.8))
    return fahrenheit


print((celsius_to_fahrenheit(celsius)))
