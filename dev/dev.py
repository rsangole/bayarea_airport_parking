import polars as pl
import requests as re
import plotly
from bs4 import BeautifulSoup

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

gc_all = soup.find_all(class_="garageCard")

{_.find("div", class_="garageCard__title").text:_.find("div", class_="garageCard__infos__spots").text for _ in gc_all}


{
    _.find("div", class_="garageCard__title").text: _.find(
        "p", class_="garageCard__infos__spots"
    ).text
    for _ in gc_all
}