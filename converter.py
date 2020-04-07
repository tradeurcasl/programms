from tkinter import *

#testing tkinter in work so wanna create little programm to calculate gramm - kg - pounds and oz

window = Tk()

def from_kg():
    gram = float(e2_value.get()) * 1000
    pound = float(e2_value.get()) * 2.20462
    ounce = float(e2_value.get()) * 35.274
    t1.delete("1.0", END)
    t1.insert(END, gram)
    t2.delete("1.0", END)
    t2.insert(END, pound)
    t3.delete("1.0", END)
    t3.insert(END, ounce)

x4 = Label(window, text=" ")
x4.grid(row=0, column=1)

e1 = Label(window, text="Kg")
e1.grid(row=1, column=0)

e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)
e2.grid(row=1, column=1)

b1 = Button(window, text="Convert", command=from_kg)
b1.grid(row=1, column=2)

x1 = Label(window, text="g")
x1.grid(row=2, column=0)

t1 = Text(window, height=1, width=20)
t1.grid(row=3, column=0)

x2 = Label(window, text="pound")
x2.grid(row=2, column=1)

t2 = Text(window, height=1, width=20)
t2.grid(row=3, column=1)

x3 = Label(window, text="oz")
x3.grid(row=2, column=2)

t3 = Text(window, height=1, width=20)
t3.grid(row=3, column=2)

x4 = Label(window, text=" ")
x4.grid(row=4, column=1)

window.mainloop()