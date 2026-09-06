import requests

# Fetch the HTML content of the BBC homepage
url = 'https://bbc.com'
response = requests.get(url)

# Check for successful request
if response.status_code == 200:
    print("Webpage fetched successfully!")
else:
    print("Failed to retrieve webpage.")

# Print HTML content
print(response.text)
