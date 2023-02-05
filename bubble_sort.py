
def bubble_sort(elements):
    size = len(elements)
    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                elements[j], elements[j+1] = elements[j+1], elements[j]
                swapped = True

        if not swapped:
            break


if __name__ == '__main__':
    elements_1 = [5, 9, 2, 1, 67, 34, 88, 34]
    elements_2 = [1, 2, 3, 4, 5]

    bubble_sort(elements_1)
    bubble_sort(elements_2)

    print()
    print(elements_1)
    print()
    print(elements_2)
