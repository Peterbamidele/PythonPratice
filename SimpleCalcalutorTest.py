from SimpleCalcalutor import *


def run_tests():
    """"test all the function"""
    assert add(2, 3) == 5, "2 + 3 is 5"
    assert multiply(2, 3) == 6, "2 * 3 is 6"
    assert subtract(2, 3) == 1, "2 - 3 is -1"
    assert divide(6, 3) == 2, "6 / 3 is 2"
    assert square_root(9) == 3, "square root of 9 is 3"
    assert square(2) == 4, "square 0f 2 is 4"


if __name__ == "__main__":
    run_tests()
