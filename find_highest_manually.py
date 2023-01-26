def find_highest_manually(numbers):
    highest_number = 0
    for each in numbers:
        if each > highest_number:
            highest_number = each

    return highest_number


a_list = [1, 100, 200, 500, 50, 20, 15, 30, 25, 80, 60, 77, 88, 44, 13, 89, 58, 99, -1]

print(find_highest_manually(a_list))
