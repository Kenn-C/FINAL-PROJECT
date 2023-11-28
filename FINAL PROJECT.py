import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import webbrowser


def login_home():
    sign_in_frame.place_forget()
    frame.place(x=480, y=200)
    root.update()


def login():
    if log_in_validation():
        frame.place_forget()
        home()
    else:
        messagebox.showinfo(title='INVALID LOGIN', message="PLEASE TRY AGAIN.")
        login_home()


def _log():
    frame.place(x=480, y=200)
    sign_in_frame.place_forget()


def log_in_validation():
    con = sqlite3.connect("Accounts.db")
    c = con.cursor()

    c.execute("SELECT * FROM accounts")
    x = c.fetchall()

    for acc in x:

        if username_entry.get() == acc[1] and password_entry.get() == acc[2]:
            print(acc[1])
            messagebox.showinfo("LOGIN SUCCESSFUL!", "YOU HAVE LOGGED IN!")
            return True

    con.commit()
    con.close()


def home():
    start_window.pack(expand=True, fill=BOTH)


def sign_validation():
    pass


def signin():
    frame.place_forget()
    sign_in_frame.place(x=480, y=200)


def show():
    password_entry.config(show="")
    show_button.config(command=hide)


def hide():
    password_entry.config(show="*")
    show_button.config(command=show)


def insert_data():
    if signin_username_entry.get() == "" and signin_password_entry.get() == "" and confirm_entry.get() == "":
        messagebox.showerror("Error", "All fields are empty")

    elif signin_password_entry.get() != confirm_entry.get():
        messagebox.showerror("ERROR", "PASSWORD DOES NOT MATCH")

    elif check.get() == 0:
        messagebox.showerror("ERROR", "PLEASE ACCEPT TERMS AND CONDITIONS")

    else:
        if signin_password_entry.get() == confirm_entry.get():
            con = sqlite3.connect("Accounts.db")
            c = con.cursor()
            c.execute("INSERT INTO Accounts (username, password) VALUES (?,?)",
                      (signin_username_entry.get(), signin_password_entry.get(),))
            con.commit()
            con.close()
            messagebox.showinfo("SUCCESS", "SIGN IN SUCCESSFUL")


def to_start_window():
    home_window.place_forget()
    start_window.pack(expand=True, fill=BOTH)


def home_enter():
    start_window.pack_forget()
    frame.pack_forget()
    home_window.pack(expand=True, fill=BOTH)


def back_obj1():
    objective_1.pack_forget()
    home_window.pack(expand=True, fill=BOTH)


def back_obj2():
    objective_2.pack_forget()
    home_window.pack(expand=True, fill=BOTH)


def back_obj3():
    objective_3.pack_forget()
    home_window.pack(expand=True, fill=BOTH)


def back_top1():
    topic_con_btns1.pack_forget()
    home_window.pack(expand=True, fill=BOTH)


def back_top2():
    topic_con_btns2.pack_forget()
    home_window.pack(expand=True, fill=BOTH)


def back_top3():
    topic_con_btns3.pack_forget()
    home_window.pack(expand=True, fill=BOTH)


def chapter_1():
    home_window.pack_forget()
    objective_1.pack(expand=True, fill=BOTH)


def chapter_2():
    home_window.pack_forget()
    objective_2.pack(expand=True, fill=BOTH)


def chapter_3():
    home_window.pack_forget()
    objective_3.pack(expand=True, fill=BOTH)


def acs1_btn():
    home_window.pack_forget()
    topic_con_btns1.pack(expand=True, fill=BOTH)


def acs2_btn():
    home_window.pack_forget()
    topic_con_btns2.pack(expand=True, fill=BOTH)


def acs3_btn():
    home_window.pack_forget()
    topic_con_btns3.pack(expand=True, fill=BOTH)


def show_toggle():
    toggle_frame.place(x=1320, y=30)
    toggle_button.config(command=hide_toggle)


def hide_toggle():
    toggle_frame.place_forget()
    score_frame.place_forget()
    average_frame.place_forget()
    final_quiz_frame.place_forget()
    toggle_button.config(command=show_toggle)


