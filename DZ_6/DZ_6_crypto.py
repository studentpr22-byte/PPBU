import threading
from datetime import datetime
from tkinter import *
from tkinter import ttk

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


def on_crypto_select(event):
    """Запускает получение цены в отдельном потоке при выборе монеты."""
    coin_id = crypto_combobox.get()
    if coin_id:
        threading.Thread(target=lambda: get_crypto_price(coin_id), daemon=True).start()


# Настройка интерфейса
root = Tk()
root.title('Конвертер криптовалют в USD (CoinGecko)')
root.geometry('400x220')
root.resizable(False, False)

# # Стили
style = ttk.Style(root)

# Заголовок
Label(root, text='Курс криптовалют к доллару США', font=('Arial', 14, 'bold')).pack(pady=(15, 5))

# Выпадающий список выбора криптовалюты
Label(root, text='Выберите криптовалюту:', font=('Arial', 10)).pack(pady=(5, 0))
crypto_combobox = ttk.Combobox(root, values=list(crypto_currencies.keys()), font=('Arial', 11), state='readonly',
                               width=30)
crypto_combobox.pack(pady=5)
crypto_combobox.bind('<<ComboboxSelected>>', on_crypto_select)

# Метка для отображения результата
result_label = Label(root, text='Выберите монету из списка...', font=('Arial', 11, 'bold'), justify=LEFT)
result_label.pack(pady=20, padx=20, anchor='center')

# Устанавливаем значение по умолчанию
crypto_combobox.current(0)
# И сразу запрашиваем данные для первой монеты
threading.Thread(target=lambda: get_crypto_price(crypto_combobox.get()), daemon=True).start()

root.mainloop()
