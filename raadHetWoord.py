import random
import tkinter, string
from tkinter import ttk

def screen1():
    window = tkinter.Tk()
    
    window.title("Woordgeuss = speler 1")
    window.geometry("250x150")
    window.resizable(False, False)
    window.protocol("WM_DELETE_WINDOW", lambda: "")

    def stop():
        global woord, lengteWoord
        woord = woordEntry.get()
        if len(woord) > 7 or len(woord) < 4:
            retrieve()
        else:
            lengteWoord = len(woord)
            window.destroy()
    

    def retrieve(event=""):
        if woordEntry.get().isalpha() == False:
            woord = woordEntry.get()
            alpha_filter = filter(str.isalpha, woord)
            alpha_string = "".join(alpha_filter)
            v.set(alpha_string)
        if len(woordEntry.get()) > 7:
            x = woordEntry.get()
            x = x[0:7]
            v.set(x)
        if len(woordEntry.get()) >= 4 and len(woordEntry.get()) <= 7:
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
        woordUp = list(woord.upper())
        list1 = [woordUp[0]]
        list2 = [woordUp[1]]
        list3 = [woordUp[2]]
        list4 = [woordUp[3]]
        if lengteWoord > 4:
            list5 = [woordUp[4]]
            if lengteWoord > 5:
                list6 = [woordUp[5]]
                if lengteWoord > 6:
                    list7 = [woordUp[6]]
        
    
    def randomAdd(list):
        for x in range(4):
            choice = random.choice(alphabet_list)
            list.append(choice)
        random.shuffle(list)
        return list
        

    def checkWord():
        letter1 = spinBox1.get()
        letter2 = spinBox2.get()
        letter3 = spinBox3.get()
        letter4 = spinBox4.get()
        lettersGok = letter1 + letter2 + letter3 + letter4
        if lengteWoord > 4:
            letter5 = spinBox5.get()
            lettersGok += letter5
            if lengteWoord > 5:
                letter6 = spinBox6.get()
                lettersGok += letter6
                if lengteWoord > 6:
                    letter7 = spinBox6.get()
                    lettersGok += letter7
        print(lettersGok)
        if lettersGok == woord.upper():
            print("Goede woord")
        else:
            print("Foute woord")

    label1 = tkinter.Label(window,
    text="Vul een woord in",
        padx=30,
        pady=10,
        font=('Helvatical bold', 20)
    )    

    spinBox1 = ttk.Spinbox(window,
    values = alphabet_list,
    state = "readonly",
    width=2,
    wrap=True
    )

    spinBox2 = ttk.Spinbox(window,
    values = alphabet_list,
    state = "readonly",
    width=2,
    wrap=True
    )

    spinBox3 = ttk.Spinbox(window,
    values = alphabet_list,
    state = "readonly",
    width=2,
    wrap=True
    )

    spinBox4 = ttk.Spinbox(window,
    values = alphabet_list,
    state = "readonly",
    width=2,
    wrap=True
    )

    spinBox5 = ttk.Spinbox(window,
    values = alphabet_list,
    state = "readonly",
    width=2,
    wrap=True
    )

    spinBox6 = ttk.Spinbox(window,
    values = alphabet_list,
    state = "readonly",
    width=2,
    wrap=True
    )

    spinBox7 = ttk.Spinbox(window,
    values = alphabet_list,
    state = "readonly",
    width=2,
    wrap=True
    )

    gok = tkinter.Button(window,
    text = "Doe een gok!",
    command = checkWord
    )
    listMaker(lengteWoord)



    label1.grid(row=0, column=0, columnspan=lengteWoord,)
    gok.grid(row=2, column=0, columnspan = lengteWoord, pady=15)
    spinBox1.grid(row=1, column=0)
    spinBox2.grid(row=1, column=1)
    spinBox3.grid(row=1, column=2)
    spinBox4.grid(row=1, column=3)
    if lengteWoord > 4:
        spinBox5.grid(row=1, column=4)
        if lengteWoord > 5:
            spinBox6.grid(row=1, column=5)
            if lengteWoord > 6:
                spinBox7.grid(row=1, column=6)


    spinBox1.set("A")
    spinBox2.set("A")
    spinBox3.set("A")
    spinBox4.set("A")
    spinBox5.set("A")
    spinBox6.set("A")
    spinBox7.set("A")


    window.mainloop()

screen1()
screen2()