def scores():
    score_frame.place(x=0, y=30)
    score_frame.config(width=1320, height=800)
    toggle_frame.config(width=210, height=800)
    final_quiz_frame.place_forget()
    average_frame.place_forget()


def quiz_final():
    final_quiz_frame.place(x=0, y=30)
    final_quiz_frame.config(width=1320, height=800)
    toggle_frame.config(width=210, height=800)
    score_frame.place_forget()
    average_frame.place_forget()


def avrg():
    average_frame.place(x=0, y=30)
    average_frame.config(width=1320, height=800)
    toggle_frame.config(width=210, height=800)
    score_frame.place_forget()
    final_quiz_frame.place_forget()


questions_1st = [

    {"ask": "1. what is 100 + 134?",
     "ans": "234"
     },
    {"ask": "2. what is 1 + 134?",
     "ans": "135"
     },
    {"ask": "3. what is 1 + 1?",
     "ans": "2"
     },
    {"ask": "4. what is 1 + 135?",
            "ans": "136"
     },
    {"ask": "5. what is 1 + 136?",
            "ans": "137"
     },
    {"ask": "6. what is 1 + 137?",
            "ans": "138"
     },
    {"ask": "7. what is 1 + 137?",
            "ans": "138"
     },
    {"ask": "8. what is 1 + 138?",
            "ans": "139"
     },
    {"ask": "9. what is 1 + 139?",
            "ans": "140"
     },
    {"ask": "10. what is 1 + 140?",
            "ans": "141"
     },
    {"ask": "11. what is 1 + 141?",
            "ans": "142"
     },
    {"ask": "12. what is 1 + 142?",
            "ans": "143"
     },
    {"ask": "13. what is 1 + 143?",
            "ans": "144"
     },
    {"ask": "14. what is 1 + 144?",
            "ans": "145"
     },
    {"ask": "15. what is 1 + 145?",
            "ans": "146"
     }

]
quiz_num = 0
correct_ans = 0


def no_1():
    global quiz_num
    q1.place(x=0, y=0)
    quiz(quiz_num)


def quiz(n):
    global questions_1st
    if n < len(questions_1st):
        ques = questions_1st[n].get("ask")
        correct = questions_1st[n].get("ans")
        question.config(text=f'{ques}')
        done.config(command=lambda: check_ans(correct))
    else:
        end_quiz()


def check_ans(ans):
    global quiz_num, correct_ans
    user_ans = str(answer.get())
    if user_ans == str(ans):
        messagebox.showinfo("correct", "NEXT QUESTION")
        correct_ans += 1

    quiz_num += 1

    if quiz_num < len(questions_1st):
        answer.delete(0, END)
        quiz(quiz_num)

    else:
        end_quiz()


def end_quiz():
    global quiz_num
    messagebox.showinfo("WELL DONE", f"QUIZ COMPLETE\n Your Score is: {correct_ans}/{len(questions_1st)}")


def out():
    toggle_frame.place_forget()
    home_window.place_forget()
    start_window.place_forget()
    frame.place(x=480, y=200)
    sign_in_frame.place(x=480, y=200)


# start


root = Tk()

window = root
window.title("Login Form")
window.geometry("1540x864")
window.resizable(False, False)
#winBG = ImageTk.PhotoImage(file='C:/Users/kenneth/Pictures/Saved Pictures/BG3.jpg')
#winBg = Label(window, image=winBG)
#winBg.place(x=0, y=0)

logbg = Image.open("C:/Users/kenneth/Pictures/Saved Pictures/loginbutton.png")
logbg = logbg.resize((90, 60))
logbg = ImageTk.PhotoImage(logbg)

# login

frame = Canvas(root)
frame.config(bg="BLACK")
frame.place(x=480, y=200)

# binding


f1 = frame.create_image(100, 165, image=logbg)
frame.tag_bind(f1, "<Button>", lambda event: login())

# Label


login_label = Label(frame, text='LOGIN', bg="BLACK", fg="GRAY", font=("Display", 15))
login_label.grid(row=5, column=0, sticky="news", pady=10)

username_label = Label(frame, text='USERNAME', bg="BLACK", fg="GRAY", font=("Arial", 10))
username_label.grid(row=7, column=0)

