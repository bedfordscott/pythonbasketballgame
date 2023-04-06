import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.nba.com/players"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find the table with player data
table = soup.find_all("table", {"class": "players-list__table"})[0]

# Create a list of dictionaries containing player information
player_data = []
for row in table.find_all("tr"):
    data = {}
    cols = row.find_all("td")
    if len(cols) > 0:
        data["Name"] = cols[0].get_text()
        data["Team"] = cols[1].get_text()
        data["Position"] = cols[2].get_text()
        data["Stats"] = cols[3].get_text()
        player_data.append(data)

# Create a pandas DataFrame from the player data
df = pd.DataFrame(player_data)
