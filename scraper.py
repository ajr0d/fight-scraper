import requests
from bs4 import BeautifulSoup

URL = "https://www.ufc.com/rankings/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

rankings_table = soup.find(class_="views-table")

rankings_text = rankings_table.find_all("div", class_="views-row")

print("## Men's Pound-For-Pound Top Rank:")
ranking_num = 0
for ranking in rankings_text:
    ranking_num +=1
    name = ranking.find("a")
    ranking_name = name.text.strip()
    print(str(ranking_num) + " " + ranking_name)
