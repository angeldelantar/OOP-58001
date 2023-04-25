from tkinter import *
win = Tk()

lbl = Label(win, text="Gender")
lbl.place(relx= .5, rely= .5)
lbl.pack(anchor="center")
var1 = IntVar()
var2 = IntVar()
r1 = Radiobutton(win, text= "Male", variable=var1)
r1.place(x=50, y=50)
r2 = Radiobutton(win, text= "Female", variable=var2)
r2.place(x=50, y=70)
var1 = IntVar()
var2 = IntVar()

chk1 = Checkbutton(win, text="100-200")
chk2 = Checkbutton(win, text="201-300")
chk3 = Checkbutton(win, text="301-400")

chk1.place(x=70, y=90)
chk2.place(x=70, y=120)
chk3.place(x=70, y=150)

lbl2 = Label(win,text="Select from the list of Fruits:")
lbl2.place(x=80, y=180)

lt = Listbox(win, selectmode="Single")
lt.insert(1, "Banana")
lt.insert(2, "Strawberry")
lt.insert(3, "Blueberry")
lt.insert(3, "Mango")
lt.insert(4, "Grapefruit")
lt.insert(5, "Apple")
lt.place(x=80, y=200)

win.geometry("500x400+10+10")
win.mainloop()

