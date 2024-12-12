import re
import polars as pl
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pytz
import os

# Fetch the content of the webpage
response = requests.get("https://www.flysfo.com/passengers/parking")

# Parse the content with BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all elements with the class 'garageCard'
gc_all = soup.find_all(class_="garageCard")

# Get the current date and time in PST
pst = pytz.timezone("US/Pacific")
current_time_pst = datetime.now(pst)
current_date = current_time_pst.strftime("%Y-%m-%d")
current_time = current_time_pst.strftime("%H:%M:%S")

# Create a DataFrame with the extracted data
df = pl.DataFrame(
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
        "date": [current_date for _ in gc_all],
        "time": [current_time for _ in gc_all],
    }
)

# Append the data to a CSV file
csv_file = "data.csv"
if os.path.exists(csv_file):
    df.write_csv(csv_file, mode="a", has_header=False)
else:
    df.write_csv(csv_file)
