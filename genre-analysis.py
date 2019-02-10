import json
import datetime
import pprint
import sys
pp = pprint.PrettyPrinter(indent=4)

def main(): # Main function

	current_year = int(datetime.datetime.now().year)
	genre_list = []
	for year in range(1898, current_year+1):
		with open("Datasets//IMDB_Top_50_Genre_" + str(year) + ".json", "r") as read_file:
		    data = json.load(read_file)
		    genre_list += data[str(year)]
		    # print(str(year))
		    # print(data[str(year)])

	genre_list = list(set(genre_list))
	unique_genre_list = []
	for each in genre_list:
		unique_genre_list += each.split(',')

	print(list(set(unique_genre_list)))


main() # main function