# Fill in the loop with code that prints the indexes where the items in the arrays differ.
# For example, if the arrays are:
# old_character_levels = [2, 5, 3, 7, 5]
# new_character_levels = [2, 5, 19, 7, 8]
# Then your code should print:
# 2
# 4

old_character_levels = [6, 4, 3, 7, 7, 7, 2, 7, 2, 6, 5, 1, 2, 4, 6, 6, 1, 4, 4, 1, 1, 5, 4, 3, 2, 0, 5, 5, 6, 1, 6, 2,
                        1, 2, 3, 1, 7, 7, 2, 0, 0, 6, 2, 6, 8, 5, 3, 1, 6, 3, 0, 5, 1, 3, 3, 0, 2, 8, 3, 0, 3, 5, 7, 3,
                        1, 4, 5, 0, 0, 1, 7, 0, 6, 1, 0, 2, 0, 0, 8, 6, 0, 0, 1, 4, 0, 7, 8, 2, 7, 8, 7, 4, 8, 6, 0, 3,
                        1, 4, 6, 4, 2, 2, 5, 8, 1, 5, 1, 8, 0, 6, 6, 3, 0, 2, 4, 7, 0, 6, 7, 6, 3, 1, 1, 5, 2]
new_character_levels = [6, 4, 3, 7, 7, 7, 2, 7, 2, 6, 5, 1, 2, 4, 5, 6, 1, 4, 4, 1, 1, 5, 4, 3, 2, 1, 2, 5, 6, 1, 6, 2,
                        1, 2, 3, 1, 7, 7, 2, 0, 0, 6, 2, 6, 8, 5, 3, 1, 6, 3, 0, 5, 1, 3, 3, 0, 2, 8, 3, 0, 3, 5, 7, 3,
                        1, 4, 5, 0, 0, 1, 7, 0, 6, 1, 0, 2, 0, 0, 8, 6, 0, 0, 1, 4, 0, 7, 8, 2, 7, 8, 7, 4, 9, 6, 0, 3,
                        3, 4, 6, 4, 2, 2, 5, 8, 1, 5, 1, 8, 0, 6, 6, 3, 0, 2, 4, 7, 0, 6, 7, 6, 3, 1, 8, 5, 2]

# don't touch above this line

for i in range(0, len(old_character_levels)):
    if old_character_levels[i] != new_character_levels[i]:
        print(i)
