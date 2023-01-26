
def highest_even(a_list):
    evens = []

    for number in a_list:
        if number % 2 == 0:
            evens.append(number)
    return max(evens)


print(highest_even([10, 2, 3, 4, 8, 11]))
