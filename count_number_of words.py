"""
Write a function called statistics, 
which takes in a file name and returns 
a dictionary with the number of lines, 
words, and characters in the file.

"""
def statistics(filename):
	"""
		This script takes in a filename then counts the number of lines, words, and characters.
	"""

	with open(filename, "r", encoding="utf8") as input_file:

		lines = input_file.readlines()

		return {"lines": len(lines), "words": sum(len(line.split(" ")) for line in lines),

				"characters": sum(len(line)for line in lines)}


result = statistics("test.txt")

print(result)
