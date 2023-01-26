from functools import reduce

# 1 Capitalize all pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def capitalize_names(li):
    return li.upper()


print(list(map(capitalize_names, my_pets)))

# 2 Zip the 2 lists into a list of tuples,
# but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

print(list(zip(my_strings, sorted(my_numbers))))

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def filter_it(li):
    return li > 50


print(list(filter(filter_it, scores)))


# 4 Combine all numbers that are in a list on this file
# using reduce (my_numbers and scores). What is the total?
def reduce_it(acc, item):
    print(acc, item)
    return acc + item


print(reduce(reduce_it, my_numbers, 0))
