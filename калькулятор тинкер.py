# # import tkinter as tk
# #
# # root = tk.Tk()
# # root.title("Мой калькулятор")
# # root.geometry("420x320")
# # msg = tk.Label(root, text="Нажатий!", count)
# # msg.pack(pady=12)
# #
# # count = 0
# # def click():
# #     global count
# #     count += 1
# #     msg.config(text=f"Нажатий: {count}")
# #
# #
# # def signal():
# #     msg.config(text="Проверить!")
# #
# #
# # btn = tk.Button(
# #     root,
# #     text="Начать",
# #     command=signal
# # )
# #
# # # btn.pack()
# # #
# # #
# # #
# # # root.mainloop()
# #
# #
# # import tkinter as tk
# #
# # count = 0
# #
# #
# #
# #
# # def click():
# #     global count
# #     count += 1
# #     msg.config(text=f"ЙО: {count}")
# #
# # win = tk.Tk()
# # win.title("Мой калькулятор")
# # win.geometry('420x320')
# # # msg = tk.Label(win, text="Нажатий: 0")
# # msg = tk.Label(win, text=f"Проверить: {count} ")
# # font = ('Arial', 1)
# # msg.pack(pady=55)
# #
# # def signal():
# #     # msg.config(text="Ответ получен")
# #     msg.config()
# # btn = tk.Button(
# #     win,
# #     text="Проверить",
# #     command=signal
# # )
# #
# #
# # btn.pack()
# #
# #
# #
# #
# #
# #
# #
# # win.mainloop()
#
#
#
import tkinter as tk

count = 0

root = tk.Tk()
root.title("Мой калькулятор")
root.geometry("420x320")
msg = tk.Label(root, text=f"Нажатий: {count}")
msg.pack(pady=30)


def click():
    global count
    count += 1
    msg.config(text=f"Нажатий: {count}")


def signal():
    msg.config(text=f"Нажатий: {count}")


btn = tk.Button(
    root,
    text="Проверить",
    command=signal
)
click()

btn.pack()

root.mainloop()
