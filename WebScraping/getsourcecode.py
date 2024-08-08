import requests
from bs4 import BeautifulSoup


# URL of the website you want to fetch
url = 'https://technology-channel-courses.github.io/TestWebsite/'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Store the source code in a variable
    website_source = response.text
    print("Website source code fetched successfully.")
else:
    # Handle the error
    print(f"Failed to retrieve website. Status code: {response.status_code}")

# Optional: Print the first 500 characters of the source code for inspection

# Open the file in write mode
soup = BeautifulSoup(website_source, 'html.parser')
with open('WebScraping/company.txt', 'w') as file:
    # Find all table rows in the tbody
    rows = soup.find_all('tbody')[0].find_all('tr')

    for row in rows:
        # Get the first column which contains the company names
        company_name = row.find_all('td')[0].get_text(strip=True)
        file.write(company_name + '\n')

print("Company names have been saved to company.txt")