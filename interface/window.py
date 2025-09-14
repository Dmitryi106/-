from tkinter import *
from tkinter import ttk

import main

root = Tk()
root.title("Weather app")
root.iconbitmap(default="folder_images_16081.ico")
root.geometry("1000x700+400+200")
root.resizable(False, False)
# стандартная кнопка
btn = ttk.Button(text="Нажми", command=main.basic_actions())
btn.pack(pady=20)



root.mainloop()