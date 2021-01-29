from utils import *
def celcius_to_fahrenheit(Celcius_value: float):
    return add(multiply(celcius_to_value, 1.8), 32)


values_str = input("Type in your temperature separated by comma")
print("val_str", values_str)

values_str_list = values_str.split(",")
print("val_list", values_str_list)

for values_str in values_str_list:
    temp_celcius_value = float(values_str)
    fahrenheit_value = celcius_to_fahrenheit(temp_celcius_value)

    print(f"{temp_celcius_value} deg Celsius is {fahrenheit_value} deg Fahrenheit ")
