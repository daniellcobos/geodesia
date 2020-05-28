from tkinter import *
import rotacion
import tiempo
import math
import numpy as np
window = Tk()

window.title("Programa de Habilita avilita")

window.geometry('350x200')

lbl = Label(window, text="Coso del las cosas")
lbl2 = Label(window, text="Año")
lbl3 = Label(window, text="Mes")
lbl4 = Label(window, text="Dia")
lbl5 = Label(window, text="Fraccion de dia")

lbl.grid(column=0, row=0)
lbl2.grid(column=0, row=1)
lbl3.grid(column=0, row=2)
lbl4.grid(column=0, row=3)
lbl5.grid(column=0, row=4)
lbl6 = Label(window, text="Rotaciones").grid(column=0, row=6)
year = Entry(window,width=10)
year.grid(column=1, row=1)
month = Entry(window,width=10)
month.grid(column=1, row=2)
day = Entry(window, width=10)
day.grid(column=1, row=3)
day_fraction = Entry(window,width=10)
day_fraction.grid(column=1, row=4)


def tsg():
    a = float(year.get())
    m = float(month.get())
    d = float(day.get())
    df = float(day_fraction.get())
    print(tiempo.tsg(a, m, d, df))


btn = Button(window, text="TsgT", command=tsg)

btn.grid(column=1, row=5)

option1 = IntVar()
option2 = IntVar()
Radiobutton(window, text="r1", variable=option1,
            value=1, ).grid(column=1, row=7)
Radiobutton(window, text="r2", variable=option1,
            value=2, ).grid(column=1, row=8)
Radiobutton(window, text="r3", variable=option1,
            value=3, ).grid(column=1, row=9)
Radiobutton(window, text="r1", variable=option2,
            value=1, ).grid(column=1, row=10)
Radiobutton(window, text="r2", variable=option2,
            value=2, ).grid(column=1, row=11)
Radiobutton(window, text="r3", variable=option2,
            value=3, ).grid(column=1, row=12)
angle1 = Entry(window, width=10)
angle1.grid(column=1, row=13)
angle2 = Entry(window, width=10)
angle2.grid(column=1, row=14)
result = np.array(1)


def rot():
    a1 = math.radians(float(angle1.get()))
    a2 = math.radians(float(angle2.get()))
    r1 = int(option1.get())
    r2 = int(option2.get())
    global result
    result = rotacion.matrotacion(a1, a2, r1, r2)
    print(result)


def rot2():
    a1 = math.radians(float(angle1.get()))
    a2 = math.radians(float(angle2.get()))
    r1 = int(option1.get())
    r2 = int(option2.get())
    result2 = rotacion.mat3rotacion(a1, r1, result)
    print(result2)


btn = Button(window, text="Rot", command=rot)
btn.grid(column=1, row=15)
btn = Button(window, text="Segunda Rot", command=rot2)
btn.grid(column=1, row=16)
window.geometry("800x600")
window.mainloop()
