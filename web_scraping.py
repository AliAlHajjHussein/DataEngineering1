import requests
import json
from bs4 import BeautifulSoup

#Send a GET request to the website
url = 'https://www.aljazeera.com/sitemap.xml?yyyy=2023&mm=10&dd=18'
response = requests.get(url)

#Parse the HTML content
soup = BeautifulSoup(response.content, 'xml')

#Extract the desired information
#Example: Extract all the links on the page
links = soup.find_all('url')

#Create a list to store the links
link_list = []
for url in links:
    loc = url.find('loc')
    if loc:
        if 'gaza' in loc.text:
            link_list.append(loc.text)

#Save the links to a JSON file
with open('output.json', 'w') as file:
    json.dump(link_list, file, indent=4)

