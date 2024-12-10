import re
import polars as pl
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pytz

response = requests.get("https://www.flysfo.com/passengers/parking")
soup = BeautifulSoup(response.content, "html.parser")
print(soup.prettify())


gc = soup.find(class_="garageCard")

type(gc)
gc.attrs
gc.text

garage_card_title = gc.find("div", class_="garageCard__title")
garage_card_title.text

gc.find("div", class_="garageCard__infos")
gc.find("text", class_="percentage")

gc_all = soup.find_all(class_="garageCard")

pl.DataFrame(
    {
        "garage": [_.find("div", class_="garageCard__title").text for _ in gc_all],
        "spots": [
            int(
                re.search(
                    r"\d+", _.find("p", class_="garageCard__infos__spots").text.strip()
                ).group()
            )
            for _ in gc_all
        ],
        "occupancy": [
            int(
                re.search(
                    r"\d+", _.find("text", class_="percentage").text.strip()
                ).group()
            )
            for _ in gc_all
        ],
    }
)
