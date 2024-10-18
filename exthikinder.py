import tkinter as tk
from tkinter import messagebox
import sqlite3

# Create a database or connect to one
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Create a table
c.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL)''')
conn.commit()

# Function to add a user
def add_user():
    try:
        c.execute("INSERT INTO users (name, age, username, password) VALUES (?, ?, ?, ?)",
                  (entry_name.get(), entry_age.get(), entry_username.get(), entry_password.get()))
        conn.commit()
        messagebox.showinfo("Success", "User added successfully!")
        clear_entries()
        view_users()
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists!")

# Function to view users
def view_users():
    for row in tree.get_children():
        tree.delete(row)
    
    c.execute("SELECT * FROM users")
    for row in c.fetchall():
        tree.insert("", "end", values=row)

# Function to update user
def update_user():
    selected_item = tree.selection()[0]
    user_id = tree.item(selected_item, 'values')[0]
    c.execute("UPDATE users SET name=?, age=?, username=?, password=? WHERE id=?",
              (entry_name.get(), entry_age.get(), entry_username.get(), entry_password.get(), user_id))
    conn.commit()
    messagebox.showinfo("Success", "User updated successfully!")
    clear_entries()
    view_users()

# Function to delete user
def delete_user():
    selected_item = tree.selection()[0]
    user_id = tree.item(selected_item, 'values')[0]
    c.execute("DELETE FROM users WHERE id=?", (user_id,))
    conn.commit()
    messagebox.showinfo("Success", "User deleted successfully!")
    view_users()

# Function to clear input fields
def clear_entries():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)

# Setup the main application window
app = tk.Tk()
app.title("User Management")

# Input fields
tk.Label(app, text="Name").grid(row=0, column=0)
entry_name = tk.Entry(app)
entry_name.grid(row=0, column=1)

tk.Label(app, text="Age").grid(row=1, column=0)
entry_age = tk.Entry(app)
entry_age.grid(row=1, column=1)

tk.Label(app, text="Username").grid(row=2, column=0)
entry_username = tk.Entry(app)
entry_username.grid(row=2, column=1)

tk.Label(app, text="Password").grid(row=3, column=0)
entry_password = tk.Entry(app, show='*')
entry_password.grid(row=3, column=1)

# Buttons
tk.Button(app, text="Add User", command=add_user).grid(row=4, column=0)
tk.Button(app, text="Update User", command=update_user).grid(row=4, column=1)
tk.Button(app, text="Delete User", command=delete_user).grid(row=4, column=2)

# Treeview for displaying users
tree = tk.ttk.Treeview(app, columns=('ID', 'Name', 'Age', 'Username', 'Password'), show='headings')
tree.heading('ID', text='ID')
tree.heading('Name', text='Name')
tree.heading('Age', text='Age')
tree.heading('Username', text='Username')
tree.heading('Password', text='Password')

tree.bind('<Double-1>', lambda e: populate_entries(tree.selection()[0]))

tree.grid(row=5, column=0, columnspan=3)

def populate_entries(selected_item):
    item = tree.item(selected_item)
    entry_name.delete(0, tk.END)
    entry_name.insert(0, item['values'][1])
    entry_age.delete(0, tk.END)
    entry_age.insert(0, item['values'][2])
    entry_username.delete(0, tk.END)
    entry_username.insert(0, item['values'][3])
    entry_password.delete(0, tk.END)
    entry_password.insert(0, item['values'][4])

# Initial view
view_users()

# Start the main loop
app.mainloop()

# Close the database connection when done
conn.close()
