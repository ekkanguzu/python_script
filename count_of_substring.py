"""
Write a program to find how many times substring “Emma” appears in the given string.

Given:

str_x = "Emma is good developer. Emma is a writer"

Expected Output:

Emma appeared 2 times
"""

def count_words(string):
    my_list = string.split()
    my_dict = {word: my_list.count(word) for word in my_list}
    for k,v in my_dict.items():
        if k == "Emma":
            return f"{k} appeared {v} times"
            
str_x = "Emma is a good developer. Emma is a writer"
print(count_words(str_x))