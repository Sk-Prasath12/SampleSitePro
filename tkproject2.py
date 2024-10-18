import mysql.connector
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to_email, subject, body):
    from_email = "prasath21612003@gmail.com"  # Replace with your email
    password = "hiym payn mbgs bwau"             # Replace with your email password

    # Set up the server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    
    try:
        server.login(from_email, password)

        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'plain'))
        
        server.send_message(msg)
        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {e}")

    finally:
        server.quit()

def communicate():
    try:
        # Gather values from the entry fields
        values = (
            e1.get(),
            e2.get(),
            e3.get(),
            e4.get(),
            e5.get(),
            e6.get(),
            e7.get(),
            e8.get(),
            e9.get(),
            e10.get(),
            e11.get()
        )

        # Prepare the insert statement
        insert = """INSERT INTO student_information 
                    (name, age, gender, nationality, mobile_number, email, 
                     program_of_study, year_of_study, semester, 
                     registration_number, aadhar_number) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        # Execute the insertion
        mycursor.execute(insert, values)
        connection.commit()

        messagebox.showinfo("Success", "Registration successful!")

        # Send confirmation email
        email_body = f"Hello {e1.get()},\n\nThank you for registering!\n\nBest regards,\nYour Registration Team"
        send_email(e6.get(), "Registration Confirmation", email_body)

        # Clear entry fields after successful registration
        clear_entries()

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

def clear_entries():
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    e3.set('')
    e4.set('')
    e5.delete(0, tk.END)
    e6.delete(0, tk.END)
    e7.set('')
    e8.set('')
    e9.set('')
    e10.delete(0, tk.END)
    e11.delete(0, tk.END)

# Initialize the Tkinter application
m = tk.Tk()
m.title("Student Registration Portal")
m.geometry("400x600")
m.config(bg="sky blue")

# Connect to MySQL database
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sri@2011",
        database="prasath"
    )
    mycursor = connection.cursor()
except mysql.connector.Error as err:
    messagebox.showerror("Connection Error", f"Could not connect to the database: {err}")
    m.destroy()

# Welcome label
t = tk.Label(m, text="Welcome To Examination Register Portal", font=('arial', 25, 'bold'), fg="black", bg="red")
t.pack()

# Input fields
l1 = tk.Label(m, text="Name", font=("arial", 10, "bold"), bg="sky blue")
l1.pack()
e1 = tk.Entry(m)
e1.pack()

l2 = tk.Label(m, text="Age", font=("arial", 10, "bold"), bg="sky blue")
l2.pack()
e2 = tk.Spinbox(m, from_=0, to=100)
e2.pack()

l3 = tk.Label(m, text='Gender', font=("arial", 10, "bold"), bg="sky blue")
l3.pack()
e3 = ttk.Combobox(m, values=["Male", "Female", "Transgender", "Prefer Not To Say"])
e3.pack()

l4 = tk.Label(m, text="Nationality", font=("arial", 10, "bold"), bg="sky blue")
l4.pack()
e4 = ttk.Combobox(m, values=["India", "America", "Pakistan", "SriLanka", "China", "Israel", "Russia", "South Africa", "Canada", "Australia", "Nepal", "Afghanistan", "Bangladesh", "Maldives", "Bhutan"])
e4.pack()

l5 = tk.Label(m, text='Mobile Number', font=("arial", 10, "bold"), bg="sky blue")
l5.pack()
e5 = tk.Entry(m)
e5.pack()

l6 = tk.Label(m, text="Email", font=("arial", 10, "bold"), bg="sky blue")
l6.pack()
e6 = tk.Entry(m)
e6.pack()

l7 = tk.Label(m, text="Program of Study", font=("arial", 10, "bold"), bg="sky blue")
l7.pack()
e7 = ttk.Combobox(m, values=["B.E Civil", "B.E Mechanical", "B.E IT", "B.sc Chemistry", "B.sc Physics", "BA English", "BA History", "BA Tamil", "BBA Finance", "BBA HR Management", "LLB Constitutional Law", "LLB Criminal Law", "LLB Business Law", "B.Pharm"])
e7.pack()

l8 = tk.Label(m, text="Year of Study", font=("arial", 10, "bold"), bg="sky blue")
l8.pack()
e8 = ttk.Combobox(m, values=["1 Year", "2 Year", "3 Year", "4 Year", "5 Year"])
e8.pack()

l9 = tk.Label(m, text="Semester", font=("arial", 10, "bold"), bg="sky blue")
l9.pack()
e9 = ttk.Combobox(m, values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
e9.pack()

l10 = tk.Label(m, text="Registration Number", font=("arial", 10, "bold"), bg="sky blue")
l10.pack()
e10 = tk.Entry(m)
e10.pack()

l11 = tk.Label(m, text="Aadhar Number", font=("arial", 10, "bold"), bg="sky blue")
l11.pack()
e11 = tk.Entry(m)
e11.pack()

# Buttons
b = tk.Button(m, text="Click Here To Register", command=communicate, font=("arial", 10, "bold"), fg="green")
b.pack(pady=10)

b1 = tk.Button(m, text="Exit", command=m.quit, font=("arial", 10, "bold"), fg="red")
b1.pack()

# Start the Tkinter event loop
m.mainloop()

# Close the database connection on exit
if 'connection' in locals() and connection.is_connected():
    connection.close()
