import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape_nfl_player_stats(url):
    response = requests.get(url)

    # Check if request is successful
    if response.status_code == 200:
        # Parse HTML content with Beautiful Soup 
        soup = BeautifulSoup(response.text, 'html.parser')

        # Locate data table with its ID (for rushing stats)
        table = soup.find('table', {'id': 'rushing'})

        # Extract column headers from <thead> and skip the first row
        headers = [th.text.strip() for th in table.find('thead').find_all('tr')[1].find_all('th')]

        # Extract row data from <tbody>
        rows = table.find('tbody').find_all('tr')

        # Prepare a list for row data
        data = []
        for row in rows:
            # Skip sub-header or irrelevant rows by checking for 'thead' class or empty rows
            if 'class' in row.attrs and 'thead' in row.attrs['class']:
                continue
            if row.find('td') is None:
                continue

            # Extract text from each cell in the row
            row_data = [td.text.strip() for td in row.find_all(['th', 'td'])]

            # Append row data to the list
            data.append(row_data)

        # Convert the data into a pandas DataFrame
        df = pd.DataFrame(data, columns=headers)

        print("Data and stats from Pro Football Reference (https://www.pro-football-reference.com/years/2024/rushing.htm)")

        return df

    else:
        # Print error message if the request fails
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None


df = scrape_nfl_player_stats("https://www.pro-football-reference.com/years/2024/rushing.htm")
print(df)
