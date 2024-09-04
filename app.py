import tkinter as tk
from tkinter import Frame, Listbox, BOTH
from tkinter import END,messagebox


root = tk.Tk()
root.title("To-Do-List")
root.geometry("400x900")
root.resizable(False, False)
root.config(bg='white')

task_que,undo_stack=[],[]
top,rear=-1,0

def addTask():
    global rear
    task = task_entry.get()
    task_entry.delete(0, tk.END)
    if task:
        f=open("hello.txt", 'w')
        f.write(f"\n{task}")
        task_que.append(task)
        rear+=1
        listbox.insert(tk.END, task)

def deleteTask():
    global rear
    if rear>=0 and len(task_que)!=0:
        pp=task_que.pop(0)
        f=open("hello.txt", 'w')
        listbox.delete(0)
        f.writelines(task_que)
        undo_stack.append(pp)
    else:
        p=tk.messagebox.showwarning(Warning,'THERE IS NO ITEMS TO DELETE')

def undoDelete():
    if len(undo_stack)!=0:
        global front,rear
        task = undo_stack.pop(-1)
        task_que.append(task)
        f=open("hello.txt", 'w')
        f.writelines(task_que)
        listbox.insert(0, task)
    else:
        z=tk.messagebox.showwarning(Warning,"PLEASE DELETE SOMETHING FIRST AND THEN CLICK UNDO")
    



# icon
Image_icon = tk.PhotoImage(file="gouri.png")
root.iconphoto(False, Image_icon)

# top_bar
TopImage = tk.PhotoImage(file="topbar.png")
tk.Label(root, image=TopImage).pack()

heading=tk.Label(root,text="TO-DO-LIST",font=("Arial",30),bg='orange').place(x=80,y=100)



task_entry = tk.Entry(root, width=25, font="Arial 14", bd=0,bg='black',fg='yellow')
task_entry.place(x=20, y=360)
task_entry.focus()


button = tk.Button(root, text="ADD", font="Arial", bg="#5a95ff", fg="#fff", bd=0, command=lambda:addTask())
button.place(x=320, y=350)

# listbox
frame1 = tk.Frame(root, bd=3, width=700, height=120, bg="yellow")
frame1.place(x=0,y=400)

listbox = tk.Listbox(frame1, font=('Arial', 12), width=40, height=8, bg="#32405b", fg="white", cursor="hand2",
                  selectbackground="#5a95ff")
listbox.pack(side=tk.LEFT, fill=BOTH, padx=2)

scrollbar = tk.Scrollbar(frame1)
scrollbar.pack(side=tk.RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)


# delete button
Delete_icon = tk.PhotoImage(file="delete2.png")
resized_delete_icon = Delete_icon.subsample(2, 2)  # Change the subsample factor as needed
tk.Button(root, image=resized_delete_icon, bd=0, command=lambda:deleteTask()).place(x=50,y=600)


# undo button
Undo_icon = tk.PhotoImage(file="undo.png")
resized_undo_icon = Undo_icon.subsample(2, 2)  # Change the subsample factor as needed
tk.Button(root, image=resized_undo_icon, bd=0, command=lambda:undoDelete()).place(x=200,y=620)


root.mainloop()