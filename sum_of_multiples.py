
# If we list all the natural numbers below
# that are multiples of 3 or 5, we get 3,5,6 and 9
# The sum of these multiples is 23
# Find the sum of all the multiples of 3 or 5

def sum_multiple(number):

    # List comprehension
    new_list = [num for num in range(1, number) if num % 3 == 0 or num % 5 == 0]

#    for num in range(1, number):
#        if num % 3 == 0 or num % 5 == 0:
#            new_list = new_list + [num]

    return sum(new_list)

print(sum_multiple(100))
