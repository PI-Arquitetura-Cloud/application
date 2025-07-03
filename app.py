from flask import Flask, jsonify, render_template
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

# Coins to get price data
coins = [
    'bitcoin',
    'ethereum',
    'bnb',
    'dogecoin',
    'xrp',
    'solana',
    'cardano',
    'litecoin'
    
]

def get_price(selected_coin: str):
    """ Function to get the price of the coin on CoinMarketCap """
    url = f"https://coinmarketcap.com/currencies/{selected_coin}/"
    
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        span = soup.find("span", attrs={"data-test": "text-cdp-price-display"})
        

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

@app.route('/')
def index():
    return render_template('index.html', coins=coins)

@app.route('/price/<coin>')
def get_coin_price(coin):
    if coin not in coins:
        return jsonify({"erro": "Moeda não encontrada"}), 404
    return jsonify(get_price(coin))

if __name__ == '__main__':
    app.run(debug=True) 