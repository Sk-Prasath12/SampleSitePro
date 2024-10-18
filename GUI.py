from tkinter import *

def create_main_window():
    # Initialize the main root window
    root = Tk()
    root.title("Main Window")

    # Create and place labels and entry widgets
    Label(root, text='First Name').grid(row=0, column=0, padx=10, pady=5)
    Label(root, text='Last Name').grid(row=1, column=0, padx=10, pady=5)

    e1 = Entry(root)
    e2 = Entry(root)
    e1.grid(row=0, column=1, padx=10, pady=5)
    e2.grid(row=1, column=1, padx=10, pady=5)

    # Create a Listbox
    L = Listbox(root)
    L.insert(1, 'Python')
    L.insert(2, 'Java')
    L.insert(3, 'C')
    L.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

    # Create a Text widget
    text = Text(root, height=4, width=40)
    text.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
    text.insert(END, 'Python is a language')

    # Create a Message widget
    msg = "This is a message"
    M1 = Message(root, text=msg, bg='green')
    M1.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

    # Create Frames and Buttons
    frame = Frame(root)
    frame.grid(row=5, column=0, padx=10, pady=5, sticky=W)
    redbutton = Button(frame, text='Red', fg='red')
    redbutton.pack(side=LEFT)

    bottomframe = Frame(root)
    bottomframe.grid(row=5, column=1, padx=10, pady=5, sticky=E)
    blackbutton = Button(bottomframe, text='Black', fg='black')
    blackbutton.pack(side=LEFT)

    # Create Scales
    w = Scale(root, from_=0, to=30)
    w.grid(row=6, column=0, padx=10, pady=5)

    w1 = Scale(root, from_=0, to=20, orient=HORIZONTAL)
    w1.grid(row=6, column=1, padx=10, pady=5)

    # Create a Spinbox
    spinbox = Spinbox(root, from_=10, to=50)
    spinbox.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

    # Create a Toplevel window
    top = Toplevel(root)
    top.title('Toplevel Window')
    Label(top, text='This is a Toplevel window').pack(padx=10, pady=10)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    create_main_window()