password_label = Label(frame, text="PASSWORD", bg="BLACK", fg="GRAY", font=("Arial", 10))
password_label.grid(row=9, column=0)

# Entry

username_entry = Entry(frame)
username_entry.grid(row=7, column=1, pady=10)

password_entry = Entry(frame)
password_entry.grid(row=9, column=1, pady=10)

# Button


# login_button = Button(frame, command=login, text="LOGIN", font=("Arial", 10))
# login_button.grid(row=9, column=0, padx=10, pady=20)

sign_up_button = Button(frame, text="SIGN UP", command=signin, bg="GRAY", fg="BLACK", font=("Arial", 10))
sign_up_button.grid(row=14, column=1, padx=10, pady=20)

show_button = Button(frame, command=hide)
show_button.grid(row=12, column=2, pady=10)

# signin

sign_in_frame = Frame(root)
sign_in_frame.config(bg="BLACK")

# sign_in_frame.place(x=480, y=200)

# SLabel

signup_label = Label(sign_in_frame, text='CREATE AN ACCOUNT', bg='WHITE', fg='BLUE', font=('Arial', 10))
signup_label.grid(row=0, column=0, columnspan=2, pady=30)

username_label = Label(sign_in_frame, text='ENTER YOUR USERNAME', bg="BLACK", fg="BLUE", font=("Arial", 10))
username_label.grid(row=6, column=0)

password_label = Label(sign_in_frame, text="ENTER YOUR PASSWORD", bg="BLACK", fg="BLUE", font=("Arial", 10))
password_label.grid(row=7, column=0)

confirm_label = Label(sign_in_frame, text="CONFIRM PASSWORD", bg='BLACK', fg='BLUE', font=('Arial', 10))
confirm_label.grid(row=8, column=0)

already = Label(sign_in_frame, text='Already have an account?', font=('Arial', 8))
already.grid(row=14, column=0)

# SEntry


signin_username_entry = Entry(sign_in_frame)
signin_username_entry.grid(row=6, column=1, pady=10)

signin_password_entry = Entry(sign_in_frame)
signin_password_entry.grid(row=7, column=1, pady=10)

confirm_entry = Entry(sign_in_frame)
confirm_entry.grid(row=8, column=1, pady=10)

# SButton

check = IntVar()
taC = Checkbutton(sign_in_frame, text="I Agree to the Terms and Conditions", variable=check, font=('Arial', 7),
                  cursor='hand2')
taC.grid(row=10, column=1)

sign1 = Button(sign_in_frame, text='SIGN UP', font=('Arial', 12), bg='BLACK', fg='BLUE', command=insert_data)
sign1.grid(row=12, column=0, columnspan=2, pady=20)

log = Button(sign_in_frame, text='Log in', font=('Arial', 8), bg='BLACK', fg='BLUE', cursor="hand2",
             command=lambda: _log())
log.grid(row=14, column=1)

# STARTING WINDOW

start_btn = Image.open("C:/Users/kenneth/Pictures/Saved Pictures/START.png")
start_btn = start_btn.resize((1400, 1300))
start_btn = ImageTk.PhotoImage(start_btn)

start_bg1 = Image.open("C:/Users/kenneth/Pictures/Saved Pictures/START_BG.jpg")
start_bg1 = start_bg1.resize((1540, 864))
start_bg1 = ImageTk.PhotoImage(start_bg1)


start_window = Canvas(root)
start_window.config(height=864, width=1540)
start_window.place(x=1540, y=864)

# BIND START
start_window.create_image(770, 432, image=start_bg1)
btn1 = start_window.create_image(560, 500, image=start_btn)
start_window.tag_bind(btn1, "<Button>", lambda event: home_enter())


#start_bg1 = ImageTk.PhotoImage(file="C:/Users/kenneth/Pictures/Saved Pictures/START_BG.jpg")
#starting_window = Label(start_window, image=start_bg1)
#starting_window.place(x=0, y=0)

comp = Label(start_window, text="COMPUTER", font=("Arial", 60), bg="DARK BLUE", fg="BLUE")
comp.place(x=850, y=100)
comp.config(height=0, width=10)

