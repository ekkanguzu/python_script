"""
Counting syllables
Define a function named count that takes a single parameter. The parameter is a string. The string will contain a single word divided into syllables by hyphens, such as these:

"ho-tel"
"cat"
"met-a-phor"
"ter-min-a-tor"
Your function should count the number of syllables and return it.

For example, the call count("ho-tel") should return 2.
"""

#Eric's own code
def count(param):
    new = param.split("-")
    count = 0
    for each in new:
        count+=1
    return count

#Other sources
    # def count(word):
    #     syllables = 1
    #     for letter in word:
    #         if letter == "-":
    #             syllables = syllables + 1
    #     return syllables

# using the count method
    # def count(word):
    #     return word.count("-") + 1

# # using split
    # def count(word):
    #     return len(word.split("-"))