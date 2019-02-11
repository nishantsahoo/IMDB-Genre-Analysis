import json
import datetime
import pprint
import string
import sys
pp = pprint.PrettyPrinter(indent=4)

def main(): # Main function

	current_year = int(datetime.datetime.now().year)
	genre_list = []
	for year in range(1898, current_year+1):
		with open("Datasets//IMDB_Top_50_Genre_" + str(year) + ".json", "r") as read_file:
		    data = json.load(read_file)
		    genre_list += data[str(year)]

	genre_list = list(set(genre_list))

	unique_genre_list = list(set(genre_list))

	print(unique_genre_list)

	percentage_dict_year = {}
	for year in range(1898, current_year+1):
		percentage_dict = {}
		genre_list = []
		with open("Datasets//IMDB_Top_50_Genre_" + str(year) + ".json", "r") as read_file:
		    data = json.load(read_file)
		    genre_list += data[str(year)]		

		if genre_list != []:
			for genre in unique_genre_list:
				percentage_dict[genre] = genre_list.count(genre)/len(genre_list)

			percentage_dict_year[year] = percentage_dict

	pp.pprint(percentage_dict_year)

	sys.stdout = open('Genre_Analysis//result.json', 'w')
	print(json.dumps(percentage_dict_year, indent=4))

	# End of the main function


main() # main function