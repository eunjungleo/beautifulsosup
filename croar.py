import requests # import requests
from bs4 import BeautifulSoup #import bs4 
import csv # import csv


html = requests.get("https://www.billboard.com/charts/hot-100").text  # parse web page DOM into text
soup = BeautifulSoup(html, 'lxml') # parse html using lxml

#rank
rank = soup.select(".chart-element__rank__number")
#song title
title = soup.select(".chart-element__information__song")
#artist
artist = soup.select(".chart-element__information__artist")


# csv
with open("croar_data.csv", mode="w") as croar:
    writer = csv.writer(croar)
    writer.writerow(["rank", "songtitle","artist"])

    for list in zip(rank, title, artist):
        rank = list[0].text
        songtitle = list[1].text
        artist = list[2].text

        writer.writerow([rank, songtitle, artist])


    