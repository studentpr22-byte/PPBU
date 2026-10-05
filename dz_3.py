import tkinter as tk

root = tk.Tk()
root.geometry("400x400")

msg = tk.Label(root, text="Введите 3 числа и нажмите на кнопку для вычисления суммы")
msg.pack(pady=20)

entry1 = tk.Entry(root, width=30)
entry1.pack(pady=0)
entry2 = tk.Entry(root, width=30)
entry2.pack(pady=0)
entry3 = tk.Entry(root, width=30)
entry3.pack(pady=0)


# Функция для сложения
def summa_numbers():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    num3 = float(entry3.get())

    result = num1 + num2 + num3
    result_label.config(text=f"Сумма: {result}")


# Функция для умножения
def multiply_numbers():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    num3 = float(entry3.get())

    result = (num1 * num2 * num3)
    result_label.config(text=f"Произведение: {result}")


# Функция для очистки
def clear_all():
    entry1.delete(0, "end")
    entry2.delete(0, "end")
    entry3.delete(0, "end")
    result_label.config(text="Результат: ")


button1 = tk.Button(root, text="Сложить 3 числа", width=30, command=summa_numbers)
button1.pack(pady=0)

button2 = tk.Button(root, text="Умножить 3 числа", width=30, command=multiply_numbers)
button2.pack(pady=0)

button3 = tk.Button(root, text="Очистить", width=30, command=clear_all)
button3.pack(pady=0)

# Окно вывода результата
result_label = tk.Label(root, text="Результат: ", font=("Arial", 14, "bold"))
result_label.pack(pady=15, padx=20, fill="x")

root.mainloop()
