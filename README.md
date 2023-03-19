# wwe-episode-scraper
A python script that scrapes a list of RAW, SmackDown, and PPV episodes for any given year.

To use the script, you'll need to have Python3 and pip installed.
I'm using `Python 3.8.2` and `pip 23.0.1`

1. Open a command prompt/terminal and navigate to the folder with the script and requirements.txt
2. Run the command `pip install -r requirements.txt`
3. Run the script with `python wwe.py <year>` where `<year>` is the year of WWE you want to scrape.

The script will grab all RAW, SmackDown and PPVs for that year, sort them into a list by aired date, and spit it out into a `.csv` file.

Example of the output:
![image](https://user-images.githubusercontent.com/58257152/226156907-1caec782-bfaa-4469-b460-2876889adc46.png)

Sources: 
- RAW episodes - https://thetvdb.com/series/wwe-raw
- SmackDown episodes - https://thetvdb.com/series/wwe-smackdown
- PPVs - https://en.wikipedia.org/wiki/List_of_WWE_pay-per-view_and_WWE_Network_events
