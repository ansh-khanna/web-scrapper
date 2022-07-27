from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import psycopg2
import Login_2_1


def login_main():
    w = Tk()
    w.geometry('350x550')
    w.title("LOGIN PAGE")
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
        Frame(w, width=10, height=550, bg="#"+c).place(x=j, y=0)
        j = j+10
        r = r+1

    Frame(w, width=250, height=450, bg='white').place(x=50, y=50)

    l1 = Label(w, text='Username', bg='white')
    l = ('Consolas', 13)
    l1.config(font=l)
    l1.place(x=80, y=200)

    # e1 entry for username entry
    e1 = Entry(w, width=20, border=0)
    l = ('Consolas', 13)
    e1.config(font=l)
    e1.place(x=80, y=230)

    # e2 entry for password entry
    e2 = Entry(w, width=20, border=0, show='*')
    e2.config(font=l)
    e2.place(x=80, y=310)

    l2 = Label(w, text='Password', bg='white')
    l = ('Consolas', 13)
    l2.config(font=l)
    l2.place(x=80, y=280)

    # lineframe on entry

    Frame(w, width=180, height=2, bg='#141414').place(x=80, y=332)
    Frame(w, width=180, height=2, bg='#141414').place(x=80, y=252)

    imagea = Image.open("log.png")
    imageb = ImageTk.PhotoImage(imagea)

    label1 = Label(image=imageb, border=0, justify=CENTER)

    label1.place(x=115, y=50)

    # Command

    def cmd():
        global t
        userid = e1.get()
        password = e2.get()
        print(userid, password)
        sql = "SELECT * FROM USERS WHERE USERNAME ='" + \
            userid + "' AND password = '" + password + "'"
        cursor.execute(sql)
        
        myresult = cursor.fetchall()
        if len(myresult) == 1:
            messagebox.showinfo("LOGIN SUCCESSFULLY",
                                "Welcome to Our Software")
            t = 1
            w.destroy()

        else:
            messagebox.showwarning(
                "LOGIN FAILED", "PLEASE TRY AGAIN")
            t = 0

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

    # Button_with hover effect

    def bttn2(x, y, text, ecolor, lcolor):
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
                           command=lambda: [w.destroy(), Login_2_1.new_account()])

        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x, y=y)

    bttn(100, 375, 'Login in the Program', 'white', '#994422')
    bttn2(100, 440, 'Create a New Account', 'white', '#994422')

    w.mainloop()
