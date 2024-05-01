from tkinter import *


window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=300, height=110)
window.config(padx=25, pady=25)


def total():
    distance = float(entry.get())
    value = round(distance * 1.609)
    calculated.config(text=value)

#Label
miles = Label(text="Miles")
miles.grid(column=2, row=0)
miles.config(padx=15)
km = Label(text="Km")
km.grid(column=2, row=1)
calculated = Label(text=0)
calculated.grid(column=1, row=1)
equal = Label(text="is equal to")
equal.grid(column=0, row=1)
equal.config(padx=10)


#Button
convert = Button(text="Calculate", command=total)
convert.grid(column=1, row=2)

#Entry
entry = Entry()
entry.config(width=9)
entry.grid(column=1, row=0)





window.mainloop()