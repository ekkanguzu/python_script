
my_list = [1, 5, -2, -8, -6, 10, 8, 0, 0, 26, -20, +40, -14, 80, 100]

def plusMinus(parameter):
	"""
	This function takes in a list of numbers then counts occurences of each number. 
	Example [-1,-3,2,4,0] would output 2 negative numbers, one zero and two positive numbers.
	"""
	positive = 0
	negative = 0
	zero = 0

	for each in parameter:
		if each > 0:
			positive += 1
		elif each == 0:
			zero += 1
		else:
			negative += 1
		
	print(f"Positive: {positive}")
	print(f"Negative: {negative}")
	print(f"Zero: {zero}")

#plusMinus(my_list)

if __name__ == "__main__":
	plusMinus() #Pass an argument
