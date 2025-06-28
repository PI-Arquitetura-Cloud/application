import requests

from bs4 import BeautifulSoup

url = 'https://coinmarketcap.com/currencies/ethereum'
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
span = soup.find("span", class_="sc-65e7f566-0 esyGGG base-text", attrs={"data-test": "text-cdp-price-display"})
print(span)
if span:
    preco = span.text.strip()
    print(preco)