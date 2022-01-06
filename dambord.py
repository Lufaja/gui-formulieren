import tkinter
window = tkinter.Tk()
window.title("Dambord")
window.geometry("940x930")
frame = tkinter.Frame(window)
z=1
for x in range(10):
    if z==0:
        z=1
    else:
        z=0
    for y in range(10):
        if z == 0:
            b="black"
            z=1
        else:
            b="white"
            z=0
        label = tkinter.Label(frame,
        padx=12.5*3.6,
        pady=10*3.7,
        bg=b
        ).grid(row=y,column=x)
frame.pack(expand=True)
window.mainloop()