archi = Label(start_window, text="ARCHITECTURE", font=("Arial", 60), bg="DARK BLUE", fg="BLUE")
archi.place(x=800, y=600)


#start1 = Button(start_window, text="START", font=("Arial", 30), bg="LIGHT BLUE", fg="BLUE", command=home_enter)
#start1.place(x=350, y=400)

# HOME WINDOW

home_window = Canvas(root)
home_window.place(x=1540, y=864)
home_window.config(height=864, width=1540)

# home_bg1 = ImageTk.PhotoImage(file="C:/Users/kenneth/Pictures/Saved Pictures/HOME_BG.jpg")
# h1_window = Label(home_window, image=home_bg1)
# h1_window.place(x=0, y=0)

home_screen = Label(home_window, text="COURSE MODULE", font=("Arial", 40), bg="GRAY", fg="BLACK")
home_screen.place(x=550, y=50)

back_start = Button(home_window, command=to_start_window)
back_start.pack(anchor="nw")

# CHAPTER BUTTON


chap1 = Button(home_window, text="CHAPTER 1", font=("Arial", 30), fg="BLACK", bg="BLUE", command=chapter_1)
chap1.place(x=200, y=200)

chap2 = Button(home_window, text="CHAPTER 2", font=("Arial", 30), fg="BLACK", bg="BLUE", command=chapter_2)
chap2.place(x=625, y=200)

chap3 = Button(home_window, text="CHAPTER 3", font=("Arial", 30), fg="BLACK", bg="BLUE", command=chapter_3)
chap3.place(x=1050, y=200)

# TOPIC ACCESS BUTTON

access1 = Button(home_window, text="", bg="GRAY", command=acs1_btn)
access1.place(x=200, y=300)
access1.config(height=20, width=35)

access2 = Button(home_window, bg="GRAY", command=acs2_btn)
access2.place(x=625, y=300)
access2.config(height=20, width=35)

access3 = Button(home_window, bg="GRAY", command=acs3_btn)
access3.place(x=1050, y=300)
access3.config(height=20, width=35)

# acc3 = Image.open("C:/Users/kenneth/Pictures/Saved Pictures/START.png")
# acc3 = acc3.resize((1100, 1100))
# acc3 = ImageTk.PhotoImage(acc3)

# ac3 = start_window.create_image(1000, 1000, image=acc3)
# home_window.tag_bind(acc3, "<Button>", lambda event: acs3_btn())

# "C:UserskennethPicturesSaved PicturesCHAPTER_BG1.jpg"

# CHAPTER OBJECTIVE


objective_1 = Frame(root, height=1980, width=1080)

in_object1 = Label(objective_1, text="CHAPTER OBJECTIVES", font=("Arial", 50), fg="BLACK", bg="GRAY")
in_object1.place(x=100, y=50)

back1 = Button(objective_1, command=back_obj1)
back1.pack(anchor="nw")

objective_2 = Frame(root, height=1980, width=1080)

in_object2 = Label(objective_2, text="CHAPTER OBJECTIVES", font=("Arial", 50), fg="BLACK", bg="GRAY")
in_object2.place(x=100, y=50)

back2 = Button(objective_2, command=back_obj2)
back2.pack(anchor="nw")

objective_3 = Frame(root, height=1980, width=1080)

in_object3 = Label(objective_3, text="CHAPTER OBJECTIVES", font=("Arial", 50), fg="DARK BLUE", bg="BLUE")
in_object3.place(x=100, y=50)

back3 = Button(objective_3, command=back_obj3)
back3.pack(anchor="nw")

# CHAPTER 1 TOPIC

topic_con_btns1 = Frame(root, height=1980, width=1000)
back4 = Button(topic_con_btns1, command=back_top1)
back4.pack(anchor="nw")

chap1_top1 = Button(topic_con_btns1, text="TOPIC 1", font=("Arial", 30), fg="BLACK", bg="GRAY")
chap1_top1.place(x=100, y=95)

chap1_top2 = Button(topic_con_btns1, text="TOPIC 2", font=("Arial", 30), fg="BLACK", bg="GRAY")
chap1_top2.place(x=100, y=245)

