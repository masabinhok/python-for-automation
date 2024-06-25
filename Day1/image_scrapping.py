from bs4 import BeautifulSoup
import requests
import os

# declaring the url
url = "https://pcampus.edu.np/"

# sending request to the url
response = requests.get(url)

# parsing HTML
soup = BeautifulSoup(response.content, 'html.parser')

# directory to save images
os.makedirs('images', exist_ok=True)

image_tags = soup.find_all('img')

i = 1

for image in image_tags:
    # get the image link (src attribute)
    image_link = image.get('src')

    # handle relative URLs
    if image_link.startswith('http'):
        image_data = requests.get(image_link).content

        with open(f'images/image_{i}.jpg', 'wb') as file:
            file.write(image_data)

    i += 1

print("Images downloaded successfully.")

    # request the image data
    
    # save the image data to a file
    
