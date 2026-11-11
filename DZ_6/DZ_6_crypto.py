from datetime import datetime

import requests

# Список популярных криптовалют (ID CoinGecko : Название)
crypto_currencies = {
    'bitcoin': 'Bitcoin (BTC)',
    'ethereum': 'Ethereum (ETH)',
    'tether': 'Tether (USDT)',
    'usd-coin': 'USD Coin (USDC)',
    'ripple': 'Ripple (XRP)',
    'binancecoin': 'BNB (BNB)',
    'solana': 'Solana (SOL)',
    'dogecoin': 'Dogecoin (DOGE)',
    'tron': 'TRON (TRX)',
    'cardano': 'Cardano (ADA)',
    'polkadot': 'Polkadot (DOT)',
    'avalanche-2': 'Avalanche (AVAX)',
    'matic-network': 'Polygon (MATIC)',
    'shiba-inu': 'Shiba Inu (SHIB)',
    'chainlink': 'Chainlink (LINK)'
}


def format_price(price):
    """Форматирует число в строку с разделителями тысяч и 2 знаками после запятой."""
    return f"{price:,.2f}"


def get_crypto_price(coin_id):
    """
    Получает курс криптовалюты к USD .
    """
    try:
        url = "https://api.coingecko.com/api/v3/simple/price"

        params = {
            'ids': coin_id,
            'vs_currencies': 'usd',
            'include_last_updated_at': 'true'
        }

        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        if coin_id in data:
            coin_data = data[coin_id]
            price = coin_data['usd']

            last_updated = coin_data.get('last_updated_at', 0)

            # Обновляем текст в интерфейле
            result_label.config(
                text=(
                    f"💲 Курс: 1 {crypto_currencies[coin_id]} = ${format_price(price)} USD\n"
                    f"⏳ Обновлено: {datetime.fromtimestamp(last_updated).strftime('%H:%M:%S')}"
                ),

            )
        else:
            result_label.config(text="Данные для этой монеты не найдены.", foreground='black')

    except requests.exceptions.RequestException as e:
        result_label.config(text=f"Ошибка сети:\n{e}", foreground='black')
    except Exception as e:
        result_label.config(text=f"Ошибка:\n{e}", foreground='black')
