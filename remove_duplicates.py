data = [10, 20, 30, 30, 40, 50, 50, 60, 70]


# This program removes duplicates and returns a new list with unique items
def remove_duplicates(dup_list):
    no_dup_list = []
    for element in dup_list:
        if element not in no_dup_list:
            no_dup_list.append(element)

    return no_dup_list


result = remove_duplicates(data)

print(result)
