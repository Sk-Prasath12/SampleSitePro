#entry- it accepts input from the user
from tkinter import *
root=Tk()
Label(root,text='First_name').grid(row=0)
Label(root,text='Last_name').grid(row=1)
e1=Entry(root)
e2=Entry(root)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
mainloop()

#listbox
from tkinter import *
top=Tk()
L=Listbox(top)
L.insert(1,'python')
L.insert(2,'java')
L.insert(3,'C')
L.pack()
mainloop()

#text
from tkinter import *
master=Tk()
text=Text(master)
text.pack()
text.insert(END,'python is a language')
mainloop()

#message
from tkinter import *
master=Tk()
msg="this is a message"
M1=Message(master,text=msg)
M1.config(bg='green')
M1.pack()
mainloop()

#frame
from tkinter import *
master=Tk()
frame=Frame(master)
frame.pack(side=LEFT)
redbutton=Button(frame,text='red',fg='red')
redbutton.pack(side=LEFT)
#2
bottomframe=Frame(master)
bottomframe.pack(side=BOTTOM)
blackbutton=Button(bottomframe,text='black',fg='black')
blackbutton.pack(side=BOTTOM)
mainloop()

#scale
from tkinter import *
master=Tk()
w=Scale(master,from_=0,to=30)
w.pack()
w1=Scale(master,from_=0,to=20,orient=HORIZONTAL)
w1.pack()
mainloop()

#spinbox

from tkinter import *
master=Tk()
w=Spinbox(master,from_=10,to=50)
w.pack()
mainloop()

#toplevel

from tkinter import *
master=Tk()
master.title('python')
master=Toplevel()
master.title('program')
mainloop()