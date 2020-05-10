from tkinter import *
import smtplib
from tkinter import messagebox

root = Tk()
root.title("Gmail")

sender_Email = StringVar()
sender_pass = StringVar()
rec_Email = StringVar()
mess_body = None


def layer():
    menuber = Menu(root)
    menuber.add_command(label="Instruction", command=instruction)
    menuber.add_command(label="About", command=about)
    root.config(menu = menuber)

    send_gamil = Label(root, text="Sender Gmail : ")
    send_entry = Entry(root, textvariable = sender_Email,width=25,bd=4)

    send_pass = Label(root, text="Sender Password : ")
    send_psentry = Entry(root,show="*", textvariable=sender_pass, width=25,bd=4)

    check_bu = Button(root, text="Check Connection", width=15, command=check_conn, bd=5)

    Empt = Label(root, text="")

    recv_gmail = Label(root, text="Receiver Gmail : ")
    recv_entry = Entry(root, textvariable=rec_Email, width=25,bd=4)

    mess_lb = Label(root, text="Message : ")
    global mess_body
    mess_body = Text(root, height=5, width=19, bd=4)

    send_bu = Button(root, text="Send",width=15, command=send, bd=5)
    exit_bu = Button(root, text="Exit",width=15, command=cancel, bd=5)

    send_gamil.grid(row=0,column=0,padx=5,pady=3)
    send_entry.grid(row=0, column=1, padx=5, pady=3)

    send_pass.grid(row=1, column=0, padx=5, pady=3)
    send_psentry.grid(row=1, column=1, padx=5, pady=3)

    check_bu.grid(row=2, column=1, padx=5, pady=3)
    Empt.grid(row=3, column=0, padx=5, pady=3)

    recv_gmail.grid(row=4, column=0, padx=5, pady=3)
    recv_entry.grid(row=4, column=1, padx=5, pady=3)

    mess_lb.grid(row=5, column=0, padx=5, pady=3)
    mess_body.grid(row=5, column=1, padx=5, pady=3)

    send_bu.grid(row=6, column=0, padx=5, pady=3)
    exit_bu.grid(row=6, column=1, padx=5, pady=3)
    root.mainloop()


# server = smtplib.SMTP("smtp.gmail.com", 587)
# server.starttls()
# a = sender_Email.get()
# b=sender_pass.get()
# c=rec_Email.get()
# d=mess_body.get("1.0", END)


def check_conn():
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        a = sender_Email.get()
        b = sender_pass.get()
        server.login(a, b)
        messagebox.showinfo("Connection","Connection completed")
    except Exception as err:
        messagebox.showwarning("Error", """
        Connection problem
            
            i) please check your internet conncetion.  
           ii) Fillup the above box.
          iii) Check User name and password 
           iv) Read the 'Instruction' message.""")

def send():
    try:
        if sender_Email=="" or sender_pass=="" or rec_Email=="":
            messagebox.showerror("Error", "Please fill up the TextBox.")
        else:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            a = sender_Email.get()
            b=sender_pass.get()
            c=rec_Email.get()
            d=mess_body.get("1.0", END)
            server.login(a,b)
            server.sendmail(a,c,d)
            server.close()
            mess_box()
    except Exception as error:
        messagebox.showwarning("Warning", 'Read the "Check Connection" message.')

def mess_box():
    messagebox.showinfo("Mail Infomation","Mail send Successfully.")

def cancel():
    a = messagebox.askokcancel("Exit", "Do you want to exit?")
    if a:
        root.destroy()


def instruction():
    messagebox.showinfo("Instruction","\tbefore using the app!!\n\nswitch 'allow less secure apps' to ON from\nhttps://myaccount.google.com/u/0/security?hl=en&pli=1#connectedapps")


def about():
    messagebox.showinfo("About","This app is for only educational purpose\n\n\tCreated by Golam Mostafa rabbi.")


layer()
