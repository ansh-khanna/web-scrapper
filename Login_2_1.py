from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import psycopg2
import Login_1_1


def new_account():
    w = Tk()
    w.geometry('350x570')
    w.title("NEW ACCOUNT PAGE")
    w.resizable(0, 0)

    # Making Connection to Online Database
    connection = psycopg2.connect(
        database="users", 
        user = "tiet", 
        password = "tiet", 
        host = "localhost", 
        port = "5432")
    cursor = connection.cursor()


    # Making gradient frame
    j = 0
    r = 10
    for i in range(100):
        c = str(222222+r)
        Frame(w, width=10, height=570, bg="#"+c).place(x=j, y=0)
        j = j+10
        r = r+1

    Frame(w, width=250, height=470, bg='white').place(x=50, y=50)

    # l1 label for username
    l1 = Label(w, text='Username', bg='white')
    l = ('Consolas', 13)
    l1.config(font=l)
    l1.place(x=80, y=200)

    # e1 entry for username entry
    e1 = Entry(w, width=20, border=0)
    l = ('Consolas', 13)
    e1.config(font=l)
    e1.place(x=80, y=230)

    # l3 label for name
    l3 = Label(w, text='Name', bg='white')
    l = ('Consolas', 13)
    l3.config(font=l)
    l3.place(x=80, y=280)

    # e2 entry for name entry
    e3 = Entry(w, width=20, border=0)
    e3.config(font=l)
    e3.place(x=80, y=310)

    # l2 label for password
    l2 = Label(w, text='Password', bg='white')
    l = ('Consolas', 13)
    l2.config(font=l)
    l2.place(x=80, y=360)

    # e2 entry for password entry
    e2 = Entry(w, width=20, border=0, show='*')
    e2.config(font=l)
    e2.place(x=80, y=390)

    # lineframe on entry

    Frame(w, width=180, height=2, bg='#141414').place(x=80, y=252)
    Frame(w, width=180, height=2, bg='#141414').place(x=80, y=332)
    Frame(w, width=180, height=2, bg='#141414').place(x=80, y=412)

    imagea = Image.open("log2.png")
    imageb = ImageTk.PhotoImage(imagea)

    label1 = Label(image=imageb, border=0, justify=CENTER)

    label1.place(x=115, y=50)

    # Command

    def cmd():
        username = e1.get()
        password = e2.get()
        name = e3.get()
        if len(username) != 0 and len(password) != 0 and len(name) != 0:
            sql = "SELECT * FROM USERS WHERE USERNAME ='" + \
                username + "'"
            cursor.execute(sql)
            myresult = cursor.fetchall()
            if len(myresult) != 0:
                messagebox.showwarning(
                    "REGISTERATION FAILED", "THIS USERNAME IS ALREADY IN USE")
            else:
                sql = "INSERT INTO USERS (username, name, password) VALUES (%s, %s, %s)"
                val = (username, name, password)
                cursor.execute(sql, val)
                messagebox.showinfo("REGISTERATION SUCCESSFULLY",
                                    "Registeration Completed! PLease Sign in Again")
                w.destroy()
                Login_1_1.login_main()
        else:
            messagebox.showwarning(
                "LOGIN FAILED", "PLEASE PROVIDE ALL THE ENTERIES")
        connection.commit()
        

    # Button_with hover effect

    def bttn(x, y, text, ecolor, lcolor):
        def on_entera(e):
            myButton1['background'] = ecolor  # ffcc66
            myButton1['foreground'] = lcolor  # 000d33

        def on_leavea(e):
            myButton1['background'] = lcolor
            myButton1['foreground'] = ecolor

        myButton1 = Button(w, text=text,
                           width=20,
                           height=2,
                           fg=ecolor,
                           border=0,
                           bg=lcolor,
                           activeforeground=lcolor,
                           activebackground=ecolor,
                           command=cmd)

        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x, y=y)

    bttn(100, 455, 'Sign Up into the Program', 'white', '#994422')

    w.mainloop()