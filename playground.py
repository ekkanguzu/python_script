#User's input pseudocode
first_name1 = input("Please type your first name: ")
last_name1 = input("Please type your lastname: ")

first_name2 = input("Please type a second first name: ")
last_name2 = input("Please type a second lastname: ")

#Bob Alice Cat Dog
#First two letters of your second firstname
#replaces the first letter of your previous firstname
#First two letters of your second lastname
#replaces the first letter of your previous lastname

final_firstname = first_name2[0:2] + first_name1[1:]
final_lastname = last_name2[0:2] + last_name1[2:]

#This code prints your old name
print(f"Your old name was {first_name1} {last_name1}")
print(f"And your new name is {final_firstname} {final_lastname}")