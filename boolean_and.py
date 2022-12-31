"""
Boolean and
Define a function named triple_and that takes three parameters and returns True only if they are all True and False otherwise.
"""

def triple_and(param1, param2, param3):
    compare = True
    for each in [param1, param2, param3]:
        if compare != each:
            compare = False
            break
        else:
            compare = True
    return compare

#Another solution
def triple_and(a, b, c):
    return a and b and c