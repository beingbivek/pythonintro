import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

# URL of the IMDb Top 250 page
url = 'https://www.imdb.com/chart/top/'

# User-Agent header to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Send a GET request to the website with headers
response = requests.get(url, headers=headers)
response.raise_for_status()  # Check if the request was successful

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Find the JSON data within the <script type="application/ld+json"> tag
json_data = soup.find('script', type='application/ld+json').string

# Load the JSON data
data = json.loads(json_data)

# Initialize lists to hold the data
ranks = []
titles = []
years = []

# Extract movie details
for index, movie in enumerate(data['itemListElement'], start=1):
    ranks.append(index)
    titles.append(movie['item']['name'])
    years.append(movie['item']['url'].split('/')[-2])  # Extracting year from the URL

# Create a DataFrame
df = pd.DataFrame({
    'Rank': ranks,
    'Movie Name': titles,
    'Year': years
})

# Save DataFrame to CSV file
df.to_csv('WebScraping/movies.csv', index=False)

print('Movies have been saved to movies.csv')