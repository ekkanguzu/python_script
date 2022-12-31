
number = 100

from_user = int(input("Type a number: "))

print(f"You typed {from_user}")

match from_user:
	case 100:
		print(f"yes, that matches my number which is {number}")
	case 200:
		print(f"No, that doesn't match {number} because you typed {from_user}")
	case _:
		print(f"I don't think you typed a number that I currently have in store.")