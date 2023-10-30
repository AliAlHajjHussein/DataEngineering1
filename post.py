import requests
import json
from bs4 import BeautifulSoup
from post_class import Post

# Send a GET request to the website
sitemap_url = 'https://www.aljazeera.com/sitemap.xml'
response = requests.get(sitemap_url)

# Parse the xml content
soup = BeautifulSoup(response.content, 'xml')

# Extract the desired information
# Example: Extract all the links on the page
locs = soup.find_all('loc')

# Create a list to store the Post objects
post_list = []

# Process each URL and create Post objects
for loc in locs:
    url = loc.text

    # Send a GET request to the website

    response = requests.get(url)

    # Parse the html content

    soup = BeautifulSoup(response.content, 'xml')

    links = soup.find_all('url')

    for link in links:
        loc = link.find('loc')

        # Send a GET request to the website

        response = requests.get(loc.text)

        # Parse the html content

        soup = BeautifulSoup(response.content, 'html.parser')

        news_element = soup.find('div', class_='breadcrumbs')

        if news_element:
            # Extract the title
            title_element = soup.find('h1')
            title = title_element.text if title_element else None

            # Extract the author
            author_element = soup.find('div', class_='article-b-l')
            author = author_element.text if author_element else None

            # Extract the date
            date_element = soup.find('div', class_='article-info-block css-ti04u9')
            date = date_element.text if date_element else None
            # Extract the source
            source_element = soup.find('div', class_='article-source')
            source = source_element.text if source_element else None

            # Create a Post object with the extracted data
            post = Post(title=title, author=author, date=date, source=source)
            # Append the Post object to the post_list
            post_list.append(post)

    # Convert the Post objects to a list of dictionaries
    post_data = []
    for post in post_list:
        post_data.append({
            'title': post.title,
            'author': post.author,
            'date': post.date,
            'source': post.source
        })

    # Save the post_data to a JSON file
    with open('output2.json', 'w') as file:
        json.dump(post_data, file, indent=4)

