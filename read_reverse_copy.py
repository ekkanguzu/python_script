"""
Write a function called copy, 
which takes in a file name and a new file name 
and copies the contents of the first file to the second file. 

(Note: we've provided you with the first 
chapter of Alice's Adventures in Wonderland 
to give you some sample text to work with. 
This is also the text used in the tests.
"""

def copy(filename, new_file):
	""" 
	This script reads from a file, reverses the wrods then copies the content to a new file.
	"""
	print(copy.__doc__)

	with open(f"C:\\Users\\ekanguzu\\Desktop\\Eric's Code\\{filename}", "r", encoding="utf8") as input_file:
		with open(f"C:\\Users\\ekanguzu\\Desktop\\Eric's Code\\{new_file}", "w") as output_file:

			file = input_file.read()

			output_file.write(file[::-1])


copy("story.txt", "story_copy.txt")