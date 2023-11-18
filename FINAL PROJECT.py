import tkinter
from tkinter import *
from tkinter import messagebox
import sqlite3
from PIL import Image, ImageTk
import sqlite3


def login_home():
    sign_in_frame.pack_forget()
    frame.place(x=480,y=200)
    root.update()


def login():
    if log_in_validation():
        frame.pack_forget()
        home()
    else:
        login_home()

def _log():
    frame.place(x=480, y=200)
    sign_in_frame.place_forget()


def log_in_validation():
    con = sqlite3.connect("Accounts.db")
    c = con.cursor()

    c.execute("SELECT * FROM accounts")

    x = username_entry.get() + password_entry.get()

    for acc in c.fetchall():

        if username_entry.get() == acc[1] and password_entry.get() == acc[2]:

            messagebox.showinfo("LOGIN SUCCESSFUL!", "YOU HAVE LOGGED IN!")

            return True

        else:
            messagebox.showinfo(title='INVALID LOGIN', message="PLEASE TRY AGAIN.")
            return False
    con.commit()
    con.close()


def home():
    start_window.pack()


def sign_validation():
    pass


def signin():
    frame.pack_forget()
    sign_in_frame.place(x=480, y=200)


def show():
    password_entry.config(show="")
    show_button.config(command=hide)


def hide():
    password_entry.config(show="*")
    show_button.config(command=show)


def insert_data():
    if not (signin_username_entry.get() == "" and signin_password_entry.get() == "" and confirm_entry.get() == ""):

        if (signin_password_entry.get() == confirm_entry.get()):
            con = sqlite3.connect("Accounts.db")
            c = con.cursor()
            c.execute("INSERT INTO Accounts (username, password) VALUES (?,?)",
                      (signin_username_entry.get(), signin_password_entry.get(),))
            con.commit()
            con.close()
            messagebox.showinfo("SUCCESS", "SIGN IN SUCCESSFUL")


def home_enter():
    start_window.pack_forget()
    frame.pack_forget()
    home_window.pack()


def back():
    objective_1.pack_forget()
    home_window.pack()

def Chapter_1():
    home_window.pack_forget()
    objective_1.pack(expand=True, fill=BOTH)


def ct_btn():
    home_window.pack_forget()
    topic_con_btns.pack(expand=True, fill=BOTH)


############################start


root = Tk()

window = root
window.title("Login Form")
window.geometry("1280x980")
winBG = ImageTk.PhotoImage(file='C:/Users/kenneth/Pictures/Saved Pictures/BG3.jpg')
winBg = Label(window, image=winBG)
winBg.place(x=0, y=0)

logbg = Image.open("C:/Users/kenneth/Pictures/Saved Pictures/loginbutton.png")
logbg = logbg.resize((90, 60))
logbg = ImageTk.PhotoImage(logbg)

######################login

frame = Canvas(root)
frame.config(bg="BLACK")
frame.place(x=480, y=200)

############binding


f1 = frame.create_image(100, 165, image=logbg)
frame.tag_bind(f1, "<Button>", lambda event: login())

###################Label

login_label = Label(frame, text='LOGIN', bg="BLACK", fg="GRAY", font=("Arial", 15))
login_label.grid(row=5, column=0, columnspan=2, sticky="news", pady=10)
username_label = Label(frame, text='USERNAME', bg="BLACK", fg="GRAY", font=("Arial", 10))
username_label.grid(row=6, column=0)
password_label = Label(frame, text="PASSWORD", bg="BLACK", fg="GRAY", font=("Arial", 10))
password_label.grid(row=7, column=0)

#######################Entry

username_entry = Entry(frame)
username_entry.grid(row=6, column=1, pady=10)
password_entry = Entry(frame)
password_entry.grid(row=7, column=1, pady=10)

#####################Button


# login_button = Button(frame, command=login, text="LOGIN", font=("Arial", 10))
# login_button.grid(row=9, column=0, padx=10, pady=20)
sign_up_button = Button(frame, text="SIGN UP", command=signin, bg="GRAY", fg="BLACK", font=("Arial", 10))
sign_up_button.grid(row=9, column=1, padx=10, pady=20)
show_button = Button(frame, command=hide)
show_button.grid(row=7, column=2, pady=10)

##########################signin

sign_in_frame = Frame(root)
sign_in_frame.config(bg="BLACK")
#sign_in_frame.place(x=480, y=200)

#######################SLabel

