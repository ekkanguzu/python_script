'''
#This is a csv type of file.
#example: teams.csv

Team,Games,Wins,Losses,Draws,Goals For,Goals Against
Arsenal,38,22,13,3,61,48
Liverpool,38,28,2,8,94,26
Chelsea,38,21,6,11,76,33
Tottenham,38,22,11,5,69,40
Man City,38,29,3,6,99,26
Man United,38,16,12,10,57,57
Wolves,38,15,17,6,38,43
West Ham,38,16,14,8,60,51
Newcastle,38,13,15,10,44,62
'''
from csv import reader, DictReader

def ParseCSV(filename):
	with open(filename, 'r') as csv_file:
		csv_reader = DictReader(csv_file)
		my_Goals_For = []
		my_Goals_Against = []
		for row in csv_reader:
			my_Goals_For.append(int(row['Goals For']))
			my_Goals_Against.append(int(row['Goals Against']))
			if (int(row['Goals For']) == min(my_Goals_For)):
				my_Smallest_Goals_Team = row['Team']
			if int(row['Goals Against']) == min(my_Goals_Against):
				my_Smallest_Against_Team = row['Team']

		print(f"The team with the smallest 'Goals For' difference is {my_Smallest_Goals_Team}.\n")
		print(f"The team with the smallest 'Goals Against' difference is {my_Smallest_Against_Team}.")

ParseCSV('teams.csv')