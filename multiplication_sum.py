"""
Calculate the multiplication and sum of two numbers

Given two integer numbers return their product only if the product is equal to 
or lower than 1000, else return their sum.
"""

def multiplication_sum(number1, number2):
	product = number1*number2
	if product <= 1000:
		return product
	else:
		return number1+number2

number1 = int(input("Type your first number: "))
number2 = int(input("Type your second number: "))
print(multiplication_sum(number1, number2))