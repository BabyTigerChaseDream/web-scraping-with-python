'''
1) example before is used for transform many tables to csv
2) if you just need transfer once :
	Selecting and copying all the content of an HTML table and pasting it into Excel or Google Docs
	will get you the CSV file you’re looking for without running a script!
	https://www.automateexcel.com/how-to/import-html-table/

'''

import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://en.wikipedia.org/wiki/'
	'Comparison_of_text_editors')
bs = BeautifulSoup(html, 'html.parser')
#The main comparison table is currently the first table on the page
table = bs.findAll('table',{'class':'wikitable'})[0]
rows = table.findAll('tr')

csvFile = open('editors.csv', 'wt+')
writer = csv.writer(csvFile)
try:
	for row in rows:
		csvRow = []
		for cell in row.findAll(['td', 'th']):
			csvRow.append(cell.get_text())
			writer.writerow(csvRow)
finally:
	csvFile.close()