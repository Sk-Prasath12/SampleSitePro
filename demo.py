import tkinter
from tkinter import messagebox
import mysql.connector

def communicate():
    try:
        global Connection
        connection=mysql.connector.connect(
            host='localhost',
            user='root',
            password='Sri@2011',
            database='demo'
        )

        cursor=connection.cursor()

        #create db
        #cursor.execute('create database demo')

        #create table
        cursor.execute('create table demotable(name varchar(50),age int,country varchar(25),username varchar(20),password varchar(50))')

        #insert 

        inser = 'insert into demotable(name,age,country,username,password) values (%s,%s,%s,%s,%s)'
        val = (e1.get(),e2.get(),e3.get(),e4.get(),e5.get())
        result=cursor.execute(inser,val)
        connection.commit()

        messagebox.showinfo('succesess','table inserted successfull')
    except mysql.connector.Error as err:
        messagebox.showerror('Error',f'unable to insert: {err}')

m = tkinter.Tk()
m.title('sqltkproject')

l1 = tkinter.Label(m,text='name')
l1.grid(row=0,column=0,sticky='W')
e1= tkinter.Entry()
e1.grid(row=1,column=0,sticky='W')

l2 = tkinter.Label(text='age')
l2.grid(row=2,column=0,sticky='W')
e2=tkinter.Spinbox(from_=0,to=100)
e2.grid(row=3,column=0,sticky='W')

l3 = tkinter.Label(text='country')
l3.grid(row=4,column=0,sticky='W')
e3=tkinter.Entry()
e3.grid(row=5,column=0,sticky='W')

l4 = tkinter.Label(text='username')
l4.grid(row=6,column=0,sticky='W')
e4=tkinter.Entry()
e4.grid(row=7,column=0,sticky='W')

l5 = tkinter.Label(text='password')
l5.grid(row=8,column=0,sticky='W')
e5=tkinter.Entry()
e5.grid(row=9,column=0,sticky='W')


b1 = tkinter.Button(m,text='click here to insert',command=communicate,bg='green')
b1.grid(row=10,column=0,sticky='W')
b2 = tkinter.Button(m,text='Exit',command=quit,bg='red')
b2.grid(row=11,column=0,sticky='W')
m.mainloop()