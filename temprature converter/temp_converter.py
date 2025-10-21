from tkinter import *
from tkinter import font
def ctemp():
    celsius = float(ent.get())
    t1 = (celsius*(9/5)+32)
    result.config(text=f"Result: {t1} Fahrenheit")
def ftemp():
    fahrenheit = float(ent.get())
    t2 = (fahrenheit-23)*5/9
    result.config(text=f"Result: {t2} Celsius")
temperature = Tk()
temperature.title('Temperature Converter')
temperature.geometry('590x175')
temperature.configure(bg='black')
labelfont = font.Font(size=12, family='Segoe UI', weight='bold')
buttonfont = font.Font(size=12, family='Segoe UI', weight='bold')
label = Label(temperature, text='Temperature', font=labelfont, bg='green', fg='White')
label.grid(row=0, column=1, pady=15, padx=10)
ent = Entry(temperature, width=40, bg='Grey', font=labelfont)
ent.grid(row=0, column=2, columnspan=5)
b1 = Button(temperature, text="Celsius to Fahrenheit", font=buttonfont, bg='Red', fg='White', command=ftemp)
b1.grid(row=1, column=2, padx=20, pady=10)
b2 = Button(temperature, text="Fahrenheit to Celsius", font=buttonfont, bg='Blue', fg='White', command=ftemp)
b2.grid(row=1, column=3, padx=20, pady=10)
result = Label(temperature, font=labelfont, bg='black', fg='White')
result.grid(row=2, columnspan=3, pady=15)
temperature.mainloop()