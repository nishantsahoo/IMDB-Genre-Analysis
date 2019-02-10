from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import datetime
import pprint
import sys
pp = pprint.PrettyPrinter(indent=4)

def main(): # Main function
	current_year = int(datetime.datetime.now().year)
	for year in range(1898, current_year+1):
		sys.stdout = open('DataSets//IMDB_Top_50_Genre_' + str(year) + '.json', 'w')
		url = "http://www.imdb.com/search/title?release_date=" + str(year) + "," + str(year) + "&title_type=feature"
		html = urlopen(url)
		soup = BeautifulSoup(html.read(), features="html.parser")
		dataset_top50 = {}
		id = 1
		movies_list = soup.findAll('div', attrs={'class': 'lister-item-content'})
		genre = []
		for each in movies_list:
			p_list = each.findAll('p')

			if p_list[0]:
				if p_list[0].find('span', attrs={'class': 'genre'}):
					genre_value = p_list[0].find('span', attrs={'class': 'genre'}).text.strip()
					genre_value = genre_value.split(",")
					for i in range(0, len(genre_value)):
						genre_value[i] = genre_value[i].strip()
					genre += genre_value

			id += 1

		dataset_top50[year] = genre

		pp.pprint(dataset_top50)
		print(json.dumps(dataset_top50, indent=4))

	# End of the main function


main() # Call of the main function