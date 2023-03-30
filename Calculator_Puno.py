from tkinter import *
class MyWindow:
    def __init__(self, win):

#widgets start from here
        self.lbl1 = Label(win, text="Enter First Number:")
        self.lbl1.place(x=100, y=50)
        self.lbl2 = Label(win, text= "Enter Second Number:")
        self.lbl2.place(x=100, y=100)
        self.lbl3 = Label(win, text="Results:")
        self.lbl3.place(x=100, y=150)
        self.txt1 = Entry(win, bd=1)
        self.txt1.place(x=200, y=50)
        self.txt2 = Entry(win, bd=1)
        self.txt2.place(x=200, y=100)
        self.txt3 = Entry(win, bd=3)
        self.txt3.place(x=200, y=150)
        self.btnclr = Button(win, text="Clear", bg="Pink", command=self.clr)
        self.btnclr.place(x=100, y=200)
        #self.btnclr.bind('<Button-1>', self.clr)
        self.btnadd = Button(win, text="+", command=self.add)
        self.btnadd.place(x=150, y=200)
        #self.btnadd.bind('<Button-1>', self.add)
        self.btnsub = Button(win, text="-", command=self.sub)
        self.btnsub.place(x=180, y=200)
        #self.btnsub.bind('<Button-1>', self.sub)
        self.btnmul = Button(win, text="×", command=self.mul)
        self.btnmul.place(x=210, y=200)
        #self.btnmul.bind('<Button-1>', self.mul)
        self.btndiv = Button(win, text="÷", command=self.div)
        self.btndiv.place(x=240, y=200)
        #self.btndiv.bind('<Button-1>', self.div)

#add event-handling /bind () method

    def clr(self):
        self.txt1.delete(0, 'end')
        self.txt2.delete(0, 'end')
        self.txt3.delete(0, 'end')

    def add(self):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 + num2
        self.txt3.insert(END, str(result))

    def sub(self):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 - num2
        self.txt3.insert(END, str(result))

    def mul(self):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 * num2
        self.txt3.insert(END, str(result))

    def div(self):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 / num2
        self.txt3.insert(END, str(result))

window = Tk()
mywin = MyWindow(window)
window.geometry("600x400+10+10")
window.title("Simple Calculator")
window.mainloop()