def linear_search(numbers_list, number_to_find):
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index
    return -1


if __name__ == '__main__':
    numbers_list = [13, 16, 19, 21, 25, 30, 45, 89]
    number_to_find = 89

    index = linear_search(numbers_list, number_to_find)
    print(f'Number found at index {index} using linear search')