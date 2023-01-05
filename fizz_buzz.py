# If number is divisible by 3, returns Fizz
# If number is divisible by 5, return Buzz
# If number is divisible by both 3 and 5, return FizzBuzz
# If number is not divisible by both 3 and 5, return number

def fizz_buzz(input_):
    if input_ % 3 == 0 and input_ % 5 == 0:
        return 'FizzBuzz'
    if input_ % 3 == 0:
        return 'Fizz'
    if input_ % 5 == 0:
        return 'Buzz'
    return input_

print(fizz_buzz(15))