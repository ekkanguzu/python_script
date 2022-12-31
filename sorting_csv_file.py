from csv import *

with open("filename", "r") as names: #### Type file name inside quotation mark (example: filename.txt)
	
	with open("C:\\Users\\ekanguzu\\Desktop\\Eric's Code\\sorted.csv", "w", newline="") as sortedNames:

		csv_names = DictReader(names)

		sortedThem = sorted(csv_names, lambda d: d["firstname"])

		field = ["firstname", "lastname"]

		csv_writer = DictWriter(sortedNames, fieldnames=field)

		csv_writer.writeheader()

		csv_writer.writerows(sortedThem)

#for each in names:
#		print(each)

#for each in sortedThem:
#	print(each)