chap1_top3 = Button(topic_con_btns1, text="TOPIC 3", font=("Arial", 30), fg="BLACK", bg="GRAY")
chap1_top3.place(x=100, y=395)

chap1_top4 = Button(topic_con_btns1, text="TOPIC 4", font=("Arial", 30), fg="BLACK", bg="GRAY")
chap1_top4.place(x=100, y=545)

chap1_top5 = Button(topic_con_btns1, text="TOPIC 5", font=("Arial", 30), fg="BLACK", bg="GRAY")
chap1_top5.place(x=100, y=695)

# CHAPTER1 QUIZ BTNS

chap1_quiz1 = Button(topic_con_btns1, text="QUIZ", font=("Arial", 30), fg="BLACK", bg="GRAY")
chap1_quiz1.place(x=600, y=170)

chap1_quiz2 = Button(topic_con_btns1, text="QUIZ", font=("Arial", 30), fg="BLACK", bg="GRAY")
chap1_quiz2.place(x=600, y=545)

chap1_quiz_final1 = Button(topic_con_btns1, text="FINAL QUIZ", font=("Arial", 30), fg="BLACK", bg="GRAY")
chap1_quiz_final1.place(x=900, y=350)
chap1_quiz_final1.config(height=0, width=10)

# CHAPTER 2 TOPIC

topic_con_btns2 = Frame(root, height=1980, width=1000)
back5 = Button(topic_con_btns2, command=back_top2)
back5.pack(anchor="nw")

chap2_top1 = Button(topic_con_btns2, text="TOPIC 1", font=("Arial", 30), fg="BLACK", bg="GRAY")
chap2_top1.place(x=150, y=50)

chap2_top2 = Button(topic_con_btns2, text="TOPIC 2", font=("Arial", 30), fg="BLACK", bg="GRAY")
chap2_top2.place(x=1150, y=50)

chap2_top3 = Button(topic_con_btns2, text="TOPIC 3", font=("Arial", 30), fg="BLACK", bg="GRAY")
chap2_top3.place(x=150, y=350)

chap2_top4 = Button(topic_con_btns2, text="TOPIC 4", font=("Arial", 30), fg="BLACK", bg="GRAY")
chap2_top4.place(x=640, y=350)

chap2_top5 = Button(topic_con_btns2, text="TOPIC 5", font=("Arial", 30), fg="BLACK", bg="GRAY")
chap2_top5.place(x=1180, y=350)

# CHAPTER 2 QUIZ BTNS

chap2_quiz1 = Button(topic_con_btns2, text="QUIZ", font=("Arial", 30), fg="BLACK", bg="GRAY")
chap2_quiz1.place(x=670, y=170)

chap2_quiz2 = Button(topic_con_btns2, text="QUIZ", font=("Arial", 30), fg="BLACK", bg="GRAY")
chap2_quiz2.place(x=670, y=540)

chap2_quiz_final2 = Button(topic_con_btns2, text="FINAL QUIZ", font=("Arial", 30), fg="BLACK", bg="GRAY")
chap2_quiz_final2.place(x=610, y=680)
# chap2_quiz_final2.config(height=0, width=10)


# CHAPTER 3 TOPIC

topic_con_btns3 = Frame(root, height=1980, width=1000)

# c3_bg1 = ImageTk.PhotoImage(file="C:/Users/kenneth/Pictures/Saved Pictures/CHAPTER_BG1.jpg")
# c3_background = Label(topic_con_btns3, image=c3_bg1)
# c3_background.place(x=0, y=0)

back6 = Button(topic_con_btns3, command=back_top3)
back6.pack(anchor="nw")

chap3_top1 = Button(topic_con_btns3, text="TOPIC 1", font=("Arial", 30), fg="BLACK", bg="GRAY")
chap3_top1.place(x=500, y=0)

chap3_top2 = Button(topic_con_btns3, text="TOPIC 2", font=("Arial", 30), fg="BLACK", bg="GRAY")
chap3_top2.place(x=50, y=240)

