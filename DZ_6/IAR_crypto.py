import threading
from datetime import datetime  # Добавлен импорт
from tkinter import *
from tkinter import ttk

import requests

# Словарь: Читаемое название -> Торговая пара Binance
crypto_pairs = {
    'Bitcoin (BTC)': 'BTCUSDT',
    'Ethereum (ETH)': 'ETHUSDT',
    'BNB (BNB)': 'BNBUSDT',
    'Ripple (XRP)': 'XRPUSDT',
    'Solana (SOL)': 'SOLUSDT',
    'Dogecoin (DOGE)': 'DOGEUSDT',
    'TRON (TRX)': 'TRXUSDT',
    'Cardano (ADA)': 'ADAUSDT',
    'Polkadot (DOT)': 'DOTUSDT',
    'Avalanche (AVAX)': 'AVAXUSDT',
    'Polygon (MATIC)': 'MATICUSDT',
    'Shiba Inu (SHIB)': 'SHIBUSDT',
    'Chainlink (LINK)': 'LINKUSDT'
}

pair_to_name = {v: k for k, v in crypto_pairs.items()}


def format_price(price_float):
    return f"{price_float:,.2f}".replace(",", " ")


def get_crypto_price(symbol):
    """
    Получает цену торговой пары через Binance API и добавляет время запроса.
    """
    try:
        url = "https://api.binance.com/api/v3/ticker/price"
        params = {'symbol': symbol}

        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        if 'price' in data:
            price = float(data['price'])
            coin_name = pair_to_name.get(symbol, 'Unknown')

            # Получаем текущее локальное время в момент получения ответа
            current_time = datetime.now().strftime('%H:%M:%S')

            result_label.config(
                text=(
                    f"💲 Курс: 1 {coin_name} = ${format_price(price)} USD\n"
                    f"⏳ Обновлено: {current_time}"
                ),
                foreground='black'
            )
        else:
            result_label.config(text="Ошибка: не удалось получить цену.", foreground='black')

    except requests.exceptions.RequestException as e:
        result_label.config(text=f"Ошибка сети:\n{e}", foreground='black')
    except ValueError:
        result_label.config(text="Ошибка: неверный формат данных.", foreground='black')
    except Exception as e:
        result_label.config(text=f"Ошибка:\n{e}", foreground='black')


def on_crypto_select(event):
    selected_name = crypto_combobox.get()
    symbol = crypto_pairs.get(selected_name)

    if symbol:
        threading.Thread(target=lambda: get_crypto_price(symbol), daemon=True).start()


# --- Настройка интерфейса (без изменений) ---
root = Tk()
root.title('Курс криптовалют к USD (Binance)')
root.geometry('400x220')
root.resizable(False, False)

Label(root, text='Курс криптовалют к доллару США (Binance)', font=('Arial', 14, 'bold')).pack(pady=(15, 5))
Label(root, text='Выберите криптовалюту:', font=('Arial', 10)).pack(pady=(5, 0))
crypto_combobox = ttk.Combobox(root, values=list(crypto_pairs.keys()), font=('Arial', 11), state='readonly', width=30)
crypto_combobox.pack(pady=5)
crypto_combobox.bind('<<ComboboxSelected>>', on_crypto_select)

result_label = Label(root, text='Выберите монету из списка...', font=('Arial', 11, 'bold'), justify=LEFT)
result_label.pack(pady=20, padx=20, anchor='center')

crypto_combobox.current(0)
initial_symbol = crypto_pairs[crypto_combobox.get()]
threading.Thread(target=lambda: get_crypto_price(initial_symbol), daemon=True).start()

root.mainloop()

#
