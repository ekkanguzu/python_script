
def mutate_string(string, position, character):
    mutate = string[0: position] + character + string[position+1:]
    return mutate

if __name__ == '__main__':
    a_string = input()
    index, c = input().split()
    new_string = mutate_string(a_string, int(index), c)
    print(new_string)