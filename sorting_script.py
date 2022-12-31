#This script takes in a list as an argument then sorts and counts each occurence

def count_sort(l):
    my_set = set(l)

    my_new_set = sorted(list(my_set), reverse=True)

    for each in my_new_set:

        print(str(each) + ":", l.count(each))