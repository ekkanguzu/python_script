
# check for duplicates in list

some_list = ['a', 'b', 'a', 'b', 'c', 'd', 'n', 'n', 'a', 'e', 'e']

duplicates = []

for each in some_list:
    if some_list.count(each) > 1:
        if each not in duplicates:
            duplicates.append(each)

print(duplicates)