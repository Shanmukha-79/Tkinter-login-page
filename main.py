import tkinter
from tkinter import messagebox


window=tkinter.Tk()
window.title("Login form")
window.geometry('340x440')
window.configure(bg='#333333')

def login():
    username="Shanmukha"
    password="12345"
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Login success",message="You have logged in successfully.")
    else:
        messagebox.showerror(title="Error",message="Invalid Login.")

Frame=tkinter.Frame(bg='#333333')

#creating widgets
login_label=tkinter.Label(Frame, text="Login",bg='#333333',fg='#FF3399',font=("Arial",30))
username_label=tkinter.Label(Frame, text="Username",bg='#333333',fg='#FFFFFF',font=("Arial",16))
username_entry=tkinter.Entry(Frame,font=("Arial",16))
password_entry=tkinter.Entry(Frame, show="*",font=("Arial",16))
password_label=tkinter.Label(Frame, text="password",bg='#333333',fg='#FFFFFF',font=("Arial",16))
login_button=tkinter.Button(Frame, text="Login",bg='#FF3399',fg='#FFFFFF',font=("Arial",16),command=login)

#Placing widges on the screen
login_label.grid(row=0, column=0,columnspan=2,sticky="news",pady='40')
username_label.grid(row=1,column=0)
username_entry.grid(row=1,column=1,pady=20)
password_label.grid(row=2,column=0)
password_entry.grid(row=2,column=1,pady=20)
login_button.grid(row=3, column=0, columnspan=2,pady=30)

Frame.pack()


window.mainloop()