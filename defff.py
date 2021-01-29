def add(num1: float, num2: float) -> float:
    return num1 + num2


def multiply(num1: float, num2: float) -> float:
    return num1 * num2


def run_tests():
    assert add(2, 3) == 5, "2 + 3 = 5"
    assert multiply(2, 3) == 6, "2 * 3 =6"


def main():
    def main():
        # run all the test
        print("Running tests.......")
        run_test()

        print("all the test................")

        # add 2 numbers
        x = 2
        y = 10
        z = add(x + y)
        q = multiply(x * y)

        print(f"x + y: {x} + {y} = {z}")
        print(f"x + y: {x} + {y} = {q}")

        print(f"x + y: {x} + {y} = {z}")
