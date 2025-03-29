import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os


#Coins to get price data
coins = [
    'bitcoin',
    'ethereum',
    'bnb',
    'dogecoin',
    'xrp'
]

# Get user input for which coin to track
print("Moedas disponíveis:")
for i, coin in enumerate(coins, 1):
    print(f"{i}. {coin}")

while True:
    try:
        choice = int(input("\nSelecione uma moeda (1-5): "))
        if 1 <= choice <= len(coins):
            selected_coin = coins[choice-1]
            break
        else:
            print("Por favor, insira um número válido entre 1 e 5")
    except ValueError:
        print("Por favor, insira um número válido")

print(f"\nVocê selecionou {selected_coin}. Iniciando rastreio de preço...")

# Function to get the price and save to CSV
def get_price(selected_coin: str):
    """ Function to get the price of the coin on CoinMarketCap """

    # URL of the coin page on CoinMarketCap
    url = f"https://coinmarketcap.com/currencies/{selected_coin}/" #if dont workout, use the api from binance "https://data-api.binance.vision/api/v3/exchangeInfo?symbol=BTCUSDT"
    
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()

        # Parse HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Encontrar o span que contém o preço
        span = soup.find("span", class_="sc-65e7f566-0 WXGwg base-text", attrs={"data-test": "text-cdp-price-display"})

        if span:
            preco = span.text.strip()
            horario = datetime.now().strftime("%H:%M:%S")
            data = datetime.now().strftime("%Y-%m-%d")

            # Create db directory if it doesn't exist
            os.makedirs('db', exist_ok=True)
            
            # Save data to CSV
            with open(f'db/{selected_coin}_prices.csv', 'a') as f:
                if f.tell() == 0:  # If file is empty, write the header
                    f.write("Data,Hora,Preco\n")
                f.write(f"{data},{horario},{preco}\n")
            
            return {"moeda": selected_coin, "preco": preco, "data": data, "hora": horario}
        else:
            return {"erro": "Não foi possível encontrar o preço."}

    except requests.exceptions.RequestException as e:
        return {"erro": str(e)}

        
try:
    while True:
        print(get_price(selected_coin))
        datetime.timedelta(seconds=30).total_seconds()
except KeyboardInterrupt:
    print("Interrompido pelo usuário")
