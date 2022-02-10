import random
import tkinter, string
from tkinter import ttk
from tkinter.messagebox import *

listSize = 5 #max 26
maximum = 7
minimum = 4
def screen1():
    window = tkinter.Tk()
    
    window.title("Woordgeuss = speler 1")
    window.geometry("250x150")
    window.resizable(False, False)
    window.protocol("WM_DELETE_WINDOW", lambda: "")

    def stop():
        global woord, lengteWoord, punten
        woord = woordEntry.get()
        if len(woord) > maximum or len(woord) < minimum:
            retrieve()
        else:
            lengteWoord = len(woord)
            punten = lengteWoord**2
            window.destroy()
            screen2()
    

    def retrieve(event=""):
        if woordEntry.get().isalpha() == False:
            woord = woordEntry.get()
            alpha_filter = filter(str.isalpha, woord)
            alpha_string = "".join(alpha_filter)
            v.set(alpha_string)
        if len(woordEntry.get()) > maximum:
            x = woordEntry.get()
            x = x[0:maximum]
            v.set(x)
        if len(woordEntry.get()) >= minimum and len(woordEntry.get()) <= maximum:
            button1.config(state = "active")
        else:
            button1.config(state= "disabled")

    
    v = tkinter.StringVar()

    label1 = tkinter.Label(window,
    text="Vul een woord in",
        padx=10,
        pady=10,
        font=('Helvatical bold', 20)
    )
    
    woordEntry = tkinter.Entry(window,
        width=20,
        textvariable=v
    )

    label = tkinter.Label(window,
    pady=2
    )
    
    button1 = tkinter.Button(window,
        command=stop,
        state="disabled",
        text="Stel woord in",
    )

    label1.pack()
    woordEntry.pack()
    label.pack()
    button1.pack()
    
    woordEntry.bind("<KeyRelease>", retrieve)
    
    window.mainloop()

def screen2():
    print(lengteWoord)
    window = tkinter.Tk()
    window.title("Woordgeuss = speler 2")
    window.resizable(False, False)


    alphabet_string = string.ascii_uppercase
    alphabet_list = list(alphabet_string)
    
    def listMaker(number):
        spinList = []
        woordUp = list(woord.upper())
        for x in range(0, lengteWoord):
            list_ = [woordUp[x]]
            z = randomAdd(list_)
            v = random.choice(z)
            spinList.append(ttk.Spinbox(window,
                values = z,
                state = "readonly",
                width=2,
                wrap=True
                ))
            spinList[x].set(v)
        for x in range(len(spinList)):
            spinList[x].grid(row=1, column=x)
        return spinList

    
    def randomAdd(list):
        for x in range(listSize-1):
            choice = list[0]
            while choice in list:
                choice = random.choice(alphabet_list)
            list.append(choice)
        random.shuffle(list)
        return list
        

    def checkWord():
        global punten
        goed = 0
        fout = 0
        lettersGok = ""
        for x in range(0, lengteWoord):
            lettersGok += spin[x].get()
        print(lettersGok)
        if lettersGok == woord.upper():
            print("Goede woord")
            if askretrycancel(title="Geraden", message=f"Je hebt het woord geraden!\nJe hebt {punten} punten gehaald\nWil je nog een keer?",) == True:
                window.destroy()
                screen1()
            else:
                window.destroy()
        else:
            print("Foute woord")
            listLettersGok = list(lettersGok)
            listWoord = list(woord.upper())
            for x in range(0, lengteWoord):
                if listLettersGok[x] == listWoord[x]:
                    goed += 1
                else:
                    fout += 1
            punten -= 2*fout
            showinfo(title='Punten',
                message=f'helaas er zijn {goed} letters goed\nPunten: {punten}')
            if punten <= 0:
                window.destroy()
        print(f"goed: {goed}")
        print(f"fout: {fout}")
        


    label1 = tkinter.Label(window,
    text="Vul een woord in",
        padx=30,
        pady=10,
        font=('Helvatical bold', 20)
    )    


    gok = tkinter.Button(window,
    text = "Doe een gok!",
    command = checkWord
    )
    spin = listMaker(lengteWoord)


    label1.grid(row=0, column=0, columnspan=lengteWoord,)
    gok.grid(row=2, column=0, columnspan = lengteWoord, pady=15)

    window.mainloop()

screen1()