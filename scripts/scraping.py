from datetime import datetime
import json
import os
from rss_feeds_scraper.scrap import fetch_rss_data
from rss_feeds_scraper.model import Data

urls = ["https://www.df.cl/noticias/site/list/port/rss.xml",
        "https://www.theclinic.cl/feed/",
        "https://www.cooperativa.cl/noticias/site/tax/port/all/rss____1.xml"]

data = []

for url in urls:
    fd = fetch_rss_data(url)
    data.append(fd)

d = Data(
    feeds = data
)

json_data = d.model_dump_json()
today_date = datetime.now().strftime("%Y-%m-%d")
directory_path = f"data/"
file_path = os.path.join(directory_path, f"{today_date}.json")

with open(file_path, "w") as file:
    file.write(json_data)