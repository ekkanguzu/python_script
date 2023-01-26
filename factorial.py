# Complete the factorial() function. It should calculate the factorial of a number.
# A factorial of a number is the product of all positive integers less than or equal to that number.
# For example:
# 4! = 4 * 3 * 2 * 1 = 24

def factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial


# don't touch above this line


def test(num):
    fact = factorial(num)
    print(f"The factorial of {num} is {fact}")


test(0)
test(4)
test(5)
test(7)
test(9)
test(13)
test(15)
test(14)
