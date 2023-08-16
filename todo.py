from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("To-do list")
root.iconbitmap("lists.ico")
root.geometry("283x310")
root.resizable(False,False)
E = Entry(root,width = 40)
E.grid(row=0,column=0,columnspan=3,padx=10,pady=5)

F = Frame(root)
F.grid(row=1,column=0,columnspan=3,padx=11)
L = Listbox(F,width = 40)

scroll = Scrollbar(F,orient=VERTICAL)
scroll.pack(side=RIGHT,fill=Y)
scroll.config(command = L.yview)

scrollx = Scrollbar(F,orient = HORIZONTAL)
scrollx.pack(side = BOTTOM,fill= X)
scrollx.config(command = L.xview)
    
L.config(yscrollcommand=scroll.set,xscrollcommand=scrollx.set)

L.pack(pady=10)

def Add():
    if E.get() == "":
      messagebox.showerror("Error","Empty entry")
    else:  
      L.insert(0,E.get())
      E.delete(0,END)


B_add=Button(root,text="Add",padx=15,command=Add)
B_add.grid(row=2,column=0,padx=10)

def edit():
    E.insert(0,L.get(ANCHOR))
    L.delete(ANCHOR)

B_edit = Button(root,text="Edit",padx=15,command=edit)
B_edit.grid(row=2,column=1,padx=10)


def delete():
    L.delete(ANCHOR)
             
B_delete = Button(root,text="Delete",padx=13,command=delete)
B_delete.grid(row=2,column=2,padx=10)

def deleteAll():
    L.delete(0,END)
    with open("todo.txt","w") as file:
      file.close()
B_deleteall = Button(root,text="Delete All",command=deleteAll)
B_deleteall.grid(row=3,column=1,pady=10)



root.mainloop()
