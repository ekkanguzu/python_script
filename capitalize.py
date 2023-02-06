# This program capitalizes each first letter of a string
def capitalize(s):
    for i in s.split():
        s = s.replace(i, i.capitalize())
    return s

    # return s.title()

    # s.casefold()
    # split = s.split()
    # new = []
    # for i in split:
    #     new.append(i.title())
    # return ' '.join(new)


if __name__ == '__main__':
    print()
    name = input('Enter a name to be capitalized by first letter: ')
    result = capitalize(name)
    print()
    print(f'Your name capitalized by first letter is: {result}')
