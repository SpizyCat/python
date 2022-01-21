from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Simons Vending Machine")

product_1 = Button(root, text="Chips - 15€", padx=20, pady=20)
product_2 = Button(root, text="Chips - 15€", padx=20, pady=20)

product_1.grid(row=0, column=0)
product_2.grid(row=0, column=1)

root.mainloop()