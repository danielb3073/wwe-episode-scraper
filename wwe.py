from bs4 import BeautifulSoup
import requests
from datetime import datetime
import sys
import csv

user_year = sys.argv[1]

if int(user_year) < 1993:
	print("Please enter 1993 or higher (RAW started in 1993)")
	quit()
elif int(user_year) > datetime.today().year:
	print("We're not in the future yet.")
	quit()

def raw_season_calc(raw_year):
	now_year = datetime.today().year
	raw_season = (int(raw_year) - 1993) + 1
	return raw_season

def smackdown_season_calc(smackdown_year):
	now_year = datetime.today().year
	smackdown_season = (int(smackdown_year) - 1999) + 1
	return smackdown_season

def ppv(year):
	url = "https://en.wikipedia.org/wiki/List_of_WWE_pay-per-view_and_WWE_Network_events"

	response = requests.get(url)

	soup = BeautifulSoup(response.content, 'html.parser')

	h4_tags = soup.find_all('h4')

	for h4 in h4_tags:
		span = h4.find('span')
		if span and year in span.text:
			table = h4.find_next('table')
			break

	rows = get_rows(table)
	eps = []
	for row in rows:
		eps.append(["PPV", row[1].strip(), row[0].strip() + " " + year])

	return eps

def get_rows(table):
	header = []
	rows = []
	for i, row in enumerate(table.find_all('tr')):
		if i == 0:
			header = [el.text.strip() for el in row.find_all('th')]
		else:
			rows.append([el.text.strip() for el in row.find_all('td')])
	return rows

def get_eps(url):

	replace_tv_station = {
		'USA Network': '',
		'UPN': '',
		'The National Network': '',
		'SYFY': '',
		'TNN': '',
		'Spike': ''
	}

	soup = BeautifulSoup(requests.get(url).text, "html.parser")
	table = soup.find("table", class_="table")
	rows = get_rows(table)
	eps = []
	for row in rows:
		for k, v in replace_tv_station.items():
			row[2] = row[2].replace(k, v)
		eps.append([row[0].strip(), " ".join(row[1].split()).replace("\r", "").replace("\n", ""), row[2].replace(",", "").strip()])
	return eps

if int(user_year) >= 1993 and int(user_year) <= 1998:
	raw_season = get_eps("https://thetvdb.com/series/wwe-raw/seasons/official/" + str(raw_season_calc(user_year)))
	year = []
	year.extend(raw_season)
elif int(user_year) >= 1999 and int(user_year) <= 2023:
	raw_season = get_eps("https://thetvdb.com/series/wwe-raw/seasons/official/" + str(raw_season_calc(user_year)))
	smackdown_season = get_eps("https://thetvdb.com/series/wwe-smackdown/seasons/official/" + str(smackdown_season_calc(user_year)))
	year = []
	year.extend(raw_season)
	year.extend(smackdown_season)

ppv_season = ppv(str(user_year))
year.extend(ppv_season)

year_sorted = sorted(year, key=lambda x: datetime.strptime(x[2], "%B %d %Y"))

with open ('WWE_Episodes_Ordered_' + str(user_year) + '.csv', 'w', encoding='UTF-8', newline='') as f:
	writer = csv.writer(f)

	writer.writerow(["Episode", "Name", "Date"])

	for episode in year_sorted:
		#print(episode, "\r")
		writer.writerow(episode)
