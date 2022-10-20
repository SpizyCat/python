from tkinter import *

root = Tk()
root.title("Simons Cool Calculator")

e = Entry(root, width=40, border=3)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
def button_press():
    return

my_button_1 = Button(root, text="1", padx=50, pady=25,  activeforeground="#aaffaa", command=button_press)
my_button_2 = Button(root, text="2", padx=50, pady=25,  activeforeground="#aaffaa")
my_button_3 = Button(root, text="3", padx=50, pady=25,  activeforeground="#aaffaa")
my_button_4 = Button(root, text="4", padx=50, pady=25,  activeforeground="#aaffaa")
my_button_5 = Button(root, text="5", padx=50, pady=25,  activeforeground="#aaffaa")
my_button_6 = Button(root, text="6", padx=50, pady=25,  activeforeground="#aaffaa")
my_button_7 = Button(root, text="7", padx=50, pady=25,  activeforeground="#aaffaa")
my_button_8 = Button(root, text="8", padx=50, pady=25,  activeforeground="#aaffaa")
my_button_9 = Button(root, text="9", padx=50, pady=25,  activeforeground="#aaffaa")
my_button_0 = Button(root, text="0", padx=50, pady=25,  activeforeground="#aaffaa")
my_button_dot = Button(root, text=".", padx=52, pady=25,  activeforeground="#aaffaa")
my_button_equal = Button(root, text="=", padx=50, pady=25,  activeforeground="#aaffaa")
my_button_power = Button(root, text="^", padx=50, pady=25,  activeforeground="#aaffaa")
my_button_clear = Button(root, text="AC", padx=50, pady=25,  activeforeground="#aaffaa")
my_button_divide = Button(root, text="÷", padx=55, pady=25,  activeforeground="#aaffaa")
my_button_multiply = Button(root, text="×", padx=55, pady=25,  activeforeground="#aaffaa")
my_button_addition = Button(root, text="+", padx=54, pady=25,  activeforeground="#aaffaa")
my_button_subtract = Button(root, text="-", padx=55, pady=25,  activeforeground="#aaffaa")

my_button_addition.grid(row=5, column=3)
my_button_equal.grid(row=5, column=2)
my_button_dot.grid(row=5, column=1)
my_button_0.grid(row=5, column=0)

my_button_1.grid(row=4, column=0)
my_button_2.grid(row=4, column=1)
my_button_3.grid(row=4, column=2)
my_button_subtract.grid(row=4, column=3)

my_button_4.grid(row=3, column=0)
my_button_5.grid(row=3, column=1)
my_button_6.grid(row=3, column=2)
my_button_multiply.grid(row=3, column=3)

my_button_7.grid(row=2, column=0)
my_button_8.grid(row=2, column=1)
my_button_9.grid(row=2, column=2)
my_button_divide.grid(row=2, column=3)

my_button_power.grid(row=1, column=0)
my_button_clear.grid(row=1, column=3)

root.mainloop()