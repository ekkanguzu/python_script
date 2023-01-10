# this program takes a string
# changes its character from uppercase to lowercase or vice versa
# then swaps the order and returns a string
# 'rUns dOg' returns 'RuNS DoG'

def reverse_words_order_and_swap_cases(sentence):
    new_string = ''

    for s in sentence:
        if s == s.upper():
            new_string += s.lower()
        if s == s.lower():
            new_string += s.upper()

    a_list = new_string.split()
    final_list = []

    for word in a_list:
        final_list.insert(0, word)

    final_string = ' '.join(final_list)

    # return new_string
    # return a_list
    return final_string

print(reverse_words_order_and_swap_cases('rUns dOg'))