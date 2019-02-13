import xlsxwriter
import datetime
import json

workbook = xlsxwriter.Workbook('Trend_Data.xlsx')
worksheet = workbook.add_worksheet()

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

excel_rows = []

with open("Genre_Analysis//result.json", "r") as read_file:
	dataset = json.load(read_file)
	for year in dataset.keys():
		if int(year) > 1919:
			for genre in dataset[year]:
				if genre in top_5_genre:
					genre_percentage = dataset[year][genre]
					excel_rows.append([year, genre, genre_percentage])

print(excel_rows)

# Start from the first cell. Rows and columns are zero indexed.
row = 0
col = 0

# Iterate over the data and write it out row by row.
worksheet.write(row, 0, 'Year')
worksheet.write(row, 1, 'Genre')
worksheet.write(row, 2, 'Genre_percentage')
row += 1

col = 0

for year, genre, genre_percentage in excel_rows:
    worksheet.write(row, col, year)
    worksheet.write(row, col + 1, genre)
    worksheet.write(row, col + 2, genre_percentage)
    row += 1

workbook.close()