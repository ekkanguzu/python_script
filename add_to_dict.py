
# This code take strings from the list, split, then create a dictionary with them
names = ['Eric Kanguzu', 'Broskii Clapper', 'Yessir Skii']

a_dict = {}

for name in names:
    new_arr = name.split()

    a_dict[new_arr[0]] = new_arr[1]

print(a_dict)
