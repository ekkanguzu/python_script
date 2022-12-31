"""
All equal
Define a function named all_equal that takes a list and checks whether all elements in the list are the same.

For example, calling all_equal([1, 1, 1]) should return True.
"""

def all_equal(aList):
    first_element = aList[0]
    result = True
    for each in aList:
        if first_element != each:
            result = False
            break
        else:
            result = True
    return result