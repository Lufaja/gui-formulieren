import tkinter
import time
import threading
import random
import sys
import os

window = tkinter.Tk()
window.title("FPS Trainer")
window.geometry("500x350")
window.config(bg="black")
def threadprint():
    print(threading.active_count())
    pass
threadprint()
list = ["Press W", "Press A", "Press D", "Press S", "Press Space", "Single Click", "Double Click", "Triple Click"]
popUp = 0
condition = threading.Condition()
inputTime = 0
t = 20
score = 0
pointVar = tkinter.StringVar()
pointVar = str(score) + " Point(s)"
exit_event = threading.Event()
pop_event = threading.Event()
flag = threading.Event()


def reset():
    # os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
    global t, score, exit_event, start, popUp, start, inputTime
    popUp.destroy()
    exit_event.set()
    exit_event.clear()
    # print(helpA.is_alive())
    # print(countdown_thread.is_alive())
    # print(threading_checkState.is_alive())
    threadprint()
    t = 20
    score = 0
    pointVar = str(score) + " Point(s)"
    points.config(text=pointVar)
    currentTime = ("time: " + str(t))
    timer.config(text=currentTime)
    askTime()
    start = tkinter.Button(
        window,
        text="Start",
        command=f_start
    )
    start.pack()
    start.place(anchor="c", x=250, y=175)


currentTime = ("time: " + str(t))

def popup():
    global popUp
    popUp = tkinter.Tk()
    popUp.geometry("200x200")
    retry = tkinter.Button(
        popUp,
        text = "Retry",
        width= 3,
        height= 1,
        command=reset
    )
    print(threading.active_count())
    print(countdown_thread.is_alive())
    retry.pack()
    retry.place(anchor= "s", x= 50, y=150)
    def stop():
        popUp.destroy()
        window.destroy()
    quit = tkinter.Button(
        popUp,
        text = "Quit",
        width = 3,
        height= 1,
        command=stop
    )
    pointVar = str(score) + " Point(s)"
    label1 = tkinter.Label(
    popUp,
    text = pointVar
    )
    label1.pack()
    label1.place(anchor="c", x = "100", y = "75")
    quit.pack()
    quit.place(anchor= "s", x= 150, y=150)
    popUp.mainloop()

def bindVar(var):
    if var == "Press W":
        return "w"
    elif var == "Press A":
        return "a"
    elif var == "Press D":
        return "d"
    elif var == "Press S":
        return "s"
    elif var == "Press Space":
        return "<space>"
    elif var == "Single Click":
        return "<Button-1>"
    elif var == "Double Click":
        return "<Double-Button-1>"
    elif var == "Triple Click":
        return "<Triple-Button-1>"

def f_randomLabel():
    global pop_event
    if t == 0:
        pop_event.set()
    else:    
        global pointVar
        randBind = random.choice(list)
        var1 = bindVar(randBind)
        randomLabel = tkinter.Label(
            window,
            text=randBind,
            width=10,
            height=2
        )
        randomLabel.pack()
        randomLabel.place(x=(random.randint(0,421)), y=random.randint(36, 307))
        def hit(event):
            global score
            global exit_event
            if "Press" in randBind:
                score += 1
            else:
                score += 2
            randomLabel.destroy()
            exit_event.set()
            if "Press" in randBind:
                window.unbind(var1)
            pointVar = (str(score) + " Point(s)")
            points.config(text=pointVar)
            f_randomLabel()
        if "Press" in randBind:
            window.bind(var1, hit)
        else:
            randomLabel.bind(var1, hit)
        def help():
            if exit_event.wait(timeout=2):
                exit_event.clear()
                if t == 0:
                    randomLabel.destroy()
                    if "Press" in randBind:
                        window.unbind(var1)
                    global pop_event
                    pop_event.set()
            else:
                randomLabel.destroy()
                if "Press" in randBind:
                    window.unbind(var1)
                f_randomLabel()
        def help_thread():
            global helpA
            helpA = threading.Thread(target=help)
            helpA.daemon = True
            helpA.start()
        help_thread()
        threadprint()




def countdown():
    global t
    global currentTime, flag, condition
    while True: 
        if flag.wait():
            flag.clear()
            while t != 0 :
                time.sleep(1)
                t -= 1
                currentTime = ("time: " + str(t))
                timer.config(text=currentTime)
            exit_event.set()
            popup()



def f_timer():
    global countdown_thread
    countdown_thread = threading.Thread(target = countdown)
    countdown_thread.daemon = True
    countdown_thread.start()
    threadprint()
 
timer = tkinter.Label(
    window,
    text = currentTime,
    padx=125
)

timer.pack()
timer.place(anchor="n", x=125)

points = tkinter.Label(
    window,
    text=pointVar,
    padx=125
)

points.pack()
points.place(anchor="n", x=375)

def askTime():
    global inputTime, time_label, time_entry
    inputTime = tkinter.IntVar()
    inputTime.set(20)
    time_label = tkinter.Label(window, text="Time in seconds: ", width=16, borderwidth=0, padx=2)
    time_label.pack()
    time_label.place(anchor="s", y=140, x=250)
    time_entry = tkinter.Entry(window, textvariable=inputTime, width=19, borderwidth=0)
    time_entry.pack()
    time_entry.place(anchor="n", y=140, x=250)
    time_entry.focus()
    time_entry.icursor(2)

def f_start():
    global t, inputTime, currentTime, flag, condition
    t = inputTime.get()
    currentTime = ("time: " + str(t))
    timer.config(text=currentTime)
    start.destroy()
    time_label.destroy()
    time_entry.destroy()
    flag.set()
    # f_checkState()
    f_randomLabel()


def checkState():
    global pop_event, exit_event
    if pop_event.wait():
        pop_event.clear()
        exit_event.set()
        popup()
        print("hoi")

# def f_checkState():
#     global threading_checkState
#     threading_checkState = threading.Thread(target=checkState)
#     threading_checkState.start()
    

f_timer()
askTime()
start = tkinter.Button(
    window,
    text="Start",
    command=f_start
)
start.pack()
start.place(anchor="c", x=250, y=175)
window.mainloop()
sys.exit()