import csv

import requests
from bs4 import BeautifulSoup

source = requests.get("https://coreyms.com").text

soup = BeautifulSoup(source, 'lxml')

with open("cms_scrape.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter="¥")
    csv_writer.writerow(["headline", "summary", "video-link"])

    for article in soup.find_all("article"):
        headline = article.h2.a.text
        print(headline)

        summary = article.find("div", class_="entry-content").p.text
        print(summary)

        try:
            vid_src = article.find("iframe", class_="youtube-player")["src"]
            vid_id, _ = vid_src.split("/")[4].split("?")
            vid_link = f"https://www.youtube.com/watch?v={vid_id}"
        except TypeError as e:
            vid_link = None

        print(vid_link)
        print()

        csv_writer.writerow([headline, summary, vid_link])
