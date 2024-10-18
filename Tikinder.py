import tkinter as tk
from tkinter import messagebox

# Create the main application window
m = tk.Tk()
m.title("Signup Form")

# Labels
l1 = tk.Label(m, text='Name')
l1.grid(row=0, column=0, sticky='W', padx=5, pady=5)

l2 = tk.Label(m, text='Age')
l2.grid(row=2, column=0, sticky='W', padx=5, pady=5)

l3 = tk.Label(m, text='DOB')
l3.grid(row=4, column=0, sticky='W', padx=5, pady=5)

l4 = tk.Label(m, text='Username')
l4.grid(row=6, column=0, sticky='W', padx=5, pady=5)

l5 = tk.Label(m, text='Password')
l5.grid(row=8, column=0, sticky='W', padx=5, pady=5)

# Entry fields
e1 = tk.Entry(m)
e1.grid(row=1, column=0, sticky='W', padx=5, pady=5)

sb = tk.Spinbox(m, from_=0, to=100)
sb.grid(row=3, column=0, sticky='W', padx=5, pady=5)

e3 = tk.Entry(m)
e3.grid(row=5, column=0, sticky='W', padx=5, pady=5)

e4 = tk.Entry(m)
e4.grid(row=7, column=0, sticky='W', padx=5, pady=5)

e5 = tk.Entry(m, show='*')  # Hide password input
e5.grid(row=9, column=0, sticky='W', padx=5, pady=5)

# Signup button
def communicate():
    messagebox.showinfo("Signup", "You signed up successfully!")

b = tk.Button(m, text='Signup', command=communicate, bg='green')
b.grid(row=11, column=0, sticky='W', padx=5, pady=5)

# Exit button
b1 = tk.Button(m, text='EXIT', command=m.destroy, bg='red')
b1.grid(row=11, column=1, sticky='W', padx=5, pady=5)

# Start the main event loop
m.mainloop()
