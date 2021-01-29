def add(num1: float, num2: float) -> float:
    """a function that add two numbers"""
    # logic here

    num3 = num1 + num2
    return num3


def subtract(num1: float, num2: float) -> float:
    """a function that divides two numbers,num1 divided ny mum2"""
    num3 = num1 - num2
    return num3


def divide(num1: float, num2: float) -> float:
    """a function that divides two numbers,num1 divided ny mum2"""
    num3 = num1 / num2
    return num3


def multiply(num1: float, num2: float) -> float:
    """a function that divides two numbers,num1 divided ny mum2"""
    num3 = num1 * num2
    return num3


def square_root(num1: float) -> float:
    """a function that returns the square root of a number"""
    num2 = num1 ** 0.5
    return num2


def square(num1: float) -> float:
    """a function that returns the square of a number"""
    num2 = num1 ** 2
    return num2


def run_test():
    assert add(2, 3) == 5, "2 + 3 is 5"
    assert multiply(2, 3) == 6, "2 * 3 is 6"
    assert subtract(2, 3) == -1, "2 - 3 is -1"
    assert divide(6, 3) == 2, "6 / 3 is 2"
    assert square_root(9) == 3, "square root of 9 is 3"
    assert square(2) == 4, "square 0f 2 is 4"


def main():
    # run all the test
    print("Running tests.......")
    run_test()
    run_test()
    print("all the test................")

    # add 2 numbers
    x = 2
    y = 10
    z = add(x + y)
    print()

    print(f"x + y: {x} + {y} = {z}")
