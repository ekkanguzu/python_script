# make sure array is sorted
# find low of the array
# find high of the array
# find middle: (low + high) / 2
# if array[mid] == x, return mid
# if array[mid] < x, low = mid + 1
# if array[mid] > x high = mid - 1
def binary_search(array, number_to_search):
    array.sort()

    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2

        if array[mid] == number_to_search:
            return mid

        elif array[mid] < number_to_search:
            low = mid + 1

        else:
            high = mid - 1

    return -1


result = binary_search([3, 4, 5, 6, 7, 8, 9], 8)

if result != -1:
    print(f'Number is found at index: {result}')
else:
    print('Not found')
