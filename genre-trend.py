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

	with open("Genre_Analysis//result.json", "r") as read_file:
		data = json.load(read_file)
	
	final_genre_percentage = {}
	for genre in unique_genre_list:
		final_genre_percentage[genre] = 0

	for genre in unique_genre_list:
		for year in data.keys():
			final_genre_percentage[genre] += data[str(year)][genre]

	sorted_genre = []

	for genre in sorted(final_genre_percentage, key=final_genre_percentage.get, reverse=True):
		sorted_genre += [genre]

	top_5_genre = sorted_genre[:5]
	cnt = 1
	print('Top 5 genres from 1898-2019:')
	for genre in top_5_genre:
		print(str(cnt) + '. ' + genre)
		cnt += 1

	# End of main function


main() # Main function