import tkinter
from tkinter import messagebox
from tkinter import ttk
import re
import smtplib
from email.mime.multipart import MIMEMultipart     #multipurpose internet mail extension
from email.mime.text import MIMEText
import mysql.connector



def valid_mobile_number(mobile_number):
    pattern = "^[6789][0-9]{9}$"

    return re.match(pattern,mobile_number) is not None



def send_email(recipient_email, student_name):
    # Set up the server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()    #transport layer security

    # Login credentials for sending the mail
    sender_email = 'prasath21612003@gmail.com'
    sender_password = 'hiym payn mbgs bwau'

    server.login('prashanthau0510@gmail.com', 'hiym payn mbgs bwau')

    # Email content
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = 'Registration Successful'

    # mime text of the email
    body = f"Dear {student_name},\n\nYour Exam Registration was Successful!\n\nThank you for registering."
    message.attach(MIMEText(body, 'plain'))

    # Send the email
    text = message.as_string()
    server.sendmail(sender_email, recipient_email, text)

    # Disconnect from the server
    server.quit()



def communicate():

    mobile_number = e5.get()
    if not valid_mobile_number(mobile_number):
        messagebox.showerror("error","invalid mobile number.Please enter valid mobile number")
        return


    try:
        global connection 
        connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Sri@2011",
            database = "exam_registration"
        )


        #enable cursor

        mycursor = connection.cursor()


        #create database

        #mycursor.execute("create database exam_registration")

        #create table

        #mycursor.execute("create table student_information(name varchar(50),age int,gender varchar(10),nationality varchar(50),mobile_number bigint,email varchar(50),program_of_study varchar(25),year_of_study varchar(50),semester int,registration_number bigint,aadhar_number bigint)")
        

        #insert into

        insert = "insert into student_information(name,age,gender,nationality,mobile_number,email,program_of_study,year_of_study,semester,registration_number,aadhar_number) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        value = (e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),e10.get(),e11.get())
        result = mycursor.execute(insert,value)
        connection.commit()



        messagebox.showinfo("success","Registration Successfull")

        send_email(e6.get(), e1.get())
        
    except mysql.connector.Error as err:
        messagebox.showerror("error",f"unable to Register Please Try again{err}")


m = tkinter.Tk()
m.title("Exam Registration Portal")
m.geometry("700x600")
m.config(bg="sky blue")


t = tkinter.Label(text="Welcome To Examination Register Portal",font=('arial',25,'bold'),fg="black",bg="sky blue")
t.pack()


l1 = tkinter.Label(text="Name",font=("arial",10,"bold"),bg="sky blue")
l1.pack()
e1 = tkinter.Entry()
e1.pack()

l2 = tkinter.Label(text="Age",font=("arial",10,"bold"),bg="sky blue")
l2.pack()
e2 = tkinter.Spinbox(m,from_=0,to=100)
e2.pack()

l3 = tkinter.Label(text='Gender',font=("arial",10,"bold"),bg="sky blue")
l3.pack()
e3 = ttk.Combobox(m,values=["Male","Female","Transgender","Prefer Not To Say"])
e3.pack()

l4 = tkinter.Label(text="Nationality",font=("arial",10,"bold"),bg="sky blue")
l4.pack()
e4 = ttk.Combobox(m,values=["India","America","Pakistan","SriLanka","China","Israel","Russia","South Africa","Canada","Australia","Nepal","Afghanistan","Bangladesh","Maldives","Bhutan"])
e4.pack()

l5 = tkinter.Label(text='Mobile Number',font=("arial",10,"bold"),bg="sky blue")
l5.pack()
e5 = tkinter.Entry()
e5.pack()

l6 = tkinter.Label(text="Email",font=("arial",10,"bold"),bg="sky blue")
l6.pack()
e6 = tkinter.Entry()
e6.pack()

l7 = tkinter.Label(text="Program of Study",font=("arial",10,"bold"),bg="sky blue")
l7.pack()
e7 = ttk.Combobox(m,values=["B.E Civil","B.E Mechanical","B.E IT","B.sc Chemistry","B.sc Physics","BA English","BA History","BA Tamil","BBA Finance","BBA HR Management","LLB Constitutional Law","LLB Criminal Law","LLB Business Law","B.Pharm"])
e7.pack()

l8 = tkinter.Label(text="Year of Study",font=("arial",10,"bold"),bg="sky blue")
l8.pack()
e8 = ttk.Combobox(m,values=["1 Year","2 Year","3 Year","4 Year","5 Year"])
e8.pack()

l9 = tkinter.Label(text="Semester",font=("arial",10,"bold"),bg="sky blue")
l9.pack()
e9 = ttk.Combobox(m,values=["1","2","3","4","5","6","7","8","9","10"])
e9.pack()

l10 = tkinter.Label(text="Registration Number",font=("arial",10,"bold"),bg="sky blue")
l10.pack()
e10 = tkinter.Entry()
e10.pack()

l11 = tkinter.Label(text="Aadhar Number",font=("arial",10,"bold"),bg="sky blue")
l11.pack()
e11 = tkinter.Entry()
e11.pack()


b = tkinter.Button(text="Click Here To Register",command=communicate,font=("arial",10,"bold"),fg="green").pack(pady=10)

b1 = tkinter.Button(text = "Exit",command=quit,font=("arial",10,"bold"),fg="red").pack()

m.mainloop()