from tkinter import *
from tkinter import messagebox
from random import randint
root = Tk()
root.title("Password Generator")
root.geometry("340x190")
root.resizable(False,False)
root.iconbitmap("psgn.ico")
L1 = Label(root,text="Enter the lenght of your password  ").grid(row=0,column=0,padx=5)
E1 = Entry(root,width = 20)
E1.grid(row=0,column=1,pady=20)
L2 = Label(root,text="Your password is  ").grid(row=1,column=0)
E2 = Entry(root,width = 20,bg="systembuttonface",bd=0)
E2.grid(row=1,column=1,pady=15)
def pswd():
      if E1.get() == "":
          E2.delete(0,END)
          messagebox.showerror("Passsword generator","Empty entry")
      n = int(E1.get())
      password = ''
      for i in range(n):
          password += chr((randint(33,126)))
      E2.delete(0,END)
      E2.insert(0,password)

def clp():
       root.clipboard_clear()
       root.clipboard_append(E2.get())

    
B1 = Button(root,text="Generate password",command= pswd).grid(row=2,column=0,pady=15)
B2 = Button(root,text="Copy to clipboard",command=clp).grid(row=2,column=1,pady=15)


root.mainloop()
