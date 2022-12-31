from csv import reader, DictReader

def Parse(filename):
	with open(filename,'r') as csv_File:
		csv_reader = DictReader(csv_File)
		for row in csv_reader:
			if int(row['Day']) == 1:
				first_month_average = (float(row['MaxT']) + float(row['MinT']))/2 
			if int(row['Day']) == 2:
				second_month_average = (float(row['MaxT']) + float(row['MinT']))/2
			if int(row['Day']) == 3:
				third_month_average = (float(row['MaxT']) + float(row['MinT']))/2
			if int(row['Day']) == 4:
				fourth_month_average = (float(row['MaxT']) + float(row['MinT']))/2
		Highest_Day_Average = max(first_month_average,second_month_average,third_month_average,fourth_month_average)
		for each in csv_reader:
			day = {}
			if float(each['MaxT'] + each['MinT']) == Highest_Day_Average:
				day['Day'] = int(each['Day'])
		print(Highest_Day_Average, day)
Parse('weather.csv')