a_string = input('Enter a word or sentence: ')

a_string = a_string.casefold()

vowels = 'aeiou'

vowels_data = {}.fromkeys(vowels, 0)
total_vowels = 0

for character in a_string:
    if character in vowels:
        vowels_data[character] += 1
        total_vowels += 1

print('Total vowels: ', total_vowels)
for vowel in vowels_data:
    print(vowel, ' => ', vowels_data[vowel])