chap3_top3 = Button(topic_con_btns3, text="TOPIC 3", font=("Arial", 30), fg="BLACK", bg="GRAY")
chap3_top3.place(x=900, y=0)

chap3_top4 = Button(topic_con_btns3, text="TOPIC 4", font=("Arial", 30), fg="BLACK", bg="GRAY")
chap3_top4.place(x=1320, y=240)

chap3_top5 = Button(topic_con_btns3, text="TOPIC 5", font=("Arial", 30), fg="BLACK", bg="GRAY")
chap3_top5.place(x=150, y=500)

chap3_top6 = Button(topic_con_btns3, text="TOPIC 6", font=("Arial", 30), fg="BLACK", bg="GRAY")
chap3_top6.place(x=1200, y=500)

######################## CHAPTER3 QUIZ BTNS

q1 = Frame(root)
q1.config(bg="GRAY")
q1.config(height=1080, width=1980)

question = Label(q1)
question.place(x=200, y=100)
answer = Entry(q1)
answer.place(x=300, y=300)
done = Button(q1, text="done")
done.place(x=400, y=500)

chap3_quiz1 = Button(topic_con_btns3, text="QUIZ1", font=("Arial", 30), fg="BLACK", bg="GRAY", command=no_1)
chap3_quiz1.place(x=280, y=100)


##########


chap3_quiz2 = Button(topic_con_btns3, text="QUIZ", font=("Arial", 30), fg="BLACK", bg="GRAY")
chap3_quiz2.place(x=1180, y=100)

chap3_quiz3 = Button(topic_con_btns3, text="QUIZ", font=("Arial", 30), fg="BLACK", bg="GRAY")
chap3_quiz3.place(x=670, y=650)

chap3_quiz_final3 = Button(topic_con_btns3, text="FINAL QUIZ", font=("Arial", 30), fg="BLACK", bg="GRAY")
chap3_quiz_final3.place(x=630, y=350)
chap3_quiz_final3.config(height=0, width=10)

# FINAL EXAM BUTTON

final_exam = Button(home_window, text="FINAL EXAM", font=("Arial", 30), fg="DARK BLUE", bg="BLUE")
final_exam.place(x=650, y=700)

# PROFILE BUTTON

profile = Button(home_window)
profile.place(x=1400, y=0)
profile.config(height=0, width=5)

# TOGGLE FRAME, BUTTON & MENU

toggle_frame = Frame(root)
toggle_frame.config(bg="GRAY")
toggle_frame.config(height=800, width=210)
# toggle_frame.place(x=1540, y=10)

toggle_button = Button(home_window, text="", bg="BLACK", command=show_toggle)
toggle_button.place(x=1510, y=0)

# TOGGLE BUTTON

score_frame = Frame(root)
score_frame.config(bg="GRAY")
score_frame.config(height=864, width=1540)

quiz_scores = Button(toggle_frame, text="QUIZ SCORES", bg="GRAY", fg="BLACK", command=scores)
quiz_scores.place(x=0, y=20)
quiz_scores.config(height=5, width=30)

#############################

final_quiz_frame = Frame(root)
final_quiz_frame.config(bg="BLACK")
final_quiz_frame.config(height=864, width=1540)

final_quiz_exams = Button(toggle_frame, text="FINAL QUIZ & EXAMS", bg="GRAY", fg="BLACK", command=quiz_final)
final_quiz_exams.place(x=0, y=150)
final_quiz_exams.config(height=5, width=30)

#####################

average_frame = Frame(root)
average_frame.config(bg="GREEN")
average_frame.config(height=864, width=1540)

overall_avg = Button(toggle_frame, text="OVERALL AVERAGE", bg="GRAY", fg="BLACK", command=avrg)
overall_avg.place(x=0, y=280)
overall_avg.config(height=5, width=30)

# TOGGLE CONTENT BACK

back_toggle_content = Button()

######################

log_out = Button(toggle_frame, text="LOG OUT", bg="GRAY", fg="BLACK", command=out)
log_out.place(x=0, y=700)
log_out.config(height=5, width=30)

####################


####################

if __name__ == '__main__':
    frame.place(x=480, y=200)

root.mainloop()
