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
    {"ask": "1. 3rd letter in button?",
     "ans": "t"
     },
    {"ask": "2. RISC stands for?",
     "ans": "Reduced Instruction set Computer"
     },
    {"ask": "3. CISC stands for?",
     "ans": "Complex Instruction set Computer"
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

quiz_num_1 = 0
correct_ans_1 = 0


def into_1():
    quiz_start1.place(x=0, y=0)


def no_1():
    global quiz_num_1
    q1.place(x=0, y=0)
    quiz1(quiz_num_1)


def quiz1(a):
    global questions_1st
    if a < len(questions_1st):
        ques = questions_1st[a].get("ask")
        correct = questions_1st[a].get("ans")
        question1.config(text=f'{ques}')
        done1.config(command=lambda: check_ans1(correct))
    else:
        end_quiz1()


def check_ans1(ans1):
    global quiz_num_1, correct_ans_1
    user_ans = str(answer1.get())
    if user_ans == str(ans1):
        correct_ans_1 += 1

    quiz_num_1 += 1

    if quiz_num_1 < len(questions_1st):
        answer1.delete(0, END)
        quiz1(quiz_num_1)

    else:
        end_quiz1()


def end_quiz1():
    global quiz_num_1
    messagebox.showinfo("WELL DONE", f"QUIZ COMPLETE\n Your Score is: {correct_ans_1}/{len(questions_1st)}")
    q1.place_forget()
    to_start1.place_forget()


questions_2nd = [
    {"ask": "1. 5th letter in button?",
     "ans": "o"
     },
    {"ask": "2. RISC stands for?",
     "ans": "Reduced Instruction set Computer"
     },
    {"ask": "3. CISC stands for?",
     "ans": "Complex Instruction set Computer"
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

quiz_num_2 = 0
correct_ans_2 = 0


def into_2():
    quiz_start2.place(x=0, y=0)


def no_2():
    global quiz_num_2
    q2.place(x=0, y=0)
    quiz2(quiz_num_2)


def quiz2(b):
    global questions_2nd
    if b < len(questions_2nd):
        ques = questions_2nd[b].get("ask")
        correct = questions_2nd[b].get("ans")
        question2.config(text=f'{ques}')
        done2.config(command=lambda: check_ans2(correct))
    else:
        end_quiz2()


def check_ans2(ans2):
    global quiz_num_2, correct_ans_2
    user_ans = str(answer2.get())
    if user_ans == str(ans2):
        correct_ans_2 += 1

    quiz_num_2 += 1

    if quiz_num_2 < len(questions_2nd):
        answer2.delete(0, END)
        quiz2(quiz_num_2)

    else:
        end_quiz2()


def end_quiz2():
    global quiz_num_2
    messagebox.showinfo("WELL DONE", f"QUIZ COMPLETE\n Your Score is: {correct_ans_2}/{len(questions_2nd)}")
    q2.place_forget()
    to_start2.place_forget()


final_1st = [
    {"ask": "1. 3rd letter in button?",
     "ans": "t"
     },
    {"ask": "2. RISC stands for?",
     "ans": "Reduced Instruction set Computer"
     },
    {"ask": "3. CISC stands for?",
     "ans": "Complex Instruction set Computer"
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
     },
    {"ask": "16. 1st letter in button?",
     "ans": "b"
     },
    {"ask": "17. RISC stands for?",
     "ans": "Reduced Instruction set Computer"
     },
    {"ask": "18. CISC stands for?",
     "ans": "Complex Instruction set Computer"
     },
    {"ask": "19. what is the 6th letter in letter?",
            "ans": "r"
     },
    {"ask": "20. what is 1 + 136?",
            "ans": "137"
     },
    {"ask": "21. what is 1 + 137?",
            "ans": "138"
     },
    {"ask": "22. what is 1 + 137?",
            "ans": "138"
     },
    {"ask": "23. what is 1 + 138?",
            "ans": "139"
     },
    {"ask": "24. what is 1 + 139?",
            "ans": "140"
     },
    {"ask": "25. what is 1 + 140?",
            "ans": "141"
     },
    {"ask": "26. what is 1 + 141?",
            "ans": "142"
     },
    {"ask": "27. what is 1 + 142?",
            "ans": "143"
     },
    {"ask": "28. what is 1 + 143?",
            "ans": "144"
     },
    {"ask": "29. what is 1 + 144?",
            "ans": "145"
     },
    {"ask": "30. what is 1 + 145?",
            "ans": "146"
     },
    {"ask": "31. what is 1 + 136?",
            "ans": "137"
     },
    {"ask": "32. what is 1 + 137?",
            "ans": "138"
     },
    {"ask": "33. what is 1 + 137?",
            "ans": "138"
     },
    {"ask": "34. what is 1 + 138?",
            "ans": "139"
     },
    {"ask": "35. what is 1 + 139?",
            "ans": "140"
     },
    {"ask": "36. what is 1 + 140?",
            "ans": "141"
     },
    {"ask": "37. what is 1 + 141?",
            "ans": "142"
     },
    {"ask": "38. what is 1 + 142?",
            "ans": "143"
     },
    {"ask": "39. what is 1 + 143?",
            "ans": "144"
     },
    {"ask": "40. what is 1 + 144?",
            "ans": "145"
     }

]

final_num_1 = 0
final_ans_1 = 0


def into_final1():
    quiz_start_final1.place(x=0, y=0)


def final_no_1():
    global final_num_1
    q_final1.place(x=0, y=0)
    final1(final_num_1)


def final1(c):
    global final_1st
    if c < len(final_1st):
        ques = final_1st[c].get("ask")
        correct = final_1st[c].get("ans")
        final_question1.config(text=f'{ques}')
        final_done1.config(command=lambda: check_final1(correct))
    else:
        end_final1()


def check_final1(f1):
    global final_num_1, final_ans_1
    user_ans = str(final_answer1.get())
    if user_ans == str(f1):
        final_ans_1 += 1

    final_num_1 += 1

    if final_num_1 < len(final_1st):
        final_answer1.delete(0, END)
        final1(final_num_1)

    else:
        end_final1()


def end_final1():
    global final_num_1
    messagebox.showinfo("WELL DONE", f"QUIZ COMPLETE\n Your Score is: {final_ans_1}/{len(final_1st)}")
    q_final1.place_forget()
    quiz_start_final1.place_forget()


questions_3rd = [
    {"ask": "1. Au means?",
     "ans": "Gold"
     },
    {"ask": "2. RISC stands for?",
     "ans": "Reduced Instruction set Computer"
     },
    {"ask": "3. CISC stands for?",
     "ans": "Complex Instruction set Computer"
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

quiz_num_3 = 0
correct_ans_3 = 0


def into_3():
    quiz_start3.place(x=0, y=0)


def no_3():
    global quiz_num_3
    q3.place(x=0, y=0)
    quiz3(quiz_num_3)


def quiz3(d):
    global questions_3rd
    if d < len(questions_3rd):
        ques = questions_3rd[d].get("ask")
        correct = questions_3rd[d].get("ans")
        question3.config(text=f'{ques}')
        done3.config(command=lambda: check_ans3(correct))
    else:
        end_quiz3()


def check_ans3(ans3):
    global quiz_num_3, correct_ans_3
    user_ans = str(answer3.get())
    if user_ans == str(ans3):
        correct_ans_3 += 1

    quiz_num_3 += 1

    if quiz_num_3 < len(questions_3rd):
        answer3.delete(0, END)
        quiz3(quiz_num_3)

    else:
        end_quiz3()


def end_quiz3():
    global quiz_num_3
    messagebox.showinfo("WELL DONE", f"QUIZ COMPLETE\n Your Score is: {correct_ans_3}/{len(questions_3rd)}")
    q3.place_forget()
    quiz_start3.place_forget()


questions_4th = [
    {"ask": "1. Ag means?",
     "ans": "Silver"
     },
    {"ask": "2. RISC stands for?",
     "ans": "Reduced Instruction set Computer"
     },
    {"ask": "3. CISC stands for?",
     "ans": "Complex Instruction set Computer"
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

quiz_num_4 = 0
correct_ans_4 = 0


def into_4():
    quiz_start4.place(x=0, y=0)


def no_4():
    global quiz_num_4
    q4.place(x=0, y=0)
    quiz4(quiz_num_4)


def quiz4(e):
    global questions_4th
    if e < len(questions_4th):
        ques = questions_4th[e].get("ask")
        correct = questions_4th[e].get("ans")
        question4.config(text=f'{ques}')
        done4.config(command=lambda: check_ans4(correct))
    else:
        end_quiz4()


def check_ans4(ans4):
    global quiz_num_4, correct_ans_4
    user_ans = str(answer4.get())
    if user_ans == str(ans4):
        correct_ans_4 += 1

    quiz_num_4 += 1

    if quiz_num_4 < len(questions_4th):
        answer4.delete(0, END)
        quiz4(quiz_num_4)

    else:
        end_quiz4()


def end_quiz4():
    global quiz_num_4
    messagebox.showinfo("WELL DONE", f"QUIZ COMPLETE\n Your Score is: {correct_ans_4}/{len(questions_4th)}")
    q4.place_forget()
    quiz_start4.place_forget()


final_2nd = [
    {"ask": "1. 3rd letter in button?",
     "ans": "t"
     },
    {"ask": "2. RISC stands for?",
     "ans": "Reduced Instruction set Computer"
     },
    {"ask": "3. CISC stands for?",
     "ans": "Complex Instruction set Computer"
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
     },
    {"ask": "16. 1st letter in button?",
     "ans": "b"
     },
    {"ask": "17. RISC stands for?",
     "ans": "Reduced Instruction set Computer"
     },
    {"ask": "18. CISC stands for?",
     "ans": "Complex Instruction set Computer"
     },
    {"ask": "19. what is the 6th letter in letter?",
            "ans": "r"
     },
    {"ask": "20. what is 1 + 136?",
            "ans": "137"
     },
    {"ask": "21. what is 1 + 137?",
            "ans": "138"
     },
    {"ask": "22. what is 1 + 137?",
            "ans": "138"
     },
    {"ask": "23. what is 1 + 138?",
            "ans": "139"
     },
    {"ask": "24. what is 1 + 139?",
            "ans": "140"
     },
    {"ask": "25. what is 1 + 140?",
            "ans": "141"
     },
    {"ask": "26. what is 1 + 141?",
            "ans": "142"
     },
    {"ask": "27. what is 1 + 142?",
            "ans": "143"
     },
    {"ask": "28. what is 1 + 143?",
            "ans": "144"
     },
    {"ask": "29. what is 1 + 144?",
            "ans": "145"
     },
    {"ask": "30. what is 1 + 145?",
            "ans": "146"
     },
    {"ask": "31. what is 1 + 136?",
            "ans": "137"
     },
    {"ask": "32. what is 1 + 137?",
            "ans": "138"
     },
    {"ask": "33. what is 1 + 137?",
            "ans": "138"
     },
    {"ask": "34. what is 1 + 138?",
            "ans": "139"
     },
    {"ask": "35. what is 1 + 139?",
            "ans": "140"
     },
    {"ask": "36. what is 1 + 140?",
            "ans": "141"
     },
    {"ask": "37. what is 1 + 141?",
            "ans": "142"
     },
    {"ask": "38. what is 1 + 142?",
            "ans": "143"
     },
    {"ask": "39. what is 1 + 143?",
            "ans": "144"
     },
    {"ask": "40. what is 1 + 144?",
            "ans": "145"
     }

]

final_num_2 = 0
final_ans_2 = 0


def into_final2():
    quiz_start_final2.place(x=0, y=0)


def final_no_2():
    global final_num_2
    q_final2.place(x=0, y=0)
    final2(final_num_2)


def final2(f):
    global final_2nd
    if f < len(final_2nd):
        ques = final_2nd[f].get("ask")
        correct = final_2nd[f].get("ans")
        final_question2.config(text=f'{ques}')
        final_done2.config(command=lambda: check_final2(correct))
    else:
        end_final2()


def check_final2(f2):
    global final_num_2, final_ans_2
    user_ans = str(final_answer2.get())
    if user_ans == str(f2):
        final_ans_2 += 1

    final_num_2 += 1

    if final_num_2 < len(final_2nd):
        final_answer2.delete(0, END)
        final2(final_num_2)

    else:
        end_final2()


def end_final2():
    global final_num_2
    messagebox.showinfo("WELL DONE", f"QUIZ COMPLETE\n Your Score is: {final_ans_2}/{len(final_2nd)}")
    q_final2.place_forget()
    quiz_start_final2.place_forget()


questions_5th = [

    {"ask": "1. what is RISC?",
     "ans": "Reduced Instruction set Computer"
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
quiz_num_5 = 0
correct_ans_5 = 0


def into_5():
    quiz_start5.place(x=0, y=0)


def no_5():
    global quiz_num_5
    q5.place(x=0, y=0)
    quiz5(quiz_num_5)


def quiz5(n):
    global questions_5th
    if n < len(questions_5th):
        ques = questions_5th[n].get("ask")
        correct = questions_5th[n].get("ans")
        question5.config(text=f'{ques}')
        done5.config(command=lambda: check_ans5(correct))
    else:
        end_quiz5()


def check_ans5(ans5):
    global quiz_num_5, correct_ans_5
    user_ans = str(answer5.get())
    if user_ans == str(ans5):
        correct_ans_5 += 1

    quiz_num_5 += 1

    if quiz_num_5 < len(questions_5th):
        answer5.delete(0, END)
        quiz5(quiz_num_5)

    else:
        end_quiz5()


def end_quiz5():
    global quiz_num_5
    messagebox.showinfo("WELL DONE", f"QUIZ COMPLETE\n Your Score is: {correct_ans_5}/{len(questions_5th)}")
    q5.place_forget()
    quiz_start5.place_forget()


questions_6th = [

    {"ask": "1. reuse, reduce and?",
     "ans": "recycle"
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

quiz_num_6 = 0
correct_ans_6 = 0


def into_6():
    quiz_start6.place(x=0, y=0)


def no_6():
    global quiz_num_6
    q6.place(x=0, y=0)
    quiz6(quiz_num_6)


def quiz6(h):
    global questions_6th
    if h < len(questions_6th):
        ques = questions_6th[h].get("ask")
        correct = questions_6th[h].get("ans")
        question6.config(text=f'{ques}')
        done6.config(command=lambda: check_ans6(correct))
    else:
        end_quiz6()


def check_ans6(ans6):
    global quiz_num_6, correct_ans_6
    user_ans = str(answer6.get())
    if user_ans == str(ans6):
        correct_ans_6 += 1

    quiz_num_6 += 1

    if quiz_num_6 < len(questions_6th):
        answer6.delete(0, END)
        quiz6(quiz_num_6)

    else:
        end_quiz6()


def end_quiz6():
    global quiz_num_6
    messagebox.showinfo("WELL DONE", f"QUIZ COMPLETE\n Your Score is: {correct_ans_6}/{len(questions_6th)}")
    q6.place_forget()
    quiz_start6.place_forget()


questions_7th = [

    {"ask": "1. what is RISC?",
     "ans": "Reduced Instruction set Computer"
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

quiz_num_7 = 0
correct_ans_7 = 0


def into_7():
    quiz_start7.place(x=0, y=0)


def no_7():
    global quiz_num_7
    q7.place(x=0, y=0)
    quiz7(quiz_num_7)


def quiz7(i):
    global questions_7th
    if i < len(questions_7th):
        ques = questions_7th[i].get("ask")
        correct = questions_7th[i].get("ans")
        question7.config(text=f'{ques}')
        done7.config(command=lambda: check_ans7(correct))
    else:
        end_quiz7()


def check_ans7(ans7):
    global quiz_num_7, correct_ans_7
    user_ans = str(answer7.get())
    if user_ans == str(ans7):
        correct_ans_7 += 1

    quiz_num_7 += 1

    if quiz_num_7 < len(questions_7th):
        answer7.delete(0, END)
        quiz7(quiz_num_7)

    else:
        end_quiz7()


def end_quiz7():
    global quiz_num_7
    messagebox.showinfo("WELL DONE", f"QUIZ COMPLETE\n Your Score is: {correct_ans_7}/{len(questions_7th)}")
    q7.place_forget()
    quiz_start7.place_forget()


final_3rd = [
    {"ask": "1. 3rd letter in button?",
     "ans": "t"
     },
    {"ask": "2. RISC stands for?",
     "ans": "Reduced Instruction set Computer"
     },
    {"ask": "3. CISC stands for?",
     "ans": "Complex Instruction set Computer"
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
     },
    {"ask": "16. 1st letter in button?",
     "ans": "b"
     },
    {"ask": "17. RISC stands for?",
     "ans": "Reduced Instruction set Computer"
     },
    {"ask": "18. CISC stands for?",
     "ans": "Complex Instruction set Computer"
     },
    {"ask": "19. what is the 6th letter in letter?",
            "ans": "r"
     },
    {"ask": "20. what is 1 + 136?",
            "ans": "137"
     },
    {"ask": "21. what is 1 + 137?",
            "ans": "138"
     },
    {"ask": "22. what is 1 + 137?",
            "ans": "138"
     },
    {"ask": "23. what is 1 + 138?",
            "ans": "139"
     },
    {"ask": "24. what is 1 + 139?",
            "ans": "140"
     },
    {"ask": "25. what is 1 + 140?",
            "ans": "141"
     },
    {"ask": "26. what is 1 + 141?",
            "ans": "142"
     },
    {"ask": "27. what is 1 + 142?",
            "ans": "143"
     },
    {"ask": "28. what is 1 + 143?",
            "ans": "144"
     },
    {"ask": "29. what is 1 + 144?",
            "ans": "145"
     },
    {"ask": "30. what is 1 + 145?",
            "ans": "146"
     },
    {"ask": "31. what is 1 + 136?",
            "ans": "137"
     },
    {"ask": "32. what is 1 + 137?",
            "ans": "138"
     },
    {"ask": "33. what is 1 + 137?",
            "ans": "138"
     },
    {"ask": "34. what is 1 + 138?",
            "ans": "139"
     },
    {"ask": "35. what is 1 + 139?",
            "ans": "140"
     },
    {"ask": "36. what is 1 + 140?",
            "ans": "141"
     },
    {"ask": "37. what is 1 + 141?",
            "ans": "142"
     },
    {"ask": "38. what is 1 + 142?",
            "ans": "143"
     },
    {"ask": "39. what is 1 + 143?",
            "ans": "144"
     },
    {"ask": "40. what is 1 + 144?",
            "ans": "145"
     }

]


final_num_3 = 0
final_ans_3 = 0


def into_final3():
    quiz_start_final3.place(x=0, y=0)


def final_no_3():
    global final_num_3
    q_final3.place(x=0, y=0)
    final3(final_num_3)


def final3(j):
    global final_3rd
    if j < len(final_3rd):
        ques = final_3rd[j].get("ask")
        correct = final_3rd[j].get("ans")
        final_question3.config(text=f'{ques}')
        final_done3.config(command=lambda: check_final3(correct))
    else:
        end_final3()


def check_final3(f3):
    global final_num_3, final_ans_3
    user_ans = str(final_answer3.get())
    if user_ans == str(f3):
        final_ans_3 += 1

    final_num_3 += 1

    if final_num_3 < len(final_3rd):
        final_answer3.delete(0, END)
        final3(final_num_3)

    else:
        end_final3()


def end_final3():
    global final_num_3
    messagebox.showinfo("WELL DONE", f"QUIZ COMPLETE\n Your Score is: {final_ans_3}/{len(final_3rd)}")
    q_final3.place_forget()
    quiz_start_final3.place_forget()


#############################3


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
#winBG = ImageTk.PhotoImage(file='C:/Users/kenneth/Pictures/Saved Pictures/BG1_LOGIN.jpg')
#winBg = Label(window, image=winBG)
#winBg.place(x=0, y=0)


#logbg = Image.open("C:/Users/kenneth/Pictures/Saved Pictures/loginbutton.png")
#logbg = logbg.resize((90, 60))
#logbg = ImageTk.PhotoImage(logbg)

# login

frame = Frame(root)
frame.config(bg="BLACK")
frame.place(x=480, y=200)

# binding


#f1 = frame.create_image(100, 165, image=logbg)
#frame.tag_bind(f1, "<Button>", lambda event: login())

# Label


login_label = Label(frame, text='LOG IN', bg="WHITE", fg="BLUE", font=("Display", 15))
login_label.grid(row=5, column=0, columnspan=2, pady=30)

username_label = Label(frame, text='ENTER YOUR USERNAME', bg="BLACK", fg="BLUE", font=("Arial", 10))
username_label.grid(row=7, column=0)

password_label = Label(frame, text="ENTER YOUR PASSWORD", bg="BLACK", fg="BLUE", font=("Arial", 10))
password_label.grid(row=9, column=0)

dont_label = Label(frame, text="Don't have an account?", bg="WHITE", fg="BLACK", font=("Arial", 8))
dont_label.grid(row=14, column=0)

# Entry

username_entry = Entry(frame)
username_entry.grid(row=7, column=1, pady=10)
username_entry.config(width=25)

password_entry = Entry(frame)
password_entry.grid(row=9, column=1, pady=10)
password_entry.config(width=25)

# Button

login_button = Button(frame, command=login, text="LOG IN", bg="WHITE", fg="BLUE", font=("Arial", 10))
login_button.grid(row=11, column=0, columnspan=2, padx=10, pady=20)

sign_up_button = Button(frame, text="SIGN UP", command=signin, bg="BLACK", fg="BLUE", font=("Arial", 10))
sign_up_button.grid(row=14, column=1, padx=10, pady=20)

show_button = Button(frame, command=hide)
show_button.grid(row=9, column=2, padx=10, pady=10)

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

access3 = Button(home_window, text="BINARY", bg="BLACK", fg="GREEN", command=acs3_btn)
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

# CHAPTER 1 QUIZ BTNS

######## C1 B1

chap1_quiz1 = Button(topic_con_btns1, text="QUIZ1", font=("Arial", 30), fg="BLACK", bg="GRAY", command=into_1)
chap1_quiz1.place(x=600, y=170)

quiz_start1 = Frame(root)
quiz_start1.config(bg="GRAY")
quiz_start1.config(height=864, width=1540)

to_start1 = Button(quiz_start1, text="START", command=no_1)
to_start1.place(x=750, y=500)
to_start1.config(height=10, width=30)

#

q1 = Frame(root)
q1.config(bg="GRAY")
q1.config(height=864, width=1540)

question1 = Label(q1)
question1.place(x=100, y=100)
question1.config(font=("Arial", 30))

answer1 = Entry(q1)
answer1.place(x=300, y=300)
answer1.config(width=50)

done1 = Button(q1, text="NEXT QUESTION")
done1.place(x=400, y=500)
done1.config(height=10, width=20)
done1.config(font=("HELVETICA", 10), bg="BLACK", fg="GREEN")

####### C1 B2

chap1_quiz2 = Button(topic_con_btns1, text="QUIZ2", font=("Arial", 30), fg="BLACK", bg="GRAY", command=into_2)
chap1_quiz2.place(x=600, y=545)

quiz_start2 = Frame(root)
quiz_start2.config(bg="GRAY")
quiz_start2.config(height=864, width=1540)

to_start2 = Button(quiz_start2, text="START", command=no_2)
to_start2.place(x=750, y=500)
to_start2.config(height=10, width=30)

#

q2 = Frame(root)
q2.config(bg="GRAY")
q2.config(height=864, width=1540)

question2 = Label(q2)
question2.place(x=100, y=100)
question2.config(font=("Arial", 30))

answer2 = Entry(q2)
answer2.place(x=300, y=300)
answer2.config(width=50)

done2 = Button(q2, text="NEXT QUESTION")
done2.place(x=400, y=500)
done2.config(height=10, width=20)
done2.config(font=("HELVETICA", 10), bg="BLACK", fg="GREEN")

####### C1 F1

chap1_quiz_final1 = Button(topic_con_btns1, text="FINAL QUIZ1", font=("Arial", 30), fg="BLACK", bg="GRAY", command=into_final1)
chap1_quiz_final1.place(x=900, y=350)
chap1_quiz_final1.config(height=0, width=10)

quiz_start_final1 = Frame(root)
quiz_start_final1.config(bg="GRAY")
quiz_start_final1.config(height=864, width=1540)

to_start_final1 = Button(quiz_start_final1, text="START", command=final_no_1)
to_start_final1.place(x=750, y=500)
to_start_final1.config(height=10, width=30)

#

q_final1 = Frame(root)
q_final1.config(bg="GRAY")
q_final1.config(height=864, width=1540)

final_question1 = Label(q_final1)
final_question1.place(x=100, y=100)
final_question1.config(font=("Arial", 30))

final_answer1 = Entry(q_final1)
final_answer1.place(x=300, y=300)
final_answer1.config(width=50)

final_done1 = Button(q_final1, text="NEXT QUESTION")
final_done1.place(x=400, y=500)
final_done1.config(height=10, width=20)
final_done1.config(font=("HELVETICA", 10), bg="BLACK", fg="GREEN")

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

######### C2 B1

chap2_quiz1 = Button(topic_con_btns2, text="QUIZ3", font=("Arial", 30), fg="BLACK", bg="GRAY", command=into_3)
chap2_quiz1.place(x=670, y=170)

quiz_start3 = Frame(root)
quiz_start3.config(bg="GRAY")
quiz_start3.config(height=864, width=1540)

to_start3 = Button(quiz_start3, text="START", command=no_3)
to_start3.place(x=750, y=500)
to_start3.config(height=10, width=30)

#

q3 = Frame(root)
q3.config(bg="GRAY")
q3.config(height=864, width=1540)

question3 = Label(q3)
question3.place(x=100, y=100)
question3.config(font=("Arial", 30))

answer3 = Entry(q3)
answer3.place(x=300, y=300)
answer3.config(width=50)

done3 = Button(q3, text="NEXT QUESTION")
done3.place(x=400, y=500)
done3.config(height=10, width=20)
done3.config(font=("HELVETICA", 10), bg="BLACK", fg="GREEN")

######### C2 B2

chap2_quiz2 = Button(topic_con_btns2, text="QUIZ4", font=("Arial", 30), fg="BLACK", bg="GRAY", command=into_4)
chap2_quiz2.place(x=670, y=540)

quiz_start4 = Frame(root)
quiz_start4.config(bg="GRAY")
quiz_start4.config(height=864, width=1540)

to_start4 = Button(quiz_start4, text="START", command=no_4)
to_start4.place(x=750, y=500)
to_start4.config(height=10, width=30)

#

q4 = Frame(root)
q4.config(bg="GRAY")
q4.config(height=864, width=1540)

question4 = Label(q4)
question4.place(x=100, y=100)
question4.config(font=("Arial", 30))

answer4 = Entry(q4)
answer4.place(x=300, y=300)
answer4.config(width=50)

done4 = Button(q4, text="NEXT QUESTION")
done4.place(x=400, y=500)
done4.config(height=10, width=20)
done4.config(font=("HELVETICA", 10), bg="BLACK", fg="GREEN")


######### C2 F2

chap2_quiz_final2 = Button(topic_con_btns2, text="FINAL QUIZ2", font=("Arial", 30), fg="BLACK", bg="GRAY", command=into_final2)
chap2_quiz_final2.place(x=610, y=680)
# chap2_quiz_final2.config(height=0, width=10)

quiz_start_final2 = Frame(root)
quiz_start_final2.config(bg="GRAY")
quiz_start_final2.config(height=864, width=1540)

to_start_final2 = Button(quiz_start_final2, text="START", command=final_no_2)
to_start_final2.place(x=750, y=500)
to_start_final2.config(height=10, width=30)

#

q_final2 = Frame(root)
q_final2.config(bg="GRAY")
q_final2.config(height=864, width=1540)

final_question2 = Label(q_final2)
final_question2.place(x=100, y=100)
final_question2.config(font=("Arial", 30))

final_answer2 = Entry(q_final2)
final_answer2.place(x=300, y=300)
final_answer2.config(width=50)

final_done2 = Button(q_final2, text="NEXT QUESTION")
final_done2.place(x=400, y=500)
final_done2.config(height=10, width=20)
final_done2.config(font=("HELVETICA", 10), bg="BLACK", fg="GREEN")


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

############## C3 B1

chap3_quiz1 = Button(topic_con_btns3, text="QUIZ5", font=("Arial", 30), fg="BLACK", bg="GRAY", command=into_5)
chap3_quiz1.place(x=280, y=100)

quiz_start5 = Frame(root)
quiz_start5.config(bg="GRAY")
quiz_start5.config(height=864, width=1540)

to_start5 = Button(quiz_start5, text="START", command=no_5)
to_start5.place(x=750, y=500)
to_start5.config(height=10, width=30)

#

q5 = Frame(root)
q5.config(bg="GRAY")
q5.config(height=864, width=1540)

question5 = Label(q5)
question5.place(x=100, y=100)
question5.config(font=("Arial", 30))

answer5 = Entry(q5)
answer5.place(x=300, y=300)
answer5.config(width=50)

done5 = Button(q5, text="NEXT QUESTION")
done5.place(x=400, y=500)
done5.config(height=10, width=20)
done5.config(font=("HELVETICA", 10), bg="BLACK", fg="GREEN")


########## C3 B2


chap3_quiz2 = Button(topic_con_btns3, text="QUIZ6", font=("Arial", 30), fg="BLACK", bg="GRAY", command=into_6)
chap3_quiz2.place(x=1180, y=100)

quiz_start6 = Frame(root)
quiz_start6.config(bg="GRAY")
quiz_start6.config(height=864, width=1540)

to_start6 = Button(quiz_start6, text="START", command=no_6)
to_start6.place(x=750, y=500)
to_start6.config(height=10, width=30)

#

q6 = Frame(root)
q6.config(bg="GRAY")
q6.config(height=864, width=1540)

question6 = Label(q6)
question6.place(x=100, y=100)
question6.config(font=("Arial", 30))

answer6 = Entry(q6)
answer6.place(x=300, y=300)
answer6.config(width=50)

done6 = Button(q6, text="NEXT QUESTION")
done6.place(x=400, y=500)
done6.config(height=10, width=20)
done6.config(font=("HELVETICA", 10), bg="BLACK", fg="GREEN")



######### C3 B3

chap3_quiz3 = Button(topic_con_btns3, text="QUIZ7", font=("Arial", 30), fg="BLACK", bg="GRAY", command=into_7)
chap3_quiz3.place(x=670, y=650)

quiz_start7 = Frame(root)
quiz_start7.config(bg="GRAY")
quiz_start7.config(height=864, width=1540)

to_start7 = Button(quiz_start7, text="START", command=no_7)
to_start7.place(x=750, y=500)
to_start7.config(height=10, width=30)

#

q7 = Frame(root)
q7.config(bg="GRAY")
q7.config(height=864, width=1540)

question7 = Label(q7)
question7.place(x=100, y=100)
question7.config(font=("Arial", 30))

answer7 = Entry(q7)
answer7.place(x=300, y=300)
answer7.config(width=50)

done7 = Button(q7, text="NEXT QUESTION")
done7.place(x=400, y=500)
done7.config(height=10, width=20)
done7.config(font=("HELVETICA", 10), bg="BLACK", fg="GREEN")


######## C3 F3

chap3_quiz_final3 = Button(topic_con_btns3, text="FINAL QUIZ3", font=("Arial", 30), fg="BLACK", bg="GRAY", command=into_final3)
chap3_quiz_final3.place(x=630, y=350)
chap3_quiz_final3.config(height=0, width=10)

quiz_start_final3 = Frame(root)
quiz_start_final3.config(bg="GRAY")
quiz_start_final3.config(height=864, width=1540)

to_start_final3 = Button(quiz_start_final3, text="START", command=final_no_3)
to_start_final3.place(x=750, y=500)
to_start_final3.config(height=10, width=30)

#

q_final3 = Frame(root)
q_final3.config(bg="GRAY")
q_final3.config(height=864, width=1540)

final_question3 = Label(q_final3)
final_question3.place(x=100, y=100)
final_question3.config(font=("Arial", 30))

final_answer3 = Entry(q_final3)
final_answer3.place(x=300, y=300)
final_answer3.config(width=50)

final_done3 = Button(q_final3, text="NEXT QUESTION")
final_done3.place(x=400, y=500)
final_done3.config(height=10, width=20)
final_done3.config(font=("HELVETICA", 10), bg="BLACK", fg="GREEN")


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
