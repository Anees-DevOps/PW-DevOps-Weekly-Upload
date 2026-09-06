from bs4 import BeautifulSoup
import requests

# Send a GET request to fetch page content
url = 'https://bbc.com'
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Extract all links from the page
for link in soup.find_all('a'):
    print(link.get('href'))  # Extract and print href attribute (URL)

