string1 = 'An IT Professional'
string_length = len(string1)
k = 6

split_length = string_length // k

result = [string1[s:s + split_length] for s in range(0, string_length, split_length)]

# for x in range(0, string_length, split_length):
#    result.append(string1[x:x + split_length])


print('Original string is: ', string1)

print('Chunked list is: ' + str(result))
