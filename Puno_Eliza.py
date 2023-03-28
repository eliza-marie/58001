from tkinter import *
window = Tk()
window.geometry("500x400+10+10")
window.title("My First GUI")

btn1 = Button(window, text = 'Click Me', fg = "white", bg = "black")
btn1.place(x=200, y=200)
txtfld = Entry(window, border = 2.5)
txtfld.place(x = 180, y = 150)

lbl = Label(window, text = "First Demo by Eliza")
lbl.place(x = 180, y = 100)

window.mainloop()