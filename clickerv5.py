import tkinter
import threading
window = tkinter.Tk()

window.title("Clicker")
window.config(bg="grey")
window.geometry("350x200")
count = 0
state = "neutral"
def enableBox():
    if state != "neutral":
        pass
    else:
        checkBox.config(state="active")
        
def f_add(event="none"):
    global state
    global count
    count += 1
    exit_event.set()
    counter.configure(text = count)
    enableBox()
    state = "up"

exit_event = threading.Event()

def upChecked():
    while True:
        if exit_event.wait(timeout=0.2):
            exit_event.clear()
            checkBox.deselect()
            break
        else:
            f_add()
            exit_event.clear()
def thread_up():
    upCheck = threading.Thread(target=upChecked)
    upCheck.start()

def downChecked():
    while True:
        if exit_event.wait(timeout=0.2):
            exit_event.clear()
            checkBox.deselect()
            break
        else:
            f_subtract()
            exit_event.clear()
def thread_down():
    downCheck = threading.Thread(target=downChecked)
    downCheck.start()


checkBox_var = tkinter.StringVar()


def checked():
    if checkBox_var.get() == "on":
        exit_event.clear()
        if state == "up":
            thread_up()
        elif state == "down":
            thread_down()
    else:
        exit_event.clear()




checkBox = tkinter.Checkbutton(window,
    text = "Check box",
    command = checked,
    variable= checkBox_var,
    onvalue= "on",
    offvalue= "off",
    state="disabled"
)
checkBox.deselect()
checkBox.pack()

#button to add to count
add = tkinter.Button(
    window,
    text="Up",
    width=25,
    height=1,
    command= f_add
)
add.pack()
add.place(anchor="center", x=175, y=50)

def f_subtract(event="none"):
    global state
    global count
    count -= 1
    exit_event.set()
    counter.configure(text = count)
    enableBox()
    state = "down"

#button to lower count
subtract = tkinter.Button(
    window,
    text="Down",
    width=25,
    height=1,
    command=f_subtract
)
subtract.pack()
subtract.place(anchor="center", x=175, y=150)

#shows current count
counter = tkinter.Label(
    window,
    height=1,
    width=25,
    text=count
)
counter.pack()
counter.place(anchor="center", x=175, y=100)

def calc(event):
    if count > 0:
        window.config(bg = "green")
    elif count < 0 :
        window.config(bg= "red")
    else:
        window.config(bg= "grey")

def leave(event):
    window.config(bg="grey")

def doubleClick(event):
    global count
    if state == "up":
        count *= 3
        counter.configure(text = count)
    elif state == "down":
        count //= 3
        counter.configure(text = count)
    else:
        pass



counter.bind("<Enter>", calc)
counter.bind("<Leave>", leave)
counter.bind("<Double-Button>", doubleClick)
window.bind("<Down>", f_subtract)
window.bind("-", f_subtract)
window.bind("<Up>", f_add)
window.bind("=", f_add)
window.bind("<space>", doubleClick)

def on_closing():
    exit_event.set()
    window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()