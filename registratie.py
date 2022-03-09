import tkinter, re
from tkinter import messagebox
from date import datum
import random

window = tkinter.Tk()
window.title("Registratie")
window.geometry("500x600")
window.resizable(False, False)

#Variables
email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")

#Geboorte datum dingen
datumding = datum(window)
datumding.place(x=25, y=325)
datumding.check()
# datumding.getDatum()

#Defines
def check():
    a = checkName(entry.get(), entry1.get())
    b = checkEmail(entry2.get())
    z = entry3.get()
    z = z.replace(" ","")
    c = checkPhone(z)
    d = datumding.leeftijd()
    if type(d) == int:
        if d < 16:
            messagebox.showwarning(message="Je moet 16 jaar of ouder zijn")
            d = False
    if a == False or b == False or c == False or d == False:
        button.configure(state='disabled')
        window.after(5000, lambda: button.configure(state='active'))
        if a == False:
            entry.configure(fg="red")
            entry1.configure(fg="red")
            window.after(5000, lambda: entry.configure(fg="black"))
            window.after(5000, lambda: entry1.configure(fg="black"))
        if b == False:
            entry2.configure(fg="red")
            window.after(5000, lambda: entry2.configure(fg="black"))
        if c == False:
            entry3.configure(fg="red")
            window.after(5000, lambda: entry3.configure(fg="black"))
    else:
        global name, surname, email, number, birthday
        name, surname, email, number, birthday = entry.get(), entry1.get(), entry2.get(), z, datumding.getDatum().strftime("%d/%m/%Y")
        window.destroy()


def checkName(name:str, surname:str):
    surname = surname.replace(" ", "")
    if name.isalpha() and surname.isalpha() and len(name) > 0 and len(surname) > 0:
        return True
    else:
        return False

def checkEmail(email):
    if email_regex.match(email):
        return True
    else:
        return False
    

def checkPhone(number:str):
    if number.isdigit():
        if len(number) == 10:
            return True
        else:
            return False
    else:
        return False

def error(text):
    pass

#Tkinter labels, widgets, ect...
label = tkinter.Label(
    window,
    text = "E3 2022",
    font=("Arial", 25)
)

label1 = tkinter.Label(
    window,
    text = "Vul uw volledige naam in",
    font=("Arial", 11)
)
entry = tkinter.Entry(
    window
)
entry1 = tkinter.Entry(
    window
)

label2 = tkinter.Label(
    window, 
    text = "Vul uw email in",
    font=("Arial", 11)
)

entry2 = tkinter.Entry(
    window,
    width=25
)

label3 = tkinter.Label(
    window,
    text= "Vul uw telefoon nummer in",
    font =("Arial", 11)
)

label4 = tkinter.Label(
    window,
    text= "Vul uw geboortedatum in",
    font =("Arial", 11)
)

entry3 = tkinter.Entry(
    window
)

button = tkinter.Button(
    window,
    text="Confirm",
    command=check
)

#tkinter place
label.place( x = 200)
label1.place(x = 25, y = 150)
entry.place( x = 25, y = 175)
entry1.place(x = 150, y = 175)
label2.place(x = 25, y = 200)
entry2.place(x = 25, y = 225)
label3.place(x = 25, y = 250)
entry3.place(x = 25, y = 275)
label4.place(x = 25, y = 300)
button.place(x = 25, y = 425)
window.mainloop()

window = tkinter.Tk()
window.title("Registratie")
window.geometry("200x175")
window.resizable(False, False)

label1 = tkinter.Label(
    window,
    text=f"Naam:\n{name} {surname}"
)

label2 = tkinter.Label(
    window,
    text=f"E-Mail:\n{email}"
)

label3 = tkinter.Label(
    window,
    text=f"Telefoon nummer:\n{number}"
)

label4 = tkinter.Label(
    window,
    text=f"Geboortedatum:\n{birthday}"
)

label5 = tkinter.Label(
    window,
    text= random.randint(1000000,10000000)
)

label1.pack()
label2.pack()
label3.pack()
label4.pack()
label5.pack()




window.mainloop()