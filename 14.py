import tkinter as tk


def greet():
    num_1 = entry.get()
    num_1 = int(num_1)
    num_2 = entry_2.get()
    num_2 = int(num_2)
    msg.config(text=f"Результат: {num_1 + num_2}")


win = tk.Tk()
win.title("Мой калькулятор")
win.geometry('420x320')
entry = tk.Entry(win)
entry.pack(pady=15)

entry_2 = tk.Entry(win)
win.title("Мой калькулятор")
entry_2.pack(pady=15)

btn = tk.Button(win, text='Сложить', command=greet)
btn.pack(pady=5)
msg = tk.Label(win, text="Результат: - ", font=('Arial', 18))

msg.pack(pady=15)

win.mainloop()
