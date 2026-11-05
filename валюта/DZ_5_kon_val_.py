from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk

import requests


def update_currency_label(event):
    code = target_combobox.get()
    name = currencies[code]
    target_label.config(text=name)


def update_base_label(event):
    code = base_combobox.get()
    name = currencies[code]
    base_label.config(text=name)


def update_second_base_label(event):
    code = s_base_combobox.get()
    name = currencies[code]
    s_base_label.config(text=name)


def exchange():
    target_code = target_combobox.get().strip()
    base_code = base_combobox.get().strip()
    s_base_code = s_base_combobox.get().strip()

    if target_code and base_code and s_base_code:
        try:
            # курсы для обеих базовых валют
            r1 = requests.get(f'https://open.er-api.com/v6/latest/{base_code}')
            r1.raise_for_status()
            rates1 = r1.json()['rates']

            r2 = requests.get(f'https://open.er-api.com/v6/latest/{s_base_code}')
            r2.raise_for_status()
            rates2 = r2.json()['rates']

            if target_code in rates1 and target_code in rates2:
                exchange_rate = rates1[target_code]
                s_exchange_rate = rates2[target_code]
                base = currencies[base_code]
                s_base = currencies[s_base_code]
                target = currencies[target_code]

                mb.showinfo(
                    'Курс обмена',
                    f'Курс: {exchange_rate:.1f} {target} за 1 {base}\n'
                    f'Курс: {s_exchange_rate:.1f} {target} за 1 {s_base}'
                )
            else:
                mb.showerror('Ошибка', f'Валюта {target_code} не найдена')
        except Exception as er:
            mb.showerror('Ошибка', er)
    else:
        mb.showwarning('Внимание', 'Выберите обе базовые и целевую валюту')


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
root.geometry('360x340')

Label(root, text='Базовая валюта').pack()
base_combobox = ttk.Combobox(root, values=list(currencies.keys()))
base_combobox.pack(pady=3, padx=10)
base_combobox.bind('<<ComboboxSelected>>', update_base_label)
base_label = ttk.Label(root)
base_label.pack()

Label(root, text='Вторая базовая валюта').pack()
s_base_combobox = ttk.Combobox(root, values=list(currencies.keys()))
s_base_combobox.pack(pady=3, padx=10)
s_base_combobox.bind('<<ComboboxSelected>>', update_second_base_label)  # свой обработчик
s_base_label = ttk.Label(root)
s_base_label.pack()

Label(root, text='Целевая валюта').pack(padx=10)
target_combobox = ttk.Combobox(root, values=list(currencies.keys()))
target_combobox.pack(pady=3, padx=10)
target_combobox.bind('<<ComboboxSelected>>', update_currency_label)

target_label = ttk.Label(root)
target_label.pack()

Button(text='Получить курс обмена',
       command=exchange).pack(pady=10, padx=10)

root.mainloop()
