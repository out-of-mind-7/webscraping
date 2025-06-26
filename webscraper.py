import requests
from bs4 import BeautifulSoup

url = "https://timesofindia.indiatimes.com/home/headlines"
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

headlines = soup.find_all('h2')

with open('news_headlines.txt', 'w', encoding='utf-8') as file:
    for i, h in enumerate(headlines, 1):
        title = h.get_text(strip=True)
        if title:
            file.write(f"{i}. {title}\n")

print("Headlines saved to 'news_headlines.txt'")
