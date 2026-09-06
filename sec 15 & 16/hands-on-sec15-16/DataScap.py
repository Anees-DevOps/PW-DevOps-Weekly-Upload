import os
import requests
import csv
from bs4 import BeautifulSoup


# Define your custom directory path
custom_path = '<Your-desired-path>/articles.csv'


# Ensure the folder exists (if not, create it)
os.makedirs(os.path.dirname(custom_path), exist_ok=True)


# Send a GET request to the website
url = 'https://cnn.com'
response = requests.get(url)


# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')


# Open the CSV file at the custom path to write the data
with open(custom_path, 'w', newline='') as file:
   writer = csv.writer(file)


   # Write the CSV header
   writer.writerow(['Title', 'Link'])


   # Find article titles and links
   articles = soup.find_all('a', href=True)  # Find all <a> tags with a href attribute


   # Loop through each article and extract the title and link
   for article in articles:
       title = article.get_text(strip=True)  # Get the text of the title
       link = article['href']  # Get the href attribute (URL)


       # Ensure full URL if the link is relative
       if link.startswith('/'):
           link = 'https://bbc.com' + link


       # Only save articles that contain a link (optional check to exclude unrelated links)
       if title and link:
           writer.writerow([title, link])


# Confirm the file is saved
print(f"Data saved to {custom_path}")
