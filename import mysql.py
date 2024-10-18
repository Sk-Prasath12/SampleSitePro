import tkinter
from tkinter import messagebox
import mysql.connector

# Connect to the database
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Sri@2011',
    database='demo'
)
mycursor = db.cursor()

# Create the table if it doesn't exist
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS demotable (
        name VARCHAR(50),
        age INT,
        country VARCHAR(25),
        username VARCHAR(20),
        password VARCHAR(50)
    )
""")
db.commit()

# Function to insert data into the database
def communicate():
    inser = 'INSERT INTO demotable (name, age, country, username, password) VALUES (%s, %s, %s, %s, %s)'
    val = (e1.get(), e2.get(), e3.get(), e4.get(), e5.get())
    
    try:
        mycursor.execute(inser, val)
        db.commit()
        messagebox.showinfo('Success', 'Table inserted successfully')
    except mysql.connector.Error as err:
        messagebox.showerror('Error', f'Unable to insert: {err}')

# Initialize Tkinter window
m = tkinter.Tk()
m.title('SQL Tkinter Project')

# Create and position labels and entry fields
l1 = tkinter.Label(m, text='Name')
l1.grid(row=0, column=0, sticky='W')
e1 = tkinter.Entry(m)
e1.grid(row=1, column=0, sticky='W')

l2 = tkinter.Label(m, text='Age')
l2.grid(row=2, column=0, sticky='W')
e2 = tkinter.Spinbox(m, from_=0, to=100)
e2.grid(row=3, column=0, sticky='W')

l3 = tkinter.Label(m, text='Country')
l3.grid(row=4, column=0, sticky='W')
e3 = tkinter.Entry(m)
e3.grid(row=5, column=0, sticky='W')

l4 = tkinter.Label(m, text='Username')
l4.grid(row=6, column=0, sticky='W')
e4 = tkinter.Entry(m)
e4.grid(row=7, column=0, sticky='W')

l5 = tkinter.Label(m, text='Password')
l5.grid(row=8, column=0, sticky='W')
e5 = tkinter.Entry(m, show='*')  # Hide password input
e5.grid(row=9, column=0, sticky='W')

# Create buttons
b1 = tkinter.Button(m, text='Click here to insert', command=communicate, bg='green')
b1.grid(row=10, column=0, sticky='W')
b2 = tkinter.Button(m, text='Exit', command=m.quit, bg='red')
b2.grid(row=11, column=0, sticky='W')

m.mainloop()

# Close the database connection when done
db.close()
