from tkinter import *
root = Tk()
root.title("Calculator")
root.iconbitmap("calculator.ico")
root.resizable(False,False)
E = Entry(root, borderwidth=5,width=35)
E.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
def click(num):
    C = E.get()
    E.delete(0,END)
    E.insert(0,str(C)+str(num))

def add():
    global operation
    operation = "Add"
    first_num = E.get()
    E.delete(0,END)
    global num1
    num1 = float(first_num)

def sub():
    global operation
    operation = "Sub"
    first_num = E.get()
    E.delete(0, END)
    global num1
    num1 = float(first_num)

def mul():
    global operation
    operation = "Multiply"
    first_num = E.get()
    E.delete(0, END)
    global num1
    num1 = float(first_num)

def div():
    global operation
    operation = "Divide"
    first_num = E.get()
    E.delete(0, END)
    global num1
    num1 = float(first_num)

def percentage():
    global operation
    operation = "Percentage"
    first_num = E.get()
    E.delete(0, END)
    global num1
    num1 = float(first_num)

def sqrt():
   first_num = E.get()
   sqroot = float(first_num)**0.5
   E.delete(0, END)
   E.insert(0, sqroot)

def square():
    first_num = E.get()
    square = float(first_num) ** 2
    E.delete(0, END)
    E.insert(0, square)

def point():
    E.insert(len(E.get()), ".")

def equal():
    sec_num = E.get()
    E.delete(0,END)
    if (operation  == "Add"):
        E.insert(0,num1+float(sec_num))
    elif (operation == "Sub"):
        E.insert(0, num1 - float(sec_num))
    elif (operation == "Multiply"):
        E.insert(0, num1 * float(sec_num))
    elif (operation == "Divide"):
        try:
           E.insert(0, num1 / float(sec_num))
        except ZeroDivisionError:
           E.insert(0,"Divide by Zero Error")


    elif (operation == "Percentage"):
        E.insert(0,(num1*100)/float(sec_num))




def clear():
    E.delete(0,END)

B1 = Button(root,text="1",padx=35,pady=15,command= lambda: click(1))
B1.grid(row=3,column=0)
B2 = Button(root,text="2",padx=35,pady=15,command= lambda: click(2))
B2.grid(row=3,column=1)
B3 = Button(root,text="3",padx=35,pady=15,command= lambda: click(3))
B3.grid(row=3,column=2)
B4 = Button(root,text="4",padx=35,pady=15,command= lambda: click(4))
B4.grid(row=2,column=0)
B5 = Button(root,text="5",padx=35,pady=15,command= lambda: click(5))
B5.grid(row=2,column=1)
B6 = Button(root,text="6",padx=35,pady=15,command= lambda: click(6))
B6.grid(row=2,column=2)
B7 = Button(root,text="7",padx=35,pady=15,command= lambda: click(7))
B7.grid(row=1,column=0)
B8 = Button(root,text="8",padx=35,pady=15,command= lambda: click(8))
B8.grid(row=1,column=1)
B9 = Button(root,text="9",padx=35,pady=15,command= lambda: click(9))
B9.grid(row=1,column=2)
B0 = Button(root,text="0",padx=35,pady=15,command= lambda: click(0))
B0.grid(row=4,column=0)
B_plus = Button(root,text="+",padx=33,pady=15,command= add)
B_plus.grid(row=2,column=3)
B_div = Button(root,text="/",padx=35,pady=15,command= div)
B_div.grid(row=4,column=2)
B_percentage = Button(root,text="%",padx=33,pady=15,command=percentage)
B_percentage.grid(row=5,column=0)
B_mul = Button(root,text="*",padx=36,pady=15,command= mul)
B_mul.grid(row=4,column=3)
B_minus = Button(root,text="-",padx=35,pady=15,command= sub)
B_minus.grid(row=3,column=3)
B_point = Button(root,text=".",padx=36,pady=15,command=point)
B_point.grid(row=4,column=1)
B_equal = Button(root,text="=",padx=34,pady=15,command=equal)
B_equal.grid(row=5,column=3)
B_clear = Button(root,text="clear",padx=25,pady=15,command=clear)
B_clear.grid(row=1,column=3)
B_rt = Button(root,text="√",padx=33,pady=15,command=sqrt)
B_rt.grid(row=5,column=1)
B_square = Button(root,text="x²",padx=33,pady=15,command=square)
B_square.grid(row=5,column=2)

root.mainloop()
