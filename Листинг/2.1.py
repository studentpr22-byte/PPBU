from tkinter import *

window = Tk()
frame_top = Frame(window)
frame_bottom = Frame(window)
frame_top.pack()
frame_bottom.pack()

metka1 = Label(frame_top, text='Метка 1', bg='red')
metka1.pack(side=LEFT)
metka2 = Label(frame_top, text='Метка 2', bg='yellow')
metka2.pack(side=LEFT)
metka3 = Label(frame_top, text='Метка 3', bg='lightgreen')
metka3.pack(side=LEFT)
metka4 = Label(frame_bottom, text='Метка 4', bg='lightblue')
metka4.pack(side=RIGHT)
metka5 = Label(frame_bottom, text='Метка 5', bg='pink')
metka5.pack(side=RIGHT)
metka6 = Label(frame_bottom, text='Метка 6', bg='magenta')
metka6.pack(side=RIGHT)

window.mainloop()