signup_label = Label(sign_in_frame, text='CREATE AN ACCOUNT', bg='WHITE', fg='BLUE', font=('Arial', 10))
signup_label.grid(row=0, column=0, columnspan=2, pady=30)
username_label = Label(sign_in_frame, text='ENTER YOUR USERNAME', bg="BLACK", fg="BLUE", font=("Arial", 10))
username_label.grid(row=6, column=0)
password_label = Label(frame, text="ENTER YOUR PASSWORD", bg="BLACK", fg="BLUE", font=("Arial", 10))
password_label.grid(row=7, column=0)
confirm_label = Label(sign_in_frame, text="CONFIRM PASSWORD", bg='BLACK', fg='BLUE', font=('Arial', 10))
confirm_label.grid(row=8, column=0)
already = Label(sign_in_frame, text='Already have an account?', font=('Arial', 8))
already.grid(row=14, column=0)

#########################SEntry


signin_username_entry = Entry(sign_in_frame)
signin_username_entry.grid(row=6, column=1, pady=10)
signin_password_entry = Entry(sign_in_frame)
signin_password_entry.grid(row=7, column=1, pady=10)
confirm_entry = Entry(sign_in_frame)
confirm_entry.grid(row=8, column=1, pady=10)

###################SButton

check = IntVar()
taC = Checkbutton(sign_in_frame, text="I Agree to the Terms and Conditions", variable=check, font=('Arial', 7),
                  cursor='hand2')
taC.grid(row=10, column=1)
sign1 = Button(sign_in_frame, text='SIGN UP', font=('Arial', 12), bg='BLACK', fg='BLUE', command=insert_data)
sign1.grid(row=12, column=0, columnspan=2, pady=20)
log = Button(sign_in_frame, text='Log in', font=('Arial', 8), bg='BLACK', fg='BLUE', cursor="hand2", command=lambda: _log())
log.grid(row=14, column=1)

###############STARTING WINDOW


start_window = Frame(root, height=1980, width=1080)
# start_window.ImageTk.PhotoImage(file="C:/Users/kenneth/Pictures/Saved Pictures/BG2.jpg")

#####################


start = Label(start_window, text="INTRODUCTION TO COMPUTER ARCHITECTURE", font=("Arial", 30), bg="WHITE", fg="GRAY")
start.grid(row=10, column=0)

start1 = Button(start_window, text="START", font=("Arial", 30), bg="WHITE", fg="BLACK", command=home_enter)
start1.grid(row=15, column=0, pady=500)

###############HOME WINDOW/

home_window = Frame(root, height=1980, width=1080)

home_screen = Label(home_window, text="COURSE MODULE", font=("Arial", 30), bg="GRAY", fg="BLACK")
home_screen.place(x=400, y=50)

#######################CHAPTER BUTTON


chap1 = Button(home_window, text="CHAPTER 1", font=("Arial", 30), fg="BLACK", bg="BLUE", command=Chapter_1)
chap1.place(x=150, y=200)

chap2 = Button(home_window, text="CHAPTER 2", font=("Arial", 30), fg="BLACK", bg="BLUE")
chap2.place(x=450, y=200)

chap3 = Button(home_window, text="CHAPTER 3", font=("Arial", 30), fg="BLACK", bg="BLUE")
chap3.place(x=750, y=200)

#################################TOPIC ACCESS BUTTON

access1 = Button(home_window, text="", bg="GRAY", command=ct_btn)
access1.place(x=150, y=300)
access1.config(height=20, width=35)


access2 = Button(home_window, text="", bg="GRAY")
access2.place(x=450, y=300)
access2.config(height=20, width=35)

access3 = Button(home_window, text="", bg="GRAY")
access3.place(x=750, y=300)
access3.config(height=20, width=35)


#####################CHAPTER OBJECTIVE


objective_1 = Frame(root, height=1980, width=1080)

in_object1 = Label(objective_1, text="CHAPTER OBJECTIVES", font=("Arial", 50), fg="BLACK", bg="GRAY")
in_object1.place(x=100, y=50)

back1 = Button(objective_1, command=back)
back1.pack(anchor="nw")


###########################CHAPTER 1 TOPIC

topic_con_btns = Frame(root, height=1980, width=1000)

chaptop1 = Button(topic_con_btns, text="TOPIC 1", font=("Arial", 30), fg="BLACK", bg="GRAY")
chaptop1.place(x=100, y=50)

chaptop2 = Button(topic_con_btns, text="TOPIC 2", font=("Arial", 30), fg="BLACK", bg="GRAY")
chaptop2.place(x=100, y=100)

chaptop3 = Button(topic_con_btns, text="TOPIC 3", font=("Arial", 30), fg="BLACK", bg="GRAY")
chaptop3.place(x=100, y=150)

chaptop4 = Button(topic_con_btns, text="TOPIC 4", font=("Arial", 30), fg="BLACK", bg="GRAY")
chaptop4.place(x=100, y=200)

chaptop5 = Button(topic_con_btns, text="TOPIC 5", font=("Arial", 30), fg="BLACK", bg="GRAY")
chaptop5.place(x=100, y=250)










if __name__ == '__main__':
    frame.place(x=480, y=200)

root.mainloop()
