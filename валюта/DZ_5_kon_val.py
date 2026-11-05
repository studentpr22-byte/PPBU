from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk

import requests


def update_currency_label(event):
    code = target_combobox.get()
    name = currencies[code]
    target_label.config(text=name)


def update_base_label(event):
    # Определяем, какой именно комбобокс вызвал событие
    widget = event.widget
    if widget == base_combobox:
        code = base_combobox.get()
        base_label.config(text=currencies[code])
    elif widget == s_base_combobox:
        code = s_base_combobox.get()
        s_base_label.config(text=currencies[code])


def exchange():
    target_code = target_combobox.get().strip()
    base_code = base_combobox.get().strip()
    s_base_code = s_base_combobox.get().strip()

    if not (target_code and base_code and s_base_code):
        mb.showwarning('Внимание', 'Выберите все три валюты')
        return

    try:
        # Запрос для первой базовой валюты
        response1 = requests.get(f'https://open.er-api.com/v6/latest/{base_code}')
        response1.raise_for_status()
        data1 = response1.json()

        # Запрос для второй базовой валюты
        response2 = requests.get(f'https://open.er-api.com/v6/latest/{s_base_code}')
        response2.raise_for_status()
        data2 = response2.json()

        # Проверяем наличие целевой валюты в обоих ответах
        if target_code in data1['rates'] and target_code in data2['rates']:
            rate1 = data1['rates'][target_code]
            rate2 = data2['rates'][target_code]

            base_name = currencies[base_code]
            s_base_name = currencies[s_base_code]
            target_name = currencies[target_code]

            mb.showinfo('Курсы обмена',
                        f'1 {base_name} = {rate1:.2f} {target_name}\n'
                        f'1 {s_base_name} = {rate2:.2f} {target_name}')
        else:
            mb.showerror('Ошибка', f'Валюта {target_code} не найдена в ответе API')

    except requests.exceptions.RequestException as er:
        mb.showerror('Ошибка сети', str(er))
    except Exception as er:
        mb.showerror('Ошибка', str(er))


currencies = {
    'EUR': 'Евро',
    'USD': 'Доллар США',
    'JPY': 'Японская йена',
    'GBP': 'Фунт стерлингов',
    'AUD': 'Австралийский доллар',
    'CAD': 'Канадский доллар',
    'CHF': 'Швейцарский франк',
    'CNY': 'Китайский юань',
    'RUB': 'Российский рубль',
    'KZT': 'Казахстанский тенге',
    'UZS': 'Узбекский сум'
}

root = Tk()
root.title('Курс обмена валют')
root.geometry('360x270')

# Первая базовая валюта
Label(root, text='Базовая валюта 1').pack()
base_combobox = ttk.Combobox(root, values=list(currencies.keys()), state="readonly")
base_combobox.pack(pady=3, padx=10)
base_combobox.bind('<<ComboboxSelected>>', update_base_label)
base_label = ttk.Label()
base_label.pack()
