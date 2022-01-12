import tkinter
import datetime
import calendar
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import messagebox


window = tkinter.Tk()
window.geometry("200x135")
window.title("Date calc")
window.resizable(False, False)

day_selected = tkinter.StringVar()
# day_cb = ttk.Combobox(window, textvariable=day_selected)
# day_cb.pack()
months = list(calendar.month_name)
months.pop(0)

#diffrence calculator
def calcDays():
    try:
        if Combo.get() == "Pick a month" or day_selected == "Pick a day":
            pass
        else:
            today = datetime.date.today()
            someday = datetime.date(int(yearEntry.get()), int(months.index(Combo.get()))+1, int(Combo2.get()))
            diff = someday - today
            diff = diff.days
            if diff == 0:
                output = "That is today"
            elif diff < 0:
                diff *= -1
                output = "{} day(s) ago"
            else:
                output = "In {} day(s)"
            messagebox.showinfo(title='Result',
                                message=output.format(diff))
    except:
        pass

list1 = ['January', 'March', 'May', 'July', 'August', 'October', 'December']

days1 = []
for z in range(1,32):
    days1.append(z)

days2 = []
for z in range(1,31):
    days2.append(z)

days3 = []
for z in range(1,30):
    days3.append(z)

days4 = []
for z in range(1,29):
    days4.append(z)

Combo = ttk.Combobox(window, values = months, state='readonly')
Combo.set("Pick a month")
Combo.pack(padx = 5, pady = 5)

Combo2 = ttk.Combobox(window, values = days1, state='readonly', textvariable=day_selected)
Combo2.set("Pick a day")
Combo2.pack(padx = 5, pady = 5)

v = tkinter.StringVar()

yearEntry = ttk.Entry(window, textvariable=v)
yearEntry.configure(width= 23)
yearEntry.pack(padx = 5, pady = 5)
v.set("2000")

calculate = tkinter.Button(window, text = "calculate", command=calcDays)
calculate.pack(padx = 5, pady= 5)

#checks the amount of days the month should have
def retrieve(event):
    try:
        year = int(yearEntry.get())
    except:
        year = yearEntry.get()
        numeric_filter = filter(str.isdigit, year)
        numeric_string = "".join(numeric_filter)
        v.set(numeric_string)
    if '' == yearEntry.get():
        year = 0
    else:
        year = yearEntry.get()
        year = int(year[0:4])
        v.set(year)
    leapYear = False
    if year % 400 == 0 or  year % 100 != 0 and year % 4 == 0:
        leapYear = True
    y = 1
    for x in range(7):
        if Combo.get() == list1[x]:
            Combo2["values"] = (days1)
            break
        else:
            Combo2["values"] = (days2)
            if day_selected.get() == "31":
                day_selected.set("30")
                print(yearEntry.get())
    if Combo.get() == "February" and leapYear == True:
        Combo2["values"] = (days3)
        if day_selected.get() == 'Pick a day':
            pass
        elif int(day_selected.get()) >= 30:
            day_selected.set("29x")
    elif Combo.get() == "February":
        Combo2["values"] = (days4)
        if day_selected.get() == 'Pick a day':
            pass
        elif int(day_selected.get()) >= 29:
            day_selected.set("28")


Combo.bind("<<ComboboxSelected>>",retrieve)
yearEntry.bind("<KeyRelease>", retrieve)
window.mainloop()