from csv import *

with open("status.csv", "r") as file:
	with open("C:\\Users\\ekanguzu\\Desktop\\Eric's Code\\result.csv", "w", newline="") as myOutput:

		myfile = DictReader(file)
		result = sorted(myfile, key=lambda d: int(d["output bps"]), reverse=True)
		fieldname = ["host", "port", "input bps", "output bps"]
		
		csvWriter = DictWriter(myOutput, fieldnames= fieldname)

		csvWriter.writeheader()
		csvWriter.writerows(result)


print(myOutput.closed)

#for each in result:
#	print(each)