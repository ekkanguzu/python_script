from collections import OrderedDict

def count_occurrence(sentence):
	original = sentence
	counts = dict()
	words = set(sentence.split())

#	 for each in words:

#	 	counts[each] = original.count(each)

#	 return counts

	print(words)

view = count_occurrence("Python is an amazing programming language. I love coding in Python")

print(view)


# def count(filename):
# 	with open(filename, "r") as file:

# 		lines = file.readlines()

# 		for each in lines:
# 			print(each)
# 		#return my_list

# result = count("test.txt")

# print(result)