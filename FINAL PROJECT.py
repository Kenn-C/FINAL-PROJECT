import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3


def login_home():
    sign_in_frame.place_forget()
    frame.place(x=550, y=250)
    root.update()


def login():
    if log_in_validation():
        frame.place_forget()
        home()
    else:
        messagebox.showinfo(title='INVALID LOGIN', message="PLEASE TRY AGAIN.")
        login_home()


def _log():
    frame.place(x=550, y=250)
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
    sign_in_frame.place(x=550, y=250)


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
            sign_in_frame.place_forget()
            frame.place(x=550, y=250)


def to_start_window():
    home_window.pack_forget()
    start_window.pack()


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


questions_1st = [
    {"ask": "1. A set of rules and methods that describe the functionality,\n"
     "management and implementation of computers",
     "ans": "COMPUTER ARCHITECTURE"
     },
    {"ask": "2. A programmable machine",
     "ans": "COMPUTER"
     },
    {"ask": "3. A program needs this for a computer to process",
     "ans": "INSTRUCTIONS"
     },
    {"ask": "4.The only language a computer understands?",
     "ans": "MACHINE LANGUAGE"
     },
    {"ask": "5. Second Generation of Computers are based on?",
     "ans": "TRANSISTOR BASED"
     },
    {"ask": "6. Third Generation of Computers are based on?",
     "ans": "INTEGRATED CIRCUIT BASED"
     },
    {"ask": "7. Fifth Generation of Computers are based on?",
     "ans": "ULSI MICROPROCESSOR BASED"
     },
    {"ask": "8. Fourth Generation of Computers are based on?",
     "ans": "VLSI MICROPROCESSOR BASED"
     },
    {"ask": "9. Second Generation of Computers are based on?",
     "ans": "TRANSISTOR BASED"
     },
    {"ask": "10. This concept was introduced in the fourth generation of computer",
     "ans": "INTERNER"
     },
    {"ask": "11. Generation of computer where the development of natural\n "
     "language processing is introduced",
     "ans": "FIFTH GENERATION"
     },
    {"ask": "12. Programmers typically write programs in a?",
     "ans": "HIGH LEVEL LANGUAGE"
     },
    {"ask": "13. High level language contains complex constructs such as structures,\n "
     "switch case statements, classes, inheritance and?",
     "ans": "UNIONS"
     },
    {"ask": "14. VLSI means?",
     "ans": "VERY LARGE SCALE INTEGRATION"
     },
    {"ask": "15 ULSI means?",
     "ans": "ULTRA LARGE SCALE INTEGRATION"
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
    quiz_start1.place_forget()


questions_2nd = [
    {"ask": "1. This type of computer works with discrete value",
     "ans": "DIGITAL COMPUTERS"
     },
    {"ask": "2. This computer works with continuous values?",
     "ans": "ANALOG COMPUTER"
     },
    {"ask": "3. Exhibits the features of the other different types of computers",
     "ans": "HYBRID COMPUTER"
     },
    {"ask": "4. Only one user can use the reource at any time",
     "ans": "SINGLE USER"
     },
    {"ask": "5. Single computer used by a number of user at any time",
     "ans": "MULTI USER"
     },
    {"ask": "6. Number of interconnected autonomous computers shared by a \n"
     "number of user at any time",
     "ans": "NETWORK"
     },
    {"ask": "7. Set of instructions that tells he computer what, when and how",
     "ans": "SOFTWARE"
     },
    {"ask": "8. Includes all hardware parts of a computer. This part is the \n"
     "physical computer system",
     "ans": "SYSTEM DESIGN"
     },
    {"ask": "9. The computers tangible components",
     "ans": "HARDWARE"
     },
    {"ask": "10. A collection of instructions that a computer processor reads",
     "ans": "INSTRUCTION SET ARCHITECTURE"
     },
    {"ask": "11. The hardware implementation of how an ISA is implemented \n"
     "in a particular processor ",
     "ans": "MICROARICHITECTURE"
     },
    {"ask": "12. John Von Neumann developed this architecture",
     "ans": "VON NEUMANN ARCHITECTURE"
     },
    {"ask": "13. The instruction fetches and data transfers can be \n"
     "performed at the same time",
     "ans": "HARVARD ARCHITECTURE"
     },
    {"ask": "14. RISC mean?",
     "ans": "REDUCED INSTRUCTION SET COMPUTER"
     },
    {"ask": "15. CISC means?",
     "ans": "COMPLEX INSTRUCTION SET COMPUTER"
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
    quiz_start2.place_forget()


final_1st = [
    {"ask": "1. High level language cointains complex constructs sush as stuctures, \n"
     "switch case statements, classes, inheritance and ",
     "ans": "UNIONS"
     },
    {"ask": "2. RISC stands for?",
     "ans": "REDUCED INSTRUCTION SET COMPUTER"
     },
    {"ask": "3. CISC stands for?",
     "ans": "COMPLEX INSTRUCTION SET COMPUTER"
     },
    {"ask": "4. Set of instruction that tells the computer what, when and how you do",
     "ans": "SOFTWARE"
     },
    {"ask": "5. This type of computer works with discrete value",
     "ans": "DIGITAL COMPUTERS"
     },
    {"ask": "6. ULSI means?",
     "ans": "ULTRA LARGE SCALE INTERGRATION"
     },
    {"ask": "7. Includes all hardware parts of computer. This part is \n"
     "the physical computer system",
     "ans": "SYSTEM DESIGN"
     },
    {"ask": "8. First Generation of computer",
     "ans": "VACUUM TUBE BASED"
     },
    {"ask": "9. Fifth generation of computer",
     "ans": "ULSI MICROPROCESSOR BASED"
     },
    {"ask": "10. Only one user can use the resouce at any time  ",
     "ans": "SINGLE USER"
     },
    {"ask": "11. A set of rules and methods that describe the functionality, \n"
     "management and implemetation of computers",
     "ans": "COMPUTER ARCHITECTURE"
     },
    {"ask": "12. This computer works with continuos values",
     "ans": "ANALOG COMPUTER"
     },
    {"ask": "13. VLSI means",
     "ans": "VERY LARGE-SCALE INTERGRATION"
     },
    {"ask": "14. A program needs this for a computer to process",
     "ans": "INSTRUCTION"
     },
    {"ask": "15. The hardware implementaion of how an ISA is implemented \n"
     "in a particular processor ",
     "ans": "MICROARCHITECTURE"
     },
    {"ask": "16. Number of interconnected autonomous computers shared by a \n"
     "number of user at any time",
     "ans": "NETWORK"
     },
    {"ask": "17. Exhibits the features of the other different types of computers",
     "ans": "HYBRID COMPUTER"
     },
    {"ask": "18. Programmers typically write programs in a?",
     "ans": "HIGH LEVEL LANGUAGE"
     },
    {"ask": "19. A collection of instructions that a computer processor reads",
     "ans": "INSTRUCTION SET ARCHITECTURE"
     },
    {"ask": "20. Single computer shared by a number of users at any time",
     "ans": "MULTI USER"
     },
    {"ask": "21. Generation of computer where the development of natural \n"
     "language processing is introdeced",
     "ans": "FIFTH GENERATION"
     },
    {"ask": "22. The computer's tangble components",
     "ans": "HARDWARE"
     },
    {"ask": "23. John Von Neumann developed this architecture",
     "ans": "VON NEUMANN ARCHITECTURE"
     },
    {"ask": "24. The instruction fetches and data transfers can be \n"
     "performed at the same time",
     "ans": "HARVARD ARCHITERCTURE"
     },
    {"ask": "25. This concept was introduced in the fourth generation of computer",
     "ans": "INTERNET"
     },
    {"ask": "26. Fourth generations of computer",
     "ans": "VLSI MICROPROCESSOR BASED"
     },
    {"ask": "27. Third generations of computer",
     "ans": "INTEGRATED CIRCUIT BASED"
     },
    {"ask": "28. A progmmable machine",
     "ans": "COMPUTER"
     },
    {"ask": "29. The only language a computer understands",
     "ans": "MACHINE LANGUAGE"
     },
    {"ask": "30. Second generations of computer",
     "ans": "TRANSISTOR BASED"
     },
    {"ask": "31. Includes simple instruction and takes one cycle",
     "ans": "RISC"
     },
    {"ask": "32. Cointains data or the address of the data",
     "ans": "OPERAND"
     },
    {"ask": "33. Used to transport data and instructions between the processor, \n"
     "memory unit, and input/output",
     "ans": "DATA BUS"
     },
    {"ask": "34. Includes complex instructions and takes multiple cycles",
     "ans": "CISC"
     },
    {"ask": "35. Transmits the memory address specifying where the relevant \n"
     "data needs to be sent or retrieved from",
     "ans": "ADDRESS BUS"
     },
    {"ask": "36. What type of memory is external memory also known as?",
     "ans": "SECONDARY MEMORY"
     },
    {"ask": "37. Used to transmit commands from the CPU in order to control \n"
     "and coordinate all the activities within the computer",
     "ans": "CONTROL BUS"
     },
    {"ask": "38. Storage area where logic and arithmetic results are stored",
     "ans": "ACCUMULATOR"
     },
    {"ask": "39. Which type of memory is usually a static RAM or SRAM \n"
     "and holds data word by 64 or 128 bits? ",
     "ans": "REGISTER"
     },
    {"ask": "40. Specifies type of instruction to be executed",
     "ans": "OPCODE"
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
    {"ask": "1. Which type of memory is usually a static RAM or SRAM and \n"
     "holds the data word by 64 or 128 bits",
     "ans": "REGISTER"
     },
    {"ask": "2. Has a larger storage capacity but is slower?",
     "ans": "SECONDARY MEMORY"
     },
    {"ask": "3. Under which category does external memory fall?",
     "ans": "VOLATILE MEMORY"
     },
    {"ask": "4. What is the primary reason for considering internal memory essential for \n"
     "high-end tasks like video editing and 3D rending?",
     "ans": "INTERNAL MEMORY"
     },
    {"ask": "5. The internal memory has two alternative names like the Primary memory and",
     "ans": "SEMICONDUCTOR MEMORY"
     },
    {"ask": "6. The external memory is also known as the Secondary memory or the",
     "ans": "AUXILIARY MEMORY"
     },
    {"ask": "7. Is a magnetic recording medium made a thin magnetizable coating on \n"
     "a large narrow strip of plastic film",
     "ans": "MAGNETIC TAPE"
     },
    {"ask": "8. In this mode, the DMA controller again takes control of the system bus \n"
     "to transfer the entire data block in one piece, the returns the control of \n"
     "the bus to the system",
     "ans": "BURST MODE"
     },
    {"ask": "9. The enternal memory is known for its",
     "ans": "PORTABILITY"
     },
    {"ask": "10. Small, fast storage memory used for improving average access \n"
     "time and referred as a high speed memory",
     "ans": "CACHE MEMORY"
     },
    {"ask": "11. Refers to the physical memory, one central storage unit in a computer system",
     "ans": "MAIN MEMORY"
     },
    {"ask": "12. Used to store programs and data that are stored for long periods \n"
     "of time or are not in use right away",
     "ans": "AUXILIARY MEMORY"
     },
    {"ask": "13. Usually stores information in the form of physical variations on its surface \n"
     "that can be read with the aid of a beam of light ",
     "ans": "OPTICAL DISK"
     },
    {"ask": "14. Relatively a large and fast memory used to store programs and data \n"
     "during computer operation",
     "ans": "MAIN MEMORY"
     },
    {"ask": "15. The internal memory falls under the category of",
     "ans": "VOLATILE MEMORY"
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
    {"ask": "1. The process of designing and engineering processors",
     "ans": "PROCESSOR DESIGN"
     },
    {"ask": "2. Used in desktop computers and laptops",
     "ans": "x86 PROCESSORS"
     },
    {"ask": "3. Used in wide range of devices including smartphones, tablets and\n"
        "embedded systems",
     "ans": "ARM PROCESSORS"
     },
    {"ask": "4. Type of processor that is designed for use in embedded systems",
     "ans": "MICROCONTROLERS"
     },
    {"ask": "5. The brain of computer system",
     "ans": "CENTRAL PROCESSING UNIT"
     },
    {"ask": "6. Method in computing of running two or more processors to handle separate \n"
        "separate parts of an overall task",
     "ans": "PARALLEL PROCESSING"
     },
    {"ask": "7. Contains two or more processors for better performance and more efficient\n"
        "processing of multiple tasks",
     "ans": "MULTI CORE PROCESSORS"
     },
    {"ask": "8. SIMD means",
     "ans": "SINGLE INSTRUCTION MULTIPLE DATA"
     },
    {"ask": "9. MIMB means",
     "ans": "MULTIPLE INSTRUCTION MULTIPLE DATA"
     },
    {"ask": "10. Created to produce an implementation rate of ore than one\n"
        "instruction per clock cycle",
     "ans": "SUPERSCALAR PROCESSOR"
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
    {"ask": "1. The process of designing and engineering processors",
     "ans": "PROCESSOR DESIGN"
     },
    {"ask": "2. Created to produce an implementaion rate of more than \n"
     "one instruction per clock cycle",
     "ans": "SUPERSCALAR PROCESSOR"
     },
    {"ask": "3. Used in desktops computers and laptops",
     "ans": "x86 PROCESSORS"
     },
    {"ask": "4. MIMD means",
     "ans": "MULTIPLE INSTRUCTION MULTIPLE DATA"
     },
    {"ask": "5. Used in wide range od devices including smartphones, \n"
     "tablets and embedded systems",
     "ans": "ARM PROCESSORS"
     },
    {"ask": "6. SIMD means",
     "ans": "SINGLE INSTRUCTION MULTIPLE DATA"
     },
    {"ask": "7. Type of processor that is dedihned for use in embedded systems",
     "ans": "MICROCONTROLLERS"
     },
    {"ask": "8. Cointains two or more processors for better performance \n"
     "and more efficient processing of multiple tasks",
     "ans": "MULTI CORE PROCESSORS"
     },
    {"ask": "9. The brain of the computer system",
     "ans": "CENTRAL PROCESSING UNIT"
     },
    {"ask": "10. Method in computing of running two or more processors to handle \n"
     "separate parts of an overall task",
     "ans": "PARALLEL PROCESSING"
     },
    {"ask": "11. Needs to be compatible with the motherboard for proper functiong",
     "ans": "RANDOM ACCESS MEMORY"
     },
    {"ask": "12. Consists of storage drives or devices like the optical drive and hard disk ",
     "ans": "EXTERNAL MEMORY"
     },
    {"ask": "13. This memory is less expensive",
     "ans": "EXTERNAL MEMORY"
     },
    {"ask": "14. Used for decision making and an accumulator is used to stored numbers",
     "ans": "REGISTER"
     },
    {"ask": "15. Initially, computer system were designed without a",
     "ans": "MEMORY HIERARCHY"
     },
    {"ask": "16. Tells the disk controller to read the data from the drive and \n"
     "store it in the inertal buffer",
     "ans": "CENTRAL PROCESSING UNIT"
     },
    {"ask": "17. Falls under the non-volatile category",
     "ans": "EXTERNAL MEMORY"
     },
    {"ask": "18. Can store data faster that the external memory",
     "ans": "INTERNAL MEMORY"
     },
    {"ask": "19. The internal memory falls under the category of",
     "ans": "VALATILE MEMORY"
     },
    {"ask": "20. Relatively a large and fast memory used to store programs \n"
     "and data during computer operation",
     "ans": "MAIN MEMORY"
     },
    {"ask": "21. Usually stores information in the form of physical variations \n"
     "on its surface that can be read with the aid of a beam of light",
     "ans": "OPTICAL DISK"
     },
    {"ask": "22. Used to store programs and data that are stored for long periods \n"
     "of time or are not in use right away",
     "ans": "AUXILIARY MEMORY"
     },
    {"ask": "23. Refers to the physical memory, one central storge unit in a computer system",
     "ans": "MAIN MEMORY"
     },
    {"ask": "24. Small, fast storage memory used for improving average access time and \n"
     "referred as a high speed memory",
     "ans": "CACHE MEMORY"
     },
    {"ask": "25. The external memory is known for its",
     "ans": "PORTABILITY"
     },
    {"ask": "26. Is a CPU that implements a form of parallelism called instruction-level \n"
     "parallelism within a single processor",
     "ans": "SUPERSCALAR PROCESSOR"
     },
    {"ask": "27. Was another attempt to increase performance by doing \n"
     "more than one thing at a time",
     "ans": "VECTOR PROCESSING"
     },
    {"ask": "28. Can complete multiple tasks using two or more processors",
     "ans": "PARALLEL PROCESSING "
     },
    {"ask": "29. Auxiliary Memory",
     "ans": "EXTERNAL MEMORY"
     },
    {"ask": "30. Semiconductor Memory",
     "ans": "INTERNAL MEMORY"
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

    {"ask": "1. 10010\n"
    "+ 1100",
     "ans": "11110"
     },
    {"ask": "2. 1011101\n"
     "+ 1000000",
     "ans": "10011101"
     },
    {"ask": "3. 10011\n"
     "+ 1111101",
     "ans": "10010000"
     },
    {"ask": "4. 10011001\n"
     "+ 100111",
     "ans": "11000000"
     },
    {"ask": "5. 11000011\n"
     "+ 11000011",
     "ans": "11110010"
     },
    {"ask": "6. 1001100\n"
     "+ 1100101",
     "ans": "10110001"
     },
    {"ask": "7. 111111\n"
     "+ 111000",
     "ans": "1110111"
     },
    {"ask": "8. 1100011\n"
     "- 111101",
     "ans": "100110"
     },
    {"ask": "9. 1011000\n"
     "- 111000",
     "ans": "100000"
     },
    {"ask": "10. 1001111\n"
     "- 100111",
     "ans": "101000"
     },
    {"ask": "11. 1100011\n"
     "- 100100",
     "ans": "111111"
     },
    {"ask": "12. 1100010\n"
     "- 110010",
     "ans": "110000"
     },
    {"ask": "13. 101010\n"
     "+ 100001",
     "ans": "1001011"
     },
    {"ask": "14. 1100000\n"
     "- 101010",
     "ans": "110110"
     },
    {"ask": "15. 1011101\n"
     "- 111100",
     "ans": "100001"
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

    {"ask": "1. 10101\n"
     "x 101",
     "ans": "1101001"
     },
    {"ask": "2. 1100\n"
     "x 1101",
     "ans": "10011100"
     },
    {"ask": "3. 10010\n"
     "x 110",
     "ans": "1101100"
     },
    {"ask": "4. 11001\n"
     "x 11",
     "ans": "1001011"
     },
    {"ask": "5. 10111\n"
     "x 11",
     "ans": "1000101"
     },
    {"ask": "6. 10010\n"
     "x 110",
     "ans": "1101100"
     },
    {"ask": "7. 1000\n"
     "x 10",
     "ans": "10000"
     },
    {"ask": "8. 10110\n"
     "x 101",
     "ans": "1101110"
     },
    {"ask": "9. 11010\n"
     "x 11",
     "ans": "1001110"
     },
    {"ask": "10. 1100\n"
     "x 111",
     "ans": "1010100"
     },
    {"ask": "11. 110 /1100000",
     "ans": "10000"
     },
    {"ask": "12. 111 /1101001",
     "ans": "1111"
     },
    {"ask": "13. 110 /1000010",
     "ans": "1011"
     },
    {"ask": "14. 11 /111110",
     "ans": "1010"
     },
    {"ask": "15. 10 /111110",
     "ans": "11111"
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


final_3rd = [
    {"ask": "1. 10101\n"
     "x 101",
     "ans": "1101001"
     },
    {"ask": "2. 10010\n"
    "+ 1100",
     "ans": "11110"
     },
    {"ask": "3. 10010\n"
     "x 110",
     "ans": "1101100"
     },
    {"ask": "4. 10111\n"
     "x 11",
     "ans": "1000101"
     },
    {"ask": "5. 1000\n"
     "x 10",
     "ans": "10000"
     },
    {"ask": "6. 11010\n"
     "x 11",
     "ans": "1001110"
     },
    {"ask": "7. 1011101\n"
     "+ 1000000",
     "ans": "10011101"
     },
    {"ask": "8. 10 /111110",
     "ans": "11111"
     },
    {"ask": "9. 11 /111110",
     "ans": "1010"
     },
    {"ask": "10. 1100\n"
     "x 1101",
     "ans": "10011100"
     },
    {"ask": "11. 11001\n"
     "x 11",
     "ans": "1001011"
     },
    {"ask": "12. 111111\n"
     "+ 111000",
     "ans": "1110111"
     },
    {"ask": "13. 111 /1101001",
     "ans": "1111"
     },
    {"ask": "14. what is 1 + 144?",
     "ans": "145"
     },
    {"ask": "15. 110 /1000010",
     "ans": "1011"
     },
    {"ask": "16. 1011101\n"
     "- 111100",
     "ans": "100001"
     },
    {"ask": "17. 10010\n"
     "x 110",
     "ans": "1101100"
     },
    {"ask": "18. 10110\n"
     "x 101",
     "ans": "1101110"
     },
    {"ask": "19. 100 /11000",
     "ans": "110"
     },
    {"ask": "20. 101 /10010001",
     "ans": "11101"
     },
    {"ask": "21. 11000011\n"
     "+ 11000011",
     "ans": "11110010"
     },
    {"ask": "22. 110 /1000010",
     "ans": "1011"
     },
    {"ask": "23. 1100011\n"
     "- 111101",
     "ans": "100110"
     },
    {"ask": "24. 1001100\n"
     "+ 1100101",
     "ans": "10110001"
     },
    {"ask": "25. 10011\n"
     "+ 1111101",
     "ans": "10010000"
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


exam = [
    {"ask": "1. The process of designing and enginnering processors",
     "ans": "PROCESSOR DESIGN"
     },
    {"ask": "2. Used in desktops computers and laptops",
     "ans": "x86 PROCESSORS"
     },
    {"ask": "3. Used in wide range of devices including smartphones, \n"
     "tablets and embedded system",
     "ans": "ARM PROCESSORS"
     },
    {"ask": "4. Type of processors is designed for use in embedded systems",
     "ans": "MICROCONTROLLERS"
     },
    {"ask": "5. The brain of the computer system",
     "ans": "CENTRAL PROCESSING UNIT"
     },
    {"ask": "6. Method in computing of running two or more processors \n"
     "to handle separate parts of \n"
     "an overall task",
     "ans": "PARALLEL PROCESSING"
     },
    {"ask": "7. Contains two or more processors for better performance \n"
     "and more efficient \n"
     "processing of multiple tasks",
     "ans": "MULTI CORE PROCESSORS"
     },
    {"ask": "8. SIMD means",
     "ans": "SINGLE INSTRUCTION MULTIPLE DATA"
     },
    {"ask": "9. MIMD means",
     "ans": "MULTIPLE INSTRUCTION MULTIPLE DATA"
     },
    {"ask": "10. Created to produce an implementation rate of more than \n"
     "one instruction per clock cyle",
     "ans": "SUPERSCALAR PROCESSOR"
     },
    {"ask": "11. This type of computer works with discrete value",
     "ans": "DIGITAL COMPUTER"
     },
    {"ask": "12. This computer works with continuous values",
     "ans": "ANALOG COMPUTER"
     },
    {"ask": "13. Exhibits the features of the other different tyes of computers",
     "ans": "HYBRID COMPUTER"
     },
    {"ask": "14. Only one user can use the resource at any time",
     "ans": "SINGLE USER"
     },
    {"ask": "15. Single computer shared by a number of user at any time",
     "ans": "MULTI USER"
     },
    {"ask": "16. Number of interconnected autonomous computers shared \n"
     "by a number of user at any time",
     "ans": "NETWORK"
     },
    {"ask": "17. Set of instructions that tells the computer what, when and how to do",
     "ans": "SOFTWARE"
     },
    {"ask": "18. The computer's tangible components",
     "ans": "HARDWARE"
     },
    {"ask": "19. Includes all hardware parts of a computer. This part is \n"
     "the physical computer system",
     "ans": "SYSTEM DESIGN"
     },
    {"ask": "20. A collection of instructions that a computer processor reads",
     "ans": "INSTRUCTION SET ARCHITECTURE"
     },
    {"ask": "21. The hardware implementation of how an ISA is implemented \n"
     "in a particular processor",
     "ans": "MICROARCHITECTURE"
     },
    {"ask": "22. John Von Neumann developed this architecture",
     "ans": "VON NEUMANN ARCHITECTURE"
     },
    {"ask": "23. The instruction fetches and data transfers can be performed \n"
     "at the same time",
     "ans": "HARVARD ARCHITECTURE"
     },
    {"ask": "24. RISC means",
     "ans": "REDUCED INSTRUCTION SET COMPUTER"
     },
    {"ask": "25. CISC means",
     "ans": "COMPLEX INSTRUCTION SET COMPUTER"
     },
    {"ask": "26. A set of rules and methods that describe the functionality, \n"
     "management and implementation of computers",
     "ans": "COMPUTER ARCHITECTURE"
     },
    {"ask": "27. A programmable machine",
     "ans": "COMPUTER"
     },
    {"ask": "28. A program needs this for a computer to process",
     "ans": "INSTRUCTION"
     },
    {"ask": "29. The only language a computer understands",
     "ans": "MACHINE LANGUAGE"
     },
    {"ask": "30. First Generation of a computer",
     "ans": "VACUUM TUBE BASED"
     },
    {"ask": "31. Second Generation  of a computer",
     "ans": "TRANSISTOR BASED"
     },
    {"ask": "32. Third Generation of a computer",
     "ans": "INTERGRATED CIRCUIT BASED"
     },
    {"ask": "33. Fourth Generation of computer",
     "ans": "VLSI MICROPROCESSOR BASED"
     },
    {"ask": "34. Fifth Generation of computer",
     "ans": "ULSI MICROPROCESSOR BASED"
     },
    {"ask": "35. This concept was introduced in the fourth generation of computer",
     "ans": "INTERNET"
     },
    {"ask": "36. Generation of computer where the development of natural language \n"
     "processing is introduced",
     "ans": "FIFTH GENERATION"
     },
    {"ask": "37. Programmers typically write programs in a?",
     "ans": "HIGH LEVEL LANGUAGE"
     },
    {"ask": "38. High level language contains complex constructs such as structures, \n"
     "switvh case statements, classes, inheritance and",
     "ans": "UNIONS"
     },
    {"ask": "39. VLSI means",
     "ans": "VERY LARGE-SCALE INTEGRATION"
     },
    {"ask": "40. ULSI means",
     "ans": "ULTRA LARGE SCALE INTEGRATION"
     },
    {"ask": "41. The External Memory is known for its",
     "ans": "PORTABILITY"
     },
    {"ask": "42. Small, fast storage memory used for improving average \n"
     "access time and referred as a high speed memory",
     "ans": "CACHE MEMORY"
     },
    {"ask": "43. Refers to the physical memory, one central storage unit \n"
     "in a computer system",
     "ans": "MAIN MEMORY"
     },
    {"ask": "44. Used to store programs and data that are stored for long periods \n"
     "of times or are not in used right away",
     "ans": "AUXILIARY MEMORY"
     },
    {"ask": "45. Usually stores information in the form of physical variations on \n"
     "its surface that can be read with the aid of a beam of light",
     "ans": "OPTICAL DISK"
     },
    {"ask": "46. Relatively a large and fast memory used to store programs and data \n"
     "during computer operation",
     "ans": "MAIN MEMORY"
     },
    {"ask": "47. Semiconductor memory",
     "ans": "INTERNAL MEMORY"
     },
    {"ask": "48. Auxiliary memory",
     "ans": "EXTERNAL MEMORY"
     },
    {"ask": "49. The internal memory falls under the category of",
     "ans": "VALATILE MEMORY"
     },
    {"ask": "50. Needs to be compatible with the motherboard for proper functioning",
     "ans": "RANDOM ACCESS MEMORY"
     },
    {"ask": "51. Consists of storage drives or devices like the optical drive and hard disk",
     "ans": "EXTERNAL MEMORY"
     },
    {"ask": "52. This memory is less expensive",
     "ans": "EXTERNAL MEMORY"
     },
    {"ask": "53. Used for decision making and an accumulator is used to stored numbers",
     "ans": "REGISTER"
     },
    {"ask": "54. Initially, computer system were designed without a",
     "ans": "MEMORY HIERARCHY"
     },
    {"ask": "55. Tells the disk controller to read the data from the drive and store \n"
     "it in the internal buffer",
     "ans": "CENTRAL PROCESSING UNIT"
     },
    {"ask": "56. Falls under the non-volatile category",
     "ans": "EXTERNAL MEMORY"
     },
    {"ask": "57. Can store data faster that the external memory",
     "ans": "INTERNAL MEMORY"
     },
    {"ask": "58. Can complete multiple tasks using two or more processors",
     "ans": "PARALLEL PROCESSING"
     },
    {"ask": "59. Was another attempt to increase performance by doing more than \n"
     "one thing at a time",
     "ans": "VECTOR PROCESSING"
     },
    {"ask": "60. Is a CPU that implements a form of parallelism called instruction-level \n"
     "parallelism within a single processor",
     "ans": "SUPERSCALAR PROCESSOR"
     },
    {"ask": "61. 10010\n"
    "+ 1100",
     "ans": "11110"
     },
    {"ask": "62. 11001\n"
     "x 11",
     "ans": "1001011"
     },
    {"ask": "63. 111 /1101001",
     "ans": "1111"
     },
    {"ask": "64. 1011101\n"
     "- 111100",
     "ans": "100001"
     },
    {"ask": "65. 10010\n"
     "x 110",
     "ans": "1101100"
     },
    {"ask": "66. 10110\n"
     "x 101",
     "ans": "1101110"
     },
    {"ask": "67. 100 /11000",
     "ans": "110"
     },
    {"ask": "68. 101 /10010001",
     "ans": "11101"
     },
    {"ask": "69. 1100011\n"
     "- 111101",
     "ans": "100110"
     },
    {"ask": "70. 10011\n"
     "+ 1111101",
     "ans": "10010000"
     }

]

exam_num1 = 0
exam_ans1 = 0


def into_exam():
    start_exam.place(x=0, y=0)


def exam1():
    global exam_num1
    q_exam.place(x=0, y=0)
    examine(exam_num1)


def examine(z):
    global exam
    if z < len(exam):
        ques = exam[z].get("ask")
        correct = exam[z].get("ans")
        ques_exam.config(text=f'{ques}')
        done_exam.config(command=lambda: check_exam(correct))
    else:
        end_exam()


def check_exam(ex):
    global exam_num1, exam_ans1
    user_ans = str(ans_exam.get())
    if user_ans == str(ex):
        exam_ans1 += 1

    exam_num1 += 1

    if exam_num1 < len(exam):
        ans_exam.delete(0, END)
        examine(exam_num1)

    else:
        end_exam()


def end_exam():
    global exam_num1
    messagebox.showinfo("WELL DONE", f"QUIZ COMPLETE\n Your Score is: {exam_ans1}/{len(exam)}")
    q_exam.place_forget()
    start_exam.place_forget()


#############################3


def t1():
    topic_con_btns1.pack_forget()
    tpc1.pack(expand=True, fill=BOTH)


def t2():
    topic_con_btns1.pack_forget()
    tpc2.pack(expand=True, fill=BOTH)


def t3():
    topic_con_btns1.pack_forget()
    tpc3.pack(expand=True, fill=BOTH)


def t4():
    topic_con_btns1.pack_forget()
    tpc4.pack(expand=True, fill=BOTH)


def t5():
    topic_con_btns1.pack_forget()
    tpc5.pack(expand=True, fill=BOTH)


def back_t1():
    tpc1.pack_forget()
    tpc2.pack_forget()
    tpc3.pack_forget()
    tpc4.pack_forget()
    tpc5.pack_forget()
    topic_con_btns1.pack(expand=True, fill=BOTH)


def t6():
    topic_con_btns2.pack_forget()
    tpc6.pack(expand=True, fill=BOTH)


def t7():
    topic_con_btns2.pack_forget()
    tpc7.pack(expand=True, fill=BOTH)


def t8():
    topic_con_btns2.pack_forget()
    tpc8.pack(expand=True, fill=BOTH)


def t9():
    topic_con_btns2.pack_forget()
    tpc9.pack(expand=True, fill=BOTH)


def t10():
    topic_con_btns2.pack_forget()
    tpc10.pack(expand=True, fill=BOTH)


def back_t2():
    tpc6.pack_forget()
    tpc7.pack_forget()
    tpc8.pack_forget()
    tpc9.pack_forget()
    tpc10.pack_forget()
    topic_con_btns2.pack(expand=True, fill=BOTH)


def t11():
    topic_con_btns3.pack_forget()
    tpc11.pack(expand=True, fill=BOTH)


def back_t3():
    tpc11.pack_forget()
    topic_con_btns3.pack(expand=True, fill=BOTH)


def on_mousewheel(event):
    objective_1.yview_scroll(-1 * (event.delta // 120), 'units')
    objective_2.yview_scroll(-1 * (event.delta // 120), 'units')
    objective_3.yview_scroll(-1 * (event.delta // 120), 'units')
    tpc1.yview_scroll(-1 * (event.delta // 120), 'units')
    tpc2.yview_scroll(-1 * (event.delta // 120), 'units')
    tpc3.yview_scroll(-1 * (event.delta // 120), 'units')
    tpc4.yview_scroll(-1 * (event.delta // 120), 'units')
    tpc5.yview_scroll(-1 * (event.delta // 120), 'units')
    tpc6.yview_scroll(-1 * (event.delta // 120), 'units')
    tpc7.yview_scroll(-1 * (event.delta // 120), 'units')
    tpc8.yview_scroll(-1 * (event.delta // 120), 'units')
    tpc9.yview_scroll(-1 * (event.delta // 120), 'units')
    tpc10.yview_scroll(-1 * (event.delta // 120), 'units')
    tpc11.yview_scroll(-1 * (event.delta // 120), 'units')


def out():
    home_window.pack_forget()
    start_window.pack_forget()
    frame.place(x=550, y=250)


# start


root = Tk()

window = root
window.title("Login Form")
window.geometry("1920x1080")
window.state("zoomed")
winBG = ImageTk.PhotoImage(file='C:/Users/kenneth/Pictures/Saved Pictures/BG1.jpg')
winBg = Label(window, image=winBG, bd=0)
winBg.place(x=0, y=0)

# logbg = Image.open("C:/Users/kenneth/Pictures/Saved Pictures/loginbutton.png")
# logbg = logbg.resize((90, 60))
# logbg = ImageTk.PhotoImage(logbg)

# login

frame = Frame(root)
frame.place(x=550, y=250)

frame_bg = ImageTk.PhotoImage(file="C:/Users/kenneth/Pictures/Saved Pictures/PLS5.jpg")
frame_bg1 = Label(frame, image=frame_bg, bd=0)
frame_bg1.place(x=0, y=0)
# binding
# "C:\Users\kenneth\Pictures\Saved Pictures\BG4.jpg"

# f1 = frame.create_image(100, 165, image=logbg)
# frame.tag_bind(f1, "<Button>", lambda event: login())

# Label


login_label = Label(frame, text='USER LOG IN', bg="#5E2612", fg="#FF8247", font=("Display", 10))
login_label.grid(row=5, column=0, columnspan=2, pady=30)

us_bg1 = ImageTk.PhotoImage(file="C:/Users/kenneth/Pictures/Saved Pictures/US6.jpg")
username_label = Label(frame, text='ENTER YOUR USERNAME', bg="#8B2252", fg="#FF8247", font=("Arial", 8),
                       compound="center", image=us_bg1, bd=0)
username_label.grid(row=7, column=0)

pass_bg1 = ImageTk.PhotoImage(file="C:/Users/kenneth/Pictures/Saved Pictures/US6.jpg")
password_label = Label(frame, text="ENTER YOUR PASSWORD", bg="#8B2252", fg="#FF8247", font=("Arial", 8),
                       compound="center", image=pass_bg1, bd=0)
password_label.grid(row=9, column=0)

dont_label = Label(frame, text="Don't have an account?", bg="#8B2252", fg="#FF8247", font=("Arial", 8))
dont_label.grid(row=14, column=0)

# Entry

username_entry = Entry(frame)
username_entry.grid(row=7, column=1, pady=10)
username_entry.config(width=20)

password_entry = Entry(frame)
password_entry.grid(row=9, column=1, pady=10)
password_entry.config(width=20)

# Button

login_button = Button(frame, command=login, text="LOG IN", bg="#8B2252", fg="#FF8247", font=("Arial", 10))
login_button.grid(row=11, column=0, columnspan=2, padx=10, pady=20)

sign_up_button = Button(frame, text="SIGN UP", command=signin, bg="#8B2252", fg="#FF8247", font=("Arial", 8))
sign_up_button.grid(row=14, column=1)

show_button = Button(frame, command=hide)
show_button.grid(row=9, column=2, padx=15, pady=10)

# signin

sign_in_frame = Frame(root)
sign_in_frame.config(bg="#1F1F1F")

sign_in_frame_bg = ImageTk.PhotoImage(file="C:/Users/kenneth/Pictures/Saved Pictures/PLS5.jpg")
sign_in_frame_bg1 = Label(sign_in_frame, image=sign_in_frame_bg, bd=0)
sign_in_frame_bg1.place(x=0, y=3)

# SLabel

signup_label = Label(sign_in_frame, text='CREATE AN ACCOUNT', bg='#8B2252', fg='#FF8247', font=('Arial', 10))
signup_label.grid(row=0, column=0, columnspan=2, pady=30)

us_enter_bg1 = ImageTk.PhotoImage(file="C:/Users/kenneth/Pictures/Saved Pictures/US6.jpg")
username_label = Label(sign_in_frame, text='ENTER YOUR USERNAME', bg="#8B2252", fg="#FF8247", font=("Arial", 8),
                       compound="center", image=us_enter_bg1, bd=0)
username_label.grid(row=6, column=0)

pass_enter_bg1 = ImageTk.PhotoImage(file="C:/Users/kenneth/Pictures/Saved Pictures/US6.jpg")
password_label = Label(sign_in_frame, text="ENTER YOUR PASSWORD", bg="#8B2252", fg="#FF8247", font=("Arial", 8),
                       compound="center", image=pass_enter_bg1, bd=0)
password_label.grid(row=7, column=0)

confirm_enter_bg1 = ImageTk.PhotoImage(file="C:/Users/kenneth/Pictures/Saved Pictures/US6.jpg")
confirm_label = Label(sign_in_frame, text="CONFIRM PASSWORD", bg='#8B2252', fg='#FF8247', font=('Arial', 8),
                      compound="center", image=confirm_enter_bg1, bd=0)
confirm_label.grid(row=8, column=0)

already = Label(sign_in_frame, text='Already have an account?', bg="#8B2252", fg="#FF8247", font=('Arial', 8))
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
taC = Checkbutton(sign_in_frame, text="I Agree to the Terms and Conditions", bg="#8B2252", fg="#FF8247", variable=check,
                  font=('Arial', 7),
                  cursor='hand2')
taC.grid(row=10, column=1)

sign1 = Button(sign_in_frame, text='SIGN UP', font=('Arial', 12), bg='#8B2252', fg='#FF8247', command=insert_data)
sign1.grid(row=12, column=0, columnspan=2, pady=20)

log = Button(sign_in_frame, text='Log in', font=('Arial', 8), bg='#8B2252', fg='#FF8247', cursor="hand2",
             command=lambda: _log())
log.grid(row=14, column=1)

# STARTING WINDOW

start_window = Frame(root)
start_window.config(height=1080, width=1980)
start_window.place(x=1920, y=1080)

start_bg1 = ImageTk.PhotoImage(file="C:/Users/kenneth/Pictures/Saved Pictures/STRT.jpg")
starting_window = Label(start_window, image=start_bg1, bd=0, highlightthickness=0)
starting_window.place(x=0, y=0)

comp_bg1 = ImageTk.PhotoImage(file="C:/Users/kenneth/Pictures/Saved Pictures/REDO2.jpg")
comp = Label(start_window, text="C O M P U T E R", font=("Times", 70), bg="#8B2252", fg="BLUE", compound="center",
             image=comp_bg1, bd=0)
comp.place(x=0, y=10)

archi_bg1 = ImageTk.PhotoImage(file="C:/Users/kenneth/Pictures/Saved Pictures/PLSSS.jpg")
archi = Label(start_window, text="A R C H I T E C T U R E", font=("Times", 70), bg="#8B2252", fg="BLUE",
              compound="center", image=archi_bg1, bd=0)
archi.place(x=234, y=300)

start1 = Button(start_window, text="START", font=("Fixedsys", 30), bg="#8B1A1A", fg="BLUE", command=home_enter)
start1.place(x=650, y=650)

# HOME WINDOW

home_window = Frame(root)
home_window.place(x=1540, y=864)
home_window.config(height=864, width=1540)

home_bg1 = ImageTk.PhotoImage(file="C:/Users/kenneth/Pictures/Saved Pictures/EHM.jpg")
h1_window = Label(home_window, image=home_bg1, bd=0)
h1_window.place(x=0, y=0)

home_screen = Label(home_window, text="COURSE MODULE", font=("Fixedsys", 40), bg="#FFE4C4", fg="BLACK")
home_screen.place(x=550, y=50)

back_start = Button(home_window, text="🏠", bg="#FFE4C4", font=(15) , command=to_start_window)
back_start.config(height=2, width=5)
back_start.pack(anchor="nw")

# CHAPTER BUTTON


chap1 = Button(home_window, text="CHAPTER 1", font=("Fixedsys", 30), fg="BLACK", bg="#FFE4C4", command=chapter_1)
chap1.place(x=250, y=200)

chap2 = Button(home_window, text="CHAPTER 2", font=("Fixedsys", 30), fg="BLACK", bg="#FFE4C4", command=chapter_2)
chap2.place(x=675, y=200)

chap3 = Button(home_window, text="CHAPTER 3", font=("Fixedsys", 30), fg="BLACK", bg="#FFE4C4", command=chapter_3)
chap3.place(x=1100, y=200)

# TOPIC ACCESS BUTTON

access1 = Button(home_window, text="C O M P U T E R "
                                   "\n"
                                   "\n"
                                   "\n"
                                   "A R C H I T E C T U R E", font=("Fixedsys", 13), bg="#8B3E2F", fg="#FCE6C9", command=acs1_btn)
access1.place(x=200, y=300)
access1.config(height=15, width=30)

access2 = Button(home_window, text="C O M P U T E R"
                                   "\n"
                                   "\n"
                                   "\n"
                                   "M E M O R Y", font=("Fixedsys", 13), bg="#CD6600", fg="#FCE6C9", command=acs2_btn)
access2.place(x=625, y=300)
access2.config(height=15, width=30)

access3 = Button(home_window, text="B I N A R Y"
                                   "\n"
                                   "\n"
                                   "\n"
                                   "D I G I T S ", font=("Fixedsys", 13), bg="#FF8C00", fg="#FCE6C9", command=acs3_btn)
access3.place(x=1050, y=300)
access3.config(height=15, width=30)

# acc3 = Image.open("C:/Users/kenneth/Pictures/Saved Pictures/START.png")
# acc3 = acc3.resize((1100, 1100))
# acc3 = ImageTk.PhotoImage(acc3)

# ac3 = start_window.create_image(1000, 1000, image=acc3)
# home_window.tag_bind(acc3, "<Button>", lambda event: acs3_btn())

# "C:UserskennethPicturesSaved PicturesCHAPTER_BG1.jpg"

# CHAPTER OBJECTIVE


objective_1 = Canvas(root, height=1980, width=1080, scrollregion=(0, 0, 10000, 10000),)

summary = """
C H A P T E R  O B J E C T I V E S
\n
Upon completion of this course/module on computer architecture, students will acquire a comprehensive understanding of various instruction set architectures, 
including RISC and CISC.
\n 
They will be able to compare and contrast these architectures, evaluating their advantages and disadvantages in terms of instruction execution efficiency, 
hardware complexity, and performance optimization. 
\n
Additionally, students will explore diverse computer architectures such as von Neumann and Harvard architectures, understanding their distinctive features and applications. 
Moreover, they will grasp the principles of input/output interfaces, discerning their significance in facilitating communication between the computer system and external devices, 
and analyze strategies for efficient I/O data transfer and device management within computing systems.
"""

obj1 = Label(objective_1, text=summary, font=("Times", 35), fg="BLACK", justify="left", anchor="w", wraplength=1300)
obj1.pack()

objective_1.create_window(700, 700, window=obj1)

back1 = Button(objective_1,text="🏠", font=(15), command=back_obj1)
back1.config(height=2, width=5)
back1.pack(anchor="nw")

canvas = Canvas(objective_1, borderwidth=0, background="#ffffff")
scrollbar = Scrollbar(objective_1, orient="vertical", command=canvas.yview)
scrollable_frame = Frame(canvas)

objective_1.bind_all(
    "<Configure>",
    lambda e: objective_1.configure(
        scrollregion=objective_1.bbox("all")
    )
)
objective_1.bind_all("<MouseWheel>", on_mousewheel)
scrollable_frame.bind_all()

canvas.bind_all("<MouseWheel>", on_mousewheel)

###########################################################################


objective_2 = Canvas(root, height=1980, width=1080, scrollregion=(0, 0, 10000, 10000),)


summary2 = """
C H A P T E R  O B J E C T I V E S 
\n
Understanding computer memory is crucial in comprehending how computers function. 
In this chapter, we will tackle the definitions and functions of different types of Computer Memory.

Expected Course

- Purpose of Memory
- Types of Memory
- Memory Hierarchy"""

obj2 = Label(objective_2, text=summary2, font=("Times", 35), fg="BLACK", justify="left", anchor="w", wraplength=1300)
obj2.place(x=10, y=50)

objective_2.create_window(700, 350, window=obj2)


back2 = Button(objective_2, text="🏠", font=(15), command=back_obj2)
back2.config(height=2, width=5)
back2.pack(anchor="nw")

canvas2 = Canvas(objective_2, borderwidth=0, background="#ffffff")
scrollbar2 = Scrollbar(objective_2, orient="vertical", command=canvas2.yview)
scrollable_frame2 = Frame(canvas2)

objective_2.bind_all(
    "<Configure>",
    lambda e: objective_2.configure(
        scrollregion=objective_2.bbox("all")
    )
)
objective_2.bind_all("<MouseWheel>", on_mousewheel)
scrollable_frame2.bind_all()

canvas2.bind_all("<MouseWheel>", on_mousewheel)


objective_3 = Canvas(root, height=1980, width=1080, scrollregion=(0, 0, 10000, 10000),)

summary3 = """
C H A P T E R  O B J E C T I V E S 

Learning about binary digits is fundamental to understanding how computers store and process information. This course chapter aims to provide the basic concepts of Binary, 
The Binary Number Systems and the Binary Arithmetic"""

obj3 = Label(objective_3, text=summary3, font=("Times", 35), fg="BLACK", justify="left", anchor="w", wraplength=1300)
obj3.pack(side="left")

objective_3.create_window(700, 200, window=obj3)


back3 = Button(objective_3, text="🏠", font=(15), command=back_obj3)
back3.config(height=3, width=5)
back3.pack(anchor="nw")

canvas3 = Canvas(objective_3, borderwidth=0, background="#ffffff")
scrollbar3 = Scrollbar(objective_3, orient="vertical", command=canvas3.yview)
scrollable_frame3 = Frame(canvas3)

objective_3.bind_all(
    "<Configure>",
    lambda e: objective_3.configure(
        scrollregion=objective_3.bbox("all")
    )
)
objective_3.bind_all("<MouseWheel>", on_mousewheel)
scrollable_frame3.bind_all()

canvas3.bind_all("<MouseWheel>", on_mousewheel)

# CHAPTER 1 TOPIC

topic_con_btns1 = Frame(root, height=1980, width=1000)

first = ImageTk.PhotoImage(file="C:/Users/kenneth/Pictures/Saved Pictures/SECOND.jpg")
f1 = Label(topic_con_btns1, image=first, bd=0)
f1.place(x=0, y=0)

back4 = Button(topic_con_btns1, text="🏠", bg="#4F94CD", font=(15), command=back_top1)
back4.config(height=2, width=5)
back4.pack(anchor="nw")

chap1_top1 = Button(topic_con_btns1, text="TOPIC 1", font=("Fixedsys", 30), fg="BLACK", bg="#00CDCD", command=t1)
chap1_top1.place(x=100, y=95)

tpc1 = Canvas(root, height=1080, width=1980, scrollregion=(0, 0, 10000, 10000),)

detail1 = """"COMPUTER ARCHITECTURE
\n
can be defined as a set of rules and methods that describe the functionality, management and implementation of computers.
· The main role of Computer Architecture is to balance the performance, efficiency, cost and reliability of a computer system.

COMPUTER
· A computer is a programmable machine. It is a general purpose device that can be programmed to process information, 
and yield meaningful results.  

ADVANTAGES OF COMPUTER

• Increased efficiency and productivity

• Storage and organization of information

• Improved communication

• Access to information and resources

• Automation of repetitive tasks

DISADVANTAGES OF COMPUTER

• Dependence on technology

• Security risks

• Social isolation

• Environmental impact

• Job displacement
\n
- A computer can process the program, and produce the desired output by following each instruction in the program. 
Each program needs to contain a set of basic instructions that a computer can process. 
Henceforth, a computer can produce the desired output. An instruction is defined as a basic command that can be given to a computer.
\n
LANGUAGE OF INSTRUCTION

Programmers typically write programs in a high level language These languages contain complex constructs such as 
structures, unions, switch-case statements, classes and inheritance.
"""

info1 = Label(tpc1, text=detail1, font=("Times", 25), fg="BLACK", justify="left", anchor="w", wraplength=1500)
info1.place(x=50, y=100)

tpc1.create_window(800, 1000, window=info1)

out1 = Button(tpc1, text="🏠", font=(15), command=back_t1)
out1.config(height=2, width=5)
out1.place(x=0, y=0)

canvas4 = Canvas(tpc1, borderwidth=0, background="#ffffff")
scrollbar4 = Scrollbar(tpc1, orient="vertical", command=canvas4.yview)
scrollable_frame4 = Frame(canvas4)

tpc1.bind_all(
    "<Configure>",
    lambda e: tpc1.configure(
        scrollregion=tpc1.bbox("all")
    )
)
tpc1.bind_all("<MouseWheel>", on_mousewheel)
scrollable_frame4.bind_all()

canvas4.bind_all("<MouseWheel>", on_mousewheel)

#

chap1_top2 = Button(topic_con_btns1, text="TOPIC 2", font=("Fixedsys", 30), fg="BLACK", bg="#98F5FF", command=t2)
chap1_top2.place(x=100, y=245)

tpc2 = Canvas(root, height=1080, width=1980, scrollregion=(0, 0, 10000, 10000),)

detail2 = """"GENERATIONS OF A COMPUTER
\n
- FIRST GENERATIONS: VACUUM TUBE BASED

The main features of first generation are:

Vacuum tube technology

Unreliable

Supported machine language only

• Very costly

Generated lot of heat

Slow input and output devices

Huge size

Non-portable

Consumed lot of electricity

- SECOND GENERATIONS: TRANSISTOR

BASED

The main features of second generation are:

Use of transistor

Reliable

Smaller size

Generated less heat

Consumed less electricity

Faster than first generation computer Still very costly

Supported machine and assembly

language

- THIRD GENERATIONS: INTERGRATED

CIRCUIT BASED

The main features of third generation are:

IC used

• More reliable in comparison to previous

two generation

Smaller size

- FOURTH GENERATIONS: VLSI MICROPROCESSOR BASED

The main features of fourth generation are:

VLSI technology used

Very cheap

Portable and reliable

Used of PC's

Very small size

Pipeline processing

No A.C needed

Concept of Internet was introduced

Great developments in the fields of networks

Computers became easily available

- FIFTH GENERATIONS: ULSI MICROPROCESSOR BASED

The main features of fifth generation are:

ULSI technology

Development of true artificial

intelligence

 Development of Natural language processing

• Advancement in Parallel Processing Advancement in Superconductor technology

• More user friendly interfaces with multimedia features

Availability of very powerful and compact computer and cheaper rates

Generated less heat

Faster

• Lesser maintenance

• Still costly

• A.C needed

Consumed lesser electricity

Supported high-level language"""

info2 = Label(tpc2, text=detail2, font=("Arial", 25), fg="BLACK", justify="left", anchor="w", wraplength=1500)
info2.place(x=50, y=100)

tpc2.create_window(650, 2200, window=info2)

out2 = Button(tpc2, text="🏠", font=(15), command=back_t1)
out2.config(height=2, width=5)
out2.place(x=0, y=0)

canvas5 = Canvas(tpc2, borderwidth=0, background="#ffffff")
scrollbar5 = Scrollbar(tpc2, orient="vertical", command=canvas5.yview)
scrollable_frame5 = Frame(canvas5)

tpc2.bind_all(
    "<Configure>",
    lambda e: tpc2.configure(
        scrollregion=tpc2.bbox("all")
    )
)
tpc2.bind_all("<MouseWheel>", on_mousewheel)
scrollable_frame5.bind_all()

canvas5.bind_all("<MouseWheel>", on_mousewheel)

#

chap1_top3 = Button(topic_con_btns1, text="TOPIC 3", font=("Fixedsys", 30), fg="BLACK", bg="#FF9912", command=t3)
chap1_top3.place(x=100, y=395)

tpc3 = Canvas(root, height=1080, width=1980, scrollregion=(0, 0, 10000, 10000),)

detail3 = """"
COMPUTER TYPES

Classification based on Operating Principles

1. Digital Computer

2. Analog Computer

3. Hybrid Computer

DIGITAL COMPUTER

• Digital computers works with discrete value (1,0). In can only work with digit

It can store large amount of data

It has two state on and off

Its speed of calculation is vey high

It is easy to use

Digital computer is widely used in almost all fields of life.

Digital computer is used to calculate mathematical and logical operations.

• It accuracy is comparatively low Its readability is high

ANALOG COMPUTER

Analog computer works with continuous values

It has very limited memory

It has no state

It can perform certain types of calculations

It is difficult to use

Analog computers is used in engineering and scientific applications.

Analog computer is used for calculations and measurement of physical quantities such as weight, height, temperature and speed

• Its accuracy is high Its readability is low

HYBRID COMPUTER

• It exhibit features of analog computers and digital computers. 
The digital component normally serves as the controller and provides logical operations, 
while the analog component normally serves as the a solver of differential equations.

COMPUTER TYPES

Classification based on number of user

Single User:

• Only one user can use the resource at any time.

Multi User:

A single computer shared by a number users at any time.

Network

• A number of interconnected autonomous computers shared by a number users at any time

COMPUTERS HAS TWO KINDS OF COMPONENTS:

- SOFTWARE

- HARDWARE


* SOFTWARE IS A SET OF INSTRUCTIONS THAT TELLS THE COMPUTER WHAT TO DO, WHEN TO DO, AND HOW TO DO.

* HARDWARE REFERS TO THE COMPUTER'S TANGIBLE COMPONENTS OR DELIVERY SYSTEMS THAT STORE AND 
RUN THE WRITTEN INSTRUCTIONS PROVIDED BY THE SOFTWARE."""

info3 = Label(tpc3, text=detail3, font=("Arial", 25), fg="BLACK", justify="left", anchor="w", wraplength=1500)
info3.place(x=50, y=100)

tpc3.create_window(800, 1600, window=info3)

out3 = Button(tpc3, text="🏠", font=(15), command=back_t1)
out3.config(height=2, width=5)
out3.place(x=0, y=0)

canvas6 = Canvas(tpc3, borderwidth=0, background="#ffffff")
scrollbar6 = Scrollbar(tpc3, orient="vertical", command=canvas6.yview)
scrollable_frame6 = Frame(canvas6)

tpc3.bind_all(
    "<Configure>",
    lambda e: tpc3.configure(
        scrollregion=tpc3.bbox("all")
    )
)
tpc3.bind_all("<MouseWheel>", on_mousewheel)
scrollable_frame6.bind_all()

canvas6.bind_all("<MouseWheel>", on_mousewheel)

#

chap1_top4 = Button(topic_con_btns1, text="TOPIC 4", font=("Fixedsys", 30), fg="BLACK", bg="#104E8B", command=t4)
chap1_top4.place(x=100, y=545)

tpc4 = Canvas(root, height=1080, width=1980, scrollregion=(0, 0, 10000, 10000),)

detail4 = """"CATEGORIES OF ARCHITECTURE
\n
System design includes all hardware parts of a computer, including data processors, multiprocessors, 
memory controllers, and direct memory access. It also includes the graphics processing unit (GPU). This part is the physical computer system.

Instruction set architecture:

• An instruction set architecture, or ISA, is a collection of instructions that a computer processor reads. 
It outlines how the central processing unit (CPU) is controlled by its software, and effectively acts as the interface between the machine's hardware components
and its software.

There are two main types of instruction classifications:

1. Reduced Instruction Set Computer (RISC)

2. Complex Instruction Set Computer (CISC)

The fundamental difference between RISC and CISC is that RISC (Reduced Instruction Set Computer) includes simple 
instructions and takes one cycle, while the CISC (Complex Instruction Set Computer) includes complex instructions and takes multiple cycles

Microarchitecture:
\n
Microarchitecture is also known as computer organisation and defines the data processing and storage element and how they should be implemented into the ISA. 
It is the hardware implementation of how an ISA is implemented in a particular processor.

Von-Neumann Architecture (Neumann Model or Princeton Architecture) John Von Neumann coined and developed this architecture.

This architecture design was proposed in 1945. The Von Neumann design thus constitutes t foundation of modern computing.
It was easier to execute in real hardware
\n
- Registers

Program Counter (PC): Holds the address of the next instruction to be executed

Accumulator (AC): Storage area where logic and arithmetic results are stored Memory Address Register (MAR): 
Holds the address of a location of the data that is to be read from or written to Memory Data Register (MDR):
Temporary storage location that stores data that has been read, or data that still needs to be written

Current Instruction Register (CIR): Area where the current instruction is being carried out. 
The operation is divided into operand and opcode.

- Operand: Contains data or the address of the data (where the operation will be performed)

- Opcode: Specifies type of instruction to be executed

BUSES

Data bus: This bus is referred to as a bi- directional bus, which means "bits" can be carried in both ways. 
This bus is used to transport data and instructions between the processor, memory unit, and the input/output.

Address bus: Transmits the memory address specifying where the relevant data needs to be sent or retrieved from.
Control bus: This is also a bi-directional bus used to transmit "control signals"/commands from the CPU 
(and status signals from other components) in order to control and coordinate all the activities within the computer.

- Harvard Architecture

Harvard architecture is named after the "Harvard Mark I" relay-based computer Both types of architectures contain the 
same components, however, the main difference is that in a Harvard architecture the instruction fetches and data 
transfers can be performed at the same time (simultaneously)
 """

info4 = Label(tpc4, text=detail4, font=("Arial", 25), fg="BLACK", justify="left", anchor="w", wraplength=1500)
info4.place(x=50, y=100)

tpc4.create_window(800, 1500, window=info4)

out4 = Button(tpc4, text="🏠", font=(15), command=back_t1)
out4.config(height=2, width=5)
out4.place(x=0, y=0)

canvas7 = Canvas(tpc4, borderwidth=0, background="#ffffff")
scrollbar7 = Scrollbar(tpc4, orient="vertical", command=canvas7.yview)
scrollable_frame7 = Frame(canvas7)

tpc4.bind_all(
    "<Configure>",
    lambda e: tpc4.configure(
        scrollregion=tpc4.bbox("all")
    )
)
tpc4.bind_all("<MouseWheel>", on_mousewheel)
scrollable_frame7.bind_all()

canvas7.bind_all("<MouseWheel>", on_mousewheel)

#

chap1_top5 = Button(topic_con_btns1, text="TOPIC 5", font=("Fixedsys", 30), fg="BLACK", bg="#191970", command=t5)
chap1_top5.place(x=100, y=695)

tpc5 = Canvas(root, height=1080, width=1980, scrollregion=(0, 0, 10000, 10000),)

detail5 = """"
     M E M O R Y  U N I T
\n
-Cache Memory

• Cache memory is a very high speed memory placed in between RAM and CPU. Cache memory increases the speed of processing.

Cache memory is a storage buffer that stores the data that is used more often, temporarily, and makes them available to CPU at a fast rate.

Primary Memory
\n
• Primary memory is the main memory of computer.

It is used to store data and instructions during the processing of data. Primary memory is semiconductor memory.

• Primary memory is of two kinds: Random Access Memory (RAM) and Read Only Memory (ROM).

Secondary Memory

• The secondary memory stores data and instructions permanently. The information can be stored in secondary memory for 
a long time (years), and is generally permanent in nature unless erased by the user. It is a non-volatile memory.

• It provides back-up storage for data and instructions and has a high storage capacity than the primary memory.

\n
CISC VS RISC

What is RISC?

Reduced Instruction Set Computer (RISC) is a computer architecture that emphasizes a simple and efficient instruction set.

• RISC processors have a smaller instruction set than CISC processors, with each instruction performing a single operation.

The goal of RISC architecture is to reduce the amount of work the processor needs to do for each instruction, 
which leads to faster and more efficient processing.

• RISC processors often use pipe-lining to achieve greater performance.

Advantages of RISC:

- Simplified instruction set leads to faster processing

- Pipe-lining can increase performance • Lower power consumption

- Smaller chip size, which can lead to cost savings

• Disadvantages of RISC:

- Programs may require more instructions to complete a task than with CISC Limited ability to perform complex instructions

\n
What is CISC?

• Complex Instruction Set Computer (CISC) is a computer architecture that emphasizes a large and complex instruction set. 
CISC processors have many instructions that can perform multiple operations in a single instruction.

The goal of CISC architecture is to reduce the number of instructions a program needs to execute, which can lead to faster program execution

• CISC processors typically have more extensive hardware support for performing complex instructions. 
This allows for more sophisticated operations to be performed in a single instruction, which can lead to faster program execution. However, the increased complexity can also lead to slower processing times.

Advantages of CISC:

- Ability to perform complex instructions

- Programs require fewer instructions to execute

- Greater hardware support for performing complex instructions

• Disadvantages of CISC:

- Increased complexity can lead to slower processing times

- Larger chip size can lead to increased costs

MULTICOMPUTER AND MULTIPROCESSOR

Multiprocessor:

A Multiprocessor is a computer system with two or more central processing units (CPUs) share full access to a common RAM.

Multicomputer:

• A multicomputer system is a computer system with multiple processors that are connected together to solve a problem. Each processor has its own memory and it is accessible by that particular processor and those processors can communicate with each other via an interconnection network
"""

info5 = Label(tpc5, text=detail5, font=("Arial", 25), fg="BLACK", justify="left", anchor="w", wraplength=1500)
info5.place(x=50, y=100)

tpc5.create_window(800, 2000, window=info5)

out5 = Button(tpc5, text="🏠", font=(15), command=back_t1)
out5.config(height=2, width=5)
out5.place(x=0, y=0)

canvas8 = Canvas(tpc5, borderwidth=0, background="#ffffff")
scrollbar8 = Scrollbar(tpc5, orient="vertical", command=canvas8.yview)
scrollable_frame8 = Frame(canvas8)

tpc5.bind_all(
    "<Configure>",
    lambda e: tpc5.configure(
        scrollregion=tpc5.bbox("all")
    )
)
tpc5.bind_all("<MouseWheel>", on_mousewheel)
scrollable_frame8.bind_all()

canvas8.bind_all("<MouseWheel>", on_mousewheel)

# CHAPTER 1 QUIZ BTNS

######## C1 B1

chap1_quiz1 = Button(topic_con_btns1, text="QUIZ 1", font=("Fixedsys", 30), fg="BLACK", bg="#00FFFF", command=into_1)
chap1_quiz1.place(x=600, y=170)

quiz_start1 = Frame(root)
quiz_start1.config(bg="GRAY")
quiz_start1.config(height=864, width=1540)

###################################################################### ALL STARTING QUIZ BG

quiz_starting_bg = Image.open("C:/Users/kenneth/Pictures/Saved Pictures/TRY1.jpg")
resize = quiz_starting_bg.resize((1600, 800))
now = ImageTk.PhotoImage(resize)

###############################

starting1 = Label(quiz_start1, image=now, bd=0)
starting1.pack()

star1 = ImageTk.PhotoImage(file="C:/Users/kenneth/Pictures/Saved Pictures/STARR.jpg")
start_quiz1 = Label(quiz_start1, text="Q U I Z  T I M E !", font=("Fixedsys", 60), bg="BLUE", fg="#0000FF", compound="center", image=star1, bd=0)
start_quiz1.place(x=380, y=100)

to_start1 = Button(quiz_start1, text="START", command=no_1, bg="#98F5FF")
to_start1.place(x=650, y=630)
to_start1.config(height=5, width=30)

######################################

q1 = Frame(root)
q1.config(bg="GRAY")
q1.config(height=864, width=1540)


###################### ALL FINAL BG

kys = Image.open("C:/Users/kenneth/Pictures/Saved Pictures/FINAL.jpg")
sht1 = kys.resize((1600, 800))
ok = ImageTk.PhotoImage(sht1)

hys1 = Label(q1, image=ok, bd=0)
hys1.pack()

question1 = Label(q1)
question1.place(x=100, y=100)
question1.config(font=("Arial", 30))

answer1 = Entry(q1)
answer1.place(x=300, y=300)
answer1.config(width=50)

done1 = Button(q1, text="NEXT QUESTION")
done1.place(x=400, y=500)
done1.config(height=10, width=20)
done1.config(font=("Fixedsys", 10), bg="#FFFACD", fg="#8B8386")

####### C1 B2

chap1_quiz2 = Button(topic_con_btns1, text="QUIZ2", font=("Fixedsys", 30), fg="BLACK", bg="#8B1A1A", command=into_2)
chap1_quiz2.place(x=600, y=545)

quiz_start2 = Frame(root)
quiz_start2.config(bg="GRAY")
quiz_start2.config(height=864, width=1540)

starting2 = Label(quiz_start2, image=now, bd=0)
starting2.pack()

star2 = ImageTk.PhotoImage(file="C:/Users/kenneth/Pictures/Saved Pictures/STARR.jpg")
start_quiz2 = Label(quiz_start2, text="Q U I Z  T I M E !", font=("Fixedsys", 60), bg="BLUE", fg="#0000FF", compound="center", image=star2, bd=0)
start_quiz2.place(x=380, y=100)

to_start2 = Button(quiz_start2, text="START", command=no_2, bg="#98F5FF")
to_start2.place(x=650, y=630)
to_start2.config(height=5, width=30)

#

q2 = Frame(root)
q2.config(bg="GRAY")
q2.config(height=864, width=1540)

hys2 = Label(q2, image=ok, bd=0)
hys2.pack()


question2 = Label(q2)
question2.place(x=100, y=100)
question2.config(font=("Arial", 30))

answer2 = Entry(q2)
answer2.place(x=300, y=300)
answer2.config(width=50)

done2 = Button(q2, text="NEXT QUESTION")
done2.place(x=400, y=500)
done2.config(height=10, width=20)
done2.config(font=("Fixedsys", 10), bg="#FFFACD", fg="#8B8386")

####### C1 F1

chap1_quiz_final1 = Button(topic_con_btns1, text="FINAL QUIZ1", font=("Fixedsys", 30), fg="BLACK", bg="#FF7D40",
                           command=into_final1)
chap1_quiz_final1.place(x=900, y=350)

################ ALL FINAL QUIZ BG


quiz_start_final1 = Frame(root)
quiz_start_final1.config(bg="GRAY")
quiz_start_final1.config(height=864, width=1540)

sfq = Image.open("C:/Users/kenneth/Pictures/Saved Pictures/GREEN.jpg")
sfq.resize((1600, 800))
sref = ImageTk.PhotoImage(sfq)

sfq1 = Label(quiz_start_final1, image=sref, bd=0)
sfq1.pack()


lb1 = Label(quiz_start_final1, text="F I N A L  Q U I Z", font=("Fixedsys", 60), fg="GREEN")
lb1.place(x=400, y=100)


to_start_final1 = Button(quiz_start_final1, text="START", font=("Fixedsys", 10),bg="#48D1CC", fg="#FAF0E6", command=final_no_1)
to_start_final1.place(x=700, y=500)
to_start_final1.config(height=5, width=15)


#

q_final1 = Frame(root)
q_final1.config(bg="GRAY")
q_final1.config(height=864, width=1540)

hys3 = Label(q_final1, image=ok, bd=0)
hys3.pack()


final_question1 = Label(q_final1)
final_question1.place(x=100, y=100)
final_question1.config(font=("Arial", 30))

final_answer1 = Entry(q_final1)
final_answer1.place(x=300, y=300)
final_answer1.config(width=50)

final_done1 = Button(q_final1, text="NEXT QUESTION")
final_done1.place(x=400, y=500)
final_done1.config(height=10, width=20)
final_done1.config(font=("Fixedsys", 10), bg="#FFFACD", fg="#8B8386")

# CHAPTER 2 TOPIC

topic_con_btns2 = Frame(root, height=1080, width=1980)


second = ImageTk.PhotoImage(file="C:/Users/kenneth/Pictures/Saved Pictures/FIRST.jpg")
s1 = Label(topic_con_btns2, image=second, bd=0)
s1.place(x=0, y=0)

back5 = Button(topic_con_btns2, text="🏠", font=(15), bg="#FFE4B5", command=back_top2)
back5.config(height=2, width=5)
back5.pack(anchor="nw")

chap2_top1 = Button(topic_con_btns2, text="TOPIC 6", font=("Fixedsys", 30), fg="BLACK", bg="#FFE4B5", command=t6)
chap2_top1.place(x=150, y=50)

tpc6 = Canvas(root, height=1080, width=1980, scrollregion=(0, 0, 10000, 10000),)

detail6 = """"
C O M P U T E R  M E M O R Y 
\n
WHAT IS COMPUTER MEMORY?

Computer memory is used to store data and information permanently and temporarily. 
This data and information can be recalled whenever a user requests or demands.

Internal Storage Device vs External Storage Device

CATEGORIZATION OF MEMORY

INTERNAL MEMORY

"Semiconductor memory"

EXTERNAL MEMORY

"Auxiliary Memory"

INTERNAL MEMORY

ALTERNATIVE NAMES

The internal memory has two alternative names like the "Semiconductor Memory" and the "Primary Memory ". 
It is because it is attached to the computer and cannot be separated from the computer.

- CATEGORY

The internal memory falls under the category of "Volatile memory". The volatile memory is a memory which means 
that if one is working on some data and if the power of the computer goes off, then the information or data on the computer 
which was being worked on will not be saved on the computer.

• It is recommended that one should store the data before switching off the power supply to ROM which is a non- volatile memory

- PHYSICAL FEATURES

• The internal memory is a semiconductor memory. The internal memory consists of chips that are attached to the motherboard
and is placed inside the computer. The RAM needs to be compatible with the motherboard for proper functioning

- SPEED

The internal memory has a fast access time. It is because the internal memory is directly connected to the CPU 
for better processing purposes. Which makes the processor work easy. Resulting in the computer's speedy.

- STORAGE

The internal memory can store data faster that the external memory. But the data stored are temporary. 
And once the computer goes off the data stored will be lost. The storage capacity of the internal memory cannot store 
data which is an extensive or large amount of data.

OPERATION

The internal memory is very essential for the computer. It is because the computer will not be able to operate or run. 
Without the main memory or the internal memory because it is used for better or high end tasks. Like video editing, 3D 
rendering, and many more. The internal memory is used for processing data

\n
EXTERNAL MEMORY

ALTERNATIVE NAMES

The external memory is also known as the "Secondary memory" or the "Auxiliary memory". 
It is because the memory can be portable. It can be removed and attached to the computer according to the user's choice. 
Auxiliary means support.

- CATEGORY

The external memory falls under the non-volatile category. It is because the data worked on, can be saved and later retrieved. 
Also, it is not connected to the power supply like the internal memory.

- PHYSICAL FEAURES

External memory is not a semiconductor memory. It is magnetic and optical memories. The external memory consists of 
storage drives or devices like the optical drive and hard disk. Which can be taken from one place to another. And is 
universal, which means it can be connected to every computer. It can be interchanged from one computer to another. 

- STORAGE

The external memory can store a large amount of data. The data stored in the external memory is permanently stored for 
a large period of time until the user do not erase the data from the external memory. The data remains in the external 
memory even after switching

- PORTABILITY

The external memory is known for its portability. External memory can be taken from one place to another because it is 
also known as the backup memory. It can be connected to the computer. And they are universal. Therefore, it can be 
connected or interchange from one computer to another.

- PRICE

The external memory is less expensive compared to the internal memory. It can be interchanged and the shape mostly 
comes in universal size.
"""

info6 = Label(tpc6, text=detail6, font=("Times", 25), fg="BLACK", justify="left", anchor="n", wraplength=1500)
info6.place(x=50, y=100)

tpc6.create_window(800, 2200, window=info6)

out6 = Button(tpc6, text="🏠", font=(15), command=back_t2)
out6.config(height=2, width=5)
out6.place(x=0, y=0)

canvas9 = Canvas(tpc6, borderwidth=0, background="#ffffff")
scrollbar9= Scrollbar(tpc6, orient="vertical", command=canvas9.yview)
scrollable_frame9 = Frame(canvas9)

tpc6.bind_all(
    "<Configure>",
    lambda e: tpc6.configure(
        scrollregion=tpc6.bbox("all")
    )
)
tpc6.bind_all("<MouseWheel>", on_mousewheel)
scrollable_frame9.bind_all()

canvas9.bind_all("<MouseWheel>", on_mousewheel)

#

chap2_top2 = Button(topic_con_btns2, text="TOPIC 7", font=("Fixedsys", 30), fg="BLACK", bg="#FFE4B5", command=t7)
chap2_top2.place(x=1150, y=50)

tpc7 = Canvas(root, height=1080, width=1980, scrollregion=(0, 0, 10000, 10000),)

detail7 = """"
     M E M O R Y  H I E R A R C H Y 
\n
INTRODUCTION TO MEMORY HIERARCHY

The memory hierarchy design primarily consists of several storage devices in a computer system and 
separated based on their response time or speed of access.

LEVEL 0

REGISTER

The register is usually a static RAM or SRAM in the computer's processor that holds the data word by 64 or 128 bits. 
In addition, a status word register is used for decision making and an accumulator is used to stored numbers.

CISC's typically have many registers for receiving main memory, whereas RISC's have few in comparison.

LEVEL 1

CACHE MEMORY

Small, fast storage memory used for improving average access time and referred as a high speed memory that rapidly 
increases processing speed by making current programs and data available to the CPU.

LEVEL 2

MAIN MEMORY

Refers to the physical memory, one central storage unit in a computer system. The main memory is relatively a large 
and fast memory used to store programs and data during computer operation.

The main memory in a general purpose computer comprises a RAM integrated circuit.

AUXILIARY MEMORY

Is the lowest cost, highest capacity and slowest access storage. Auxiliary memory is used to store programs and data 
that are stored for long periods of time or are not in use right away.

LEVEL 3

MAGNETIC DISK

• A type of secondary memory that is a flat disc covered with a magnetic coating to hold information. It is used to 
store various program and filesMagnetic disks are usually less expensive than RAM and can store large amount of data 
but the access rate is slower compare to main memory because of secondary memory.

OPTICAL DISK

An information storage devices in a shape of a round plate that can be rotated to give access to all parts of the surface. 
Usually stores information in the form of physical variations on its surface that can be read with the aid of a beam of light.

LEVEL 4

MAGNETIC TAPE

Is a magnetic recording medium made a thin magnetizable coating on a long narrow strip of plastic film. Bits are 
recorded as magnetic spots on the tape along several tracks. Magnetic tapes can be stopped, started to move forward or 
reverse. Read/write heads are mounted in each track so that data can be recorded and read as a sequence of characters.

CHARACTERISTICS OF MEMORY HIERARCHY

PERFORMANCE

Initially, computer system were designed without a memory hierarchy. The speed gap between that main memory and CPU 
registers grew due to the large differential in access time, resulting in a lower system performance. As a result, 
enhancement was required. Because of the system's increased performance, this was enhanced in the memory hierarchy model.

ABILITY

The total quantity of data he memory hierarchy can store is its capacity because its capacity grows as we move from top to bottom.

COST PER BIT

When we move from the bottom to the top memory hierarchy, the cost of each bit increases, implying that internal memory 
is more expensive than external memory.

ACCESS TIME

In the memory hierarchy, the access time is the time delay between data availability and request to read or write 
because the access time increases we move from the top to the bottom of the memory hierarchy

ABILITY

The total quantity of data he memory hierarchy can store is its capacity because its capacity grows as we move from top to bottom.

COST PER BIT

When we move from the bottom to the top memory hierarchy, the cost of each bit increases, implying that internal memory 
is more expensive than external memory.

ACCESS TIME

• In the memory hierarchy, the access time is the time delay between data availability and request to read or write 
because the access time increases we move from the top to the bottom of the memory hierarchy."""

info7 = Label(tpc7, text=detail7, font=("Arial", 25), fg="BLACK", justify="left", anchor="n", wraplength=1500)
info7.place(x=50, y=100)

tpc7.create_window(800, 2200, window=info7)

out7 = Button(tpc7, text="🏠", font=(15), command=back_t2)
out7.config(height=2, width=5)
out7.place(x=0, y=0)

canvas10 = Canvas(tpc7, borderwidth=0, background="#ffffff")
scrollbar10 = Scrollbar(tpc7, orient="vertical", command=canvas10.yview)
scrollable_frame10 = Frame(canvas10)

tpc7.bind_all(
    "<Configure>",
    lambda e: tpc7.configure(
        scrollregion=tpc7.bbox("all")
    )
)
tpc7.bind_all("<MouseWheel>", on_mousewheel)
scrollable_frame10.bind_all()

canvas10.bind_all("<MouseWheel>", on_mousewheel)
#

chap2_top3 = Button(topic_con_btns2, text="TOPIC 8", font=("Fixedsys", 30), fg="BLACK", bg="#EECFA1", command=t8)
chap2_top3.place(x=150, y=350)

tpc8 = Canvas(root, height=1080, width=1980, scrollregion=(0, 0, 10000, 10000),)

detail8 = """"
D I R EC T  M E M O R Y  A C C E S S
\n
INTRODUCTION

• A direct memory access (DMA) controller is a device within the system that can facilitate data transfer between 
input/output devices within the system and the main memory without the CPU's intervention. This is done by the operating
system, which programs the DMA controller by telling where the data lives on the memory, how much to copy, and which 
device it should send. As a result, it completely bypasses the CPU and, in turn, lessens the load on the CPU.

After data transfer between the I/O devices and the memory, the DMA sends an alert to the CPU that tells it that the 
transfer is done and the CPU can now use the data as required.

TYPES

BURST MODE

In this mode, the DMA controller first takes control of the system bus to transfer the entire data block in one piece, 
then returns the control of the bus to the system.

CYCLE-STEALING ODE

In this mode, the DMA controller again takes control of the system bus but transfers data in one-byte increments. 
After the first piece of data has been transferred, it gives back control of the bus. This loop keeps repeating until 
the entire block has been transferred. This is especially beneficial for real-time data monitoring systems.

TRANSPARENT MODE

In this mode, the DMA controller only initiates the data transfer when the system bus is free, i.e., the CPU is not 
using it. This allows the CPU to work uninterrupted and only to transfer data when it is free. This makes the system's 
performance much faster, but the data transfer time increases inversely.

EXPLANATION

1. The CPU programs the DMA controller by settings its registers. Simultaneously, the CPU tells the disk controller to 
read the data from the drive and store it in the internal buffer. It does this because DMA can only work with data from the buffer.

2. Next, the DMA controller's control register will request the disk controller to transfer data to memory.

3. Afterward, the disk controller will transfer the data to the memory

4. After the data transfer, the disk controller will send an acknowledgment to the DMA controller and decrease the (byte)
count in its respective register.

5. If the byte count is not equal to zero, steps 2-4 will be repeated.

6. If the byte count is zero, an interrupt will be sent to the CPU that informs it that the transfer is done.

CONCLUSION

In conclusion, the DMA controller reduces CPU overhead and creates a faster data transfer process, which is 

particularly beneficial for a large data transfer or time-sensitive operation. Due to these reasons, the DMA 

controller is a commonly used hardware device in I/O devices for efficient data transfer."""

info8 = Label(tpc8, text=detail8, font=("Times", 25), fg="BLACK", justify="left", anchor="n", wraplength=1500)
info8.place(x=50, y=100)

tpc8.create_window(800, 1200, window=info8)

out8 = Button(tpc8, text="🏠", font=(15), command=back_t2)
out8.config(height=2, width=5)
out8.place(x=0, y=0)

canvas11 = Canvas(tpc8, borderwidth=0, background="#ffffff")
scrollbar11 = Scrollbar(tpc8, orient="vertical", command=canvas11.yview)
scrollable_frame11 = Frame(canvas11)

tpc8.bind_all(
    "<Configure>",
    lambda e: tpc8.configure(
        scrollregion=tpc8.bbox("all")
    )
)
tpc8.bind_all("<MouseWheel>", on_mousewheel)
scrollable_frame11.bind_all()

canvas11.bind_all("<MouseWheel>", on_mousewheel)

#

chap2_top4 = Button(topic_con_btns2, text="TOPIC 9", font=("Fixedsys", 30), fg="BLACK", bg="#EECFA1", command=t9)
chap2_top4.place(x=640, y=350)

tpc9 = Canvas(root, height=1080, width=1980, scrollregion=(0, 0, 10000, 10000),)

detail9 = """"
P R O C E S S O R  D E S I G N
\n
Processor design is a complex process that requires knowledge of hardware, software and system design.Here we discuss 
the different types of processor available on the market and how each is used in various applications. 
We will also take
a look at some common processor architectures and how they are implemented in FPGA devices as well as 
exploring the benefits of using microcontrollers in embedded systems.

-What is Processor Design?

Processor design is the process of designing and engineering processors. It is a subfield of computer engineering and 
electronics engineering that deals with creating a processor, a key component of computer hardware.

The processor is responsible for executing instructions, and it typically contains a control unit and an arithmetic logic unit. 
A processor is a central processing unit (CPU) that performs all the instructions that make up a computer program. 
It is like the brains of a computer, handling all the calculations and decisions that keep things running smoothly.

-What does it involve?

The goal of processor design is to create a chip that can handle all the necessary tasks quickly and efficiently. 
This involves careful planning and a deep understanding of how modern processors work.

The first step is to select an instruction set, which is a collection of basic operations that the processor can perform.
The second step is to design the logic circuits that will implement those instructions. Logic circuits are 
made up of transistors, 
which are switches that can be turned on or off.
Finally, the last step in processor design is to layout the physical circuitry, which is the process of 
arranging all the 
transistors on a chip so that they can be connected together.
Once the design is complete, it must be converted into a physical form (fabricated into a real physical chip) using 
lithography and other fabrication techniques. Only then can it be installed in a computer and put to work.

- Modern processors and their challenges.

With the ever-increasing demands placed on computers, processor design is an ongoing challenge that requires 
constant innovation.

To design an effective processor, engineers must consider factors such as clock speed, consumption of power and heat dissipation.

In recent years, design in this area has been driven by the need for ever higher levels of performance. As a result, 
modern processors have become increasingly complex, with multiple cores and on-chip cache memories.

Despite the challenges, processor design remains an essential part of creating computers that are fast, 
energy-efficient, and reliable.

- Why is Processor Design Important?

Processor design is important because it determines the performance of a computer. The faster a processor can execute 
instructions, the faster the overall performance of the computer will be.

It also affects how much power is consumed and therefore cost. A more complex processor will consume more power and be 
more expensive to run than a simpler one.

As a result, processor designers must carefully balance the need for speed and performance with the other 
constraints such as efficiency.

In addition, it is becoming increasingly important as the computer becomes more integrated into our lives. We rely on it 
for everything from entertainment to communication to work, and we expect it to be always available and always fast.

This places even more demands on processor designers to create chips with power, speed and efficiency.

- Different Types of Processor

There are a range of different types of processor available on the market and each has its own advantages and disadvantages. 
The most common types of processors are x86, ARM, and FPGA.

X86 processors are used in desktop computers and laptops. They are known for their high performance and power efficiency. 
AMD’s G-Series processors are some of the most popular x86 processors available.

Intel Atom processors are another type of x86 processor. They are designed for low power consumption and are 
often used in netbooks and tablets.

Vortex86SX/DX/DX processors are a type of x86 processor that is designed for use in embedded systems. 
They offer a high level of integration and power efficiency.

ARM processors are used in a wide range of devices, including smartphones, tablets, and embedded systems. They are known 
for their low consumption of power and high performance. Some of the most popular ARM processors include the 
Freescale MX51 and the Cortex-M series from ARM.

FPGA integration
Many processors can be integrated into FPGA devices. FPGAs are programmable logic devices that offer a 
high level of flexibility and performance.

Spartan-six and Spartan-three processors from Xilinx are some of the most popular FPGA processors. Altera’s MAX series is 
another popular choice for FPGA integration.

Microcontrollers
Microcontrollers are a type of processor that is designed for use in embedded systems. They offer a high 
level of integration and power efficiency.

Microchip’s PIC microcontrollers are some of the most popular microcontrollers on the market. They offer a 
wide range of features and are suitable for a variety of applications.

- How Processors are Used

processor security cameraProcessors are used in a wide range of devices, from PCs to smartphones. They perform a variety 
of tasks, such as executing applications, processing data and controlling peripherals.

The central processing unit, or CPU, is the brains of a computer system. It interprets and carries out basic instructions 
that operate the machine. However, not all CPUs are created equal. The needs of different markets 
dictate the design of different types of CPUs.

For example, a CPU design for use in a desktop computer will be very different from a CPU design for use in a smartphone. 
A desktop computer requires more processing power than a smartphone, so its CPU is designed accordingly, 
as CPU speed and power is most important. 
However, a laptop requires more battery life than a desktop computer, so laptop CPUs are designed for energy efficiency.

Each type of market has its own unique CPU requirements, and the best way to meet those requirements is to 
design a specific type of CPU for that market.

In general, processors can be classified into two main categories: general-purpose processors and microcontrollers.

- General purpose processors
General-purpose processors are designed for use in a wide range of devices, from desktop computers to servers. 
They offer high performance and are suitable for applications that require a lot of processing power and speed.

This includes desktop, laptop, and server computers commonly used in businesses and homes. A growing percentage of these 
processors are for mobile implementations such as netbooks and laptops. As mobile devices become more and more popular, 
it’s likely that the percentage of CPU sales for mobile devices will continue to grow.

Central processing units (CPUs) are vital components of any computing system, and as our reliance on the computer 
continues to grow, so too will the demand for modern CPUs.

The design of CPUs has had to evolve to meet the demands of the ever-changing computer landscape. In the early days of 
computing, a simple CPU was designed to execute a single task, such as playing a game or running a word processor. 
However, as the range and complexity of computer applications have increased, so too has the need for 
modern CPUs that are able to execute multiple tasks simultaneously.

This has led to the development of CPU designs that are among the most advanced technologically, but which also come 
with some new challenges, such as managing high costs and power efficiency. Despite these challenges, CPUs continue to 
play an essential role in meeting the needs of today’s computer users.

Microcontrollers for embedded systems

Microcontrollers are designed for use in embedded systems. They offer a high level of integration and are often 
used in applications where power efficiency is important.

Embedded systems are electronic devices that use processors to control their operation. 
They are found in a wide range of devices, including automobiles, appliances, and industrial equipment.

Microcontrollers are often used in embedded systems due to their high level of integration and power efficiency. 
FPGA-based processors can also be used in embedded systems, but they typically offer a higher level of performance.

A microcontroller is a small, self-contained computer that is typically used in embedded systems. Unlike a general-purpose computer, 
which can be programmed to execute a variety of tasks, a microcontroller is designed to perform a specific set of tasks. This includes 
controlling and monitoring peripherals, such as sensors and actuators.

Microcontrollers often offer a high level of integration, meaning that they include a wide range of features on a single chip. 
This includes a central processing unit (CPU), memory, input/output (I/O) ports, and sometimes even analogue-to-digital 
converters (ADCs) and digital-to-analogue converters (DACs).

Due to their compact size and efficient power management, microcontrollers are often used in battery-powered 
devices, such as mobile phones and wearable electronics.

As the demands of the computer landscape continue to evolve, so too will the design of CPUs. While general-purpose processors and 
microcontrollers each have their own advantages and disadvantages, both types of CPUs will continue to play an 
essential role in meeting the needs of modern computer users.

The benefits of using microcontrollers
Microcontrollers offer a number of advantages over other types of processors. They are less expensive and consume less power. 
They also offer a high level of integration, which reduces the size and complexity of the system.

Microcontrollers are a good choice for applications that require a high level of control and power efficiency. 
They are also suitable for applications that have limited space or resources."""

info9 = Label(tpc9, text=detail9, font=("Arial", 25), fg="BLACK", justify="left", anchor="n", wraplength=15000)
info9.place(x=50, y=100)

tpc9.create_window(1000, 3200, window=info9)

out9 = Button(tpc9, text="🏠", font=(15), command=back_t2)
out9.config(height=2, width=5)
out9.place(x=0, y=0)

canvas12 = Canvas(tpc9, borderwidth=0, background="#ffffff")
scrollbar12 = Scrollbar(tpc9, orient="vertical", command=canvas12.yview)
scrollable_frame12 = Frame(canvas12)

tpc9.bind_all(
    "<Configure>",
    lambda e: tpc9.configure(
        scrollregion=tpc9.bbox("all")
    )
)
tpc9.bind_all("<MouseWheel>", on_mousewheel)
scrollable_frame12.bind_all()

canvas12.bind_all("<MouseWheel>", on_mousewheel)
#

chap2_top5 = Button(topic_con_btns2, text="TOPIC 10", font=("Fixedsys", 30), fg="BLACK", bg="#EECFA1", command=t10)
chap2_top5.place(x=1180, y=350)

tpc10 = Canvas(root, height=1080, width=1980, scrollregion=(0, 0, 10000, 10000),)

detail10 = """"
S U P E R S C A L A R  P R O C E S S O R
\n
A superscalar processor is a CPU that implements a form of parallelism called instruction-level parallelism within a 
single processor.[1] In contrast to a scalar processor, which can execute at most one single instruction per clock cycle, 
a superscalar processor can execute more than one instruction during a clock cycle by simultaneously dispatching multiple 
instructions to different execution units on the processor. It therefore allows more throughput (the number of instructions 
that can be executed in a unit of time) than would otherwise be possible at a given clock rate. Each execution unit is not 
a separate processor (or a core if the processor is a multi-core processor), but an execution resource within a 
single CPU such as an arithmetic logic unit.

While a superscalar CPU is typically also pipelined, superscalar and pipelining execution are considered different performance 
enhancement techniques. The former executes multiple instructions in parallel by using multiple execution units, whereas the 
latter executes multiple instructions in the same execution unit in parallel by dividing the execution unit into different phases.

The superscalar technique is traditionally associated with several identifying characteristics (within a given CPU):

Instructions are issued from a sequential instruction stream
The CPU dynamically checks for data dependencies between instructions at run time (versus software checking at compile time)
The CPU can execute multiple instructions per clock cycle


P A R A L L E L  P R O C E S S I N G


Parallel processing is a method in computing of running two or more processors (CPUs) to handle separate parts of an overall task. 
Breaking up different parts of a task among multiple processors will help reduce the amount of time to run a program. 
Any system that has more than one CPU can perform parallel processing, as well as multi-core processors which are 
commonly found on computers today.

Multi-core processors are IC chips that contain two or more processors for better performance, reduced power consumption 
and more efficient processing of multiple tasks. These multi-core set-ups are similar to having multiple, separate 
processors installed in the same computer. Most computers may have anywhere from two-four cores; increasing up to 12 cores.

Parallel processing is commonly used to perform complex tasks and computations. Data scientists will commonly make use of 
parallel processing for compute and data-intensive tasks.

- How parallel processing works

Typically a computer scientist will divide a complex task into multiple parts with a software tool and assign each part 
to a processor, then each processor will solve its part, and the data is reassembled by a software tool to read the 
solution or execute the task.

Typically each processor will operate normally and will perform operations in parallel as instructed, pulling data from the 
computer’s memory. Processors will also rely on software to communicate with each other so they can stay in sync concerning 
changes in data values. Assuming all the processors remain in sync with one another, at the end of a task, software 
will fit all the data pieces together.

Computers without multiple processors can still be used in parallel processing if they are networked together to form a cluster.

Types of parallel processing
There are multiple types of parallel processing, two of the most commonly used types include SIMD and MIMD. SIMD, or single 
instruction multiple data, is a form of parallel processing in which a computer will have two or more processors follow 
the same instruction set while each processor handles different data. SIMD is typically used to analyze large data 
sets that are based on the same specified benchmarks.

MIMD, or multiple instruction multiple data, is another common form of parallel processing which each computer has two or 
more of its own processors and will get data from separate data streams.

Another, less used, type of parallel processing includes MISD, or multiple instruction single data, where each processor 
will use a different algorithm with the same input data.

Difference between Serial and parallel processing
Where parallel processing can complete multiple tasks using two or more processors, serial processing 
(also called sequential processing) will only complete one task at a time using one processor. If a computer needs to 
complete multiple assigned tasks, then it will complete one task at a time. Likewise, if a computer using serial 
processing needs to complete a complex task, then it will take longer compared to a parallel processor.

- History of parallel processing
In the earliest computers, only one program ran at a time. A computation-intensive program which would take one hour to 
both run as well as and tape copying program that took one hour to run would take a total of two hours to run. 
An early form of parallel processing allowed the interleaved execution of both programs together. 
The computer would start an I/O operation, and while it was waiting for the operation to complete, it would execute the 
processor-intensive program. The total execution time for the two jobs would be a little over one hour.

The next improvement was multiprogramming. In a multiprogramming system, multiple programs submitted by users were each 
allowed to use the processor for a short time. To users, it appeared that all of the programs were executing at the same time. 
Problems of resource contention first arose in these systems. Explicit requests for resources led to the problem of the deadlock, 
where simultaneous requests for resources would effectively prevent program from accessing the resource. 
Competition for resources on machines with no tie-breaking instructions lead to the critical section routine.

Vector processing was another attempt to increase performance by doing more than one thing at a time. In this case, 
capabilities were added to machines to allow a single instruction to add (or subtract, or multiply, or otherwise manipulate) 
two arrays of numbers. This was valuable in certain engineering applications where data naturally occurred in the form of 
vectors or matrices. In applications with less well-formed data, vector processing was not so valuable.

The next step in parallel processing was the introduction of multiprocessing. In these systems, two or more processors 
shared the work to be done. The earliest versions had a master/slave configuration. One processor (the master) was 
programmed to be responsible for all of the work in the system; the other (the slave) performed only those tasks it was 
assigned by the master. This arrangement was necessary because it was not then understood how to program the machines so 
they could cooperate in managing the resources of the system.

SMP and MMP
Solving these problems led to the symmetric multiprocessing system (SMP). In an SMP system, each processor is equally 
capable and responsible for managing the flow of work through the system. Initially, the goal was to make SMP systems 
appear to programmers to be exactly the same as a single processor, multiprogramming systems. However, engineers found 
that system performance could be increased by someplace in the range of 10-20% by executing some instructions out of 
order and requiring programmers to deal with the increased complexity (the problem can become visible only when two or 
more programs simultaneously read and write the same operands; thus the burden of dealing with the increased complexity 
falls on only a very few programmers and then only in very specialized circumstances). The question of how SMP machines 
should behave on shared data is not yet resolved.

As the number of processors in SMP systems increases, the time it takes for data to propagate from one part of the 
system to all other parts also increases. When the number of processors is somewhere in the range of several dozen, 
the performance benefit of adding more processors to the system is too small to justify the additional expense. 
To get around the problem of long propagation times, a message passing system mentioned earlier was created. In these 
systems, programs that share data send messages to each other to announce that particular operands have been assigned a 
new value. Instead of a broadcast of an operand's new value to all parts of a system, the new value is communicated only 
to those programs that need to know the new value. Instead of shared memory, there is a network to support the transfer 
of messages between programs. This simplification allows hundreds, even thousands, of processors to work together 
efficiently in one system. Hence such systems have been given the name of massively parallel processing (MPP) systems.

The most successful MPP applications have been for problems that can be broken down into many separate, independent 
operations on vast quantities of data. In data mining, there is a need to perform multiple searches of a static database. 
In artificial intelligence, there is a need to analyze multiple alternatives, as in a chess game. Often MPP systems are 
structured as clusters of processors. Within each cluster the processors interact as in an SMP system. It is only between 
the clusters that messages are passed. Because operands may be addressed either via messages or via memory addresses, 
some MPP systems are called NUMA machines, for Non-Uniform Memory Addressing.

SMP machines are relatively simple to program; MPP machines are not. SMP machines do well on all types of problems, 
providing the amount of data involved is not too large. For certain problems, such as data mining of vast databases, 
only MPP systems will serve."""

info10 = Label(tpc10, text=detail10, font=("Arial", 25), fg="BLACK", justify="left", anchor="n", wraplength=1500)
info10.place(x=50, y=100)

tpc10.create_window(800, 3700, window=info10)

out10 = Button(tpc10, text="🏠", font=(15), command=back_t2)
out10.config(height=2, width=5)
out10.place(x=0, y=0)

canvas13 = Canvas(tpc10, borderwidth=0, background="#ffffff")
scrollbar13 = Scrollbar(tpc10, orient="vertical", command=canvas13.yview)
scrollable_frame13 = Frame(canvas13)

tpc10.bind_all(
    "<Configure>",
    lambda e: tpc10.configure(
        scrollregion=tpc10.bbox("all")
    )
)
tpc10.bind_all("<MouseWheel>", on_mousewheel)
scrollable_frame13.bind_all()

canvas13.bind_all("<MouseWheel>", on_mousewheel)

# CHAPTER 2 QUIZ BTNS

######### C2 B1

chap2_quiz1 = Button(topic_con_btns2, text="QUIZ 3", font=("Fixedsys", 30), fg="BLACK", bg="#FFE4B5", command=into_3)
chap2_quiz1.place(x=670, y=170)

quiz_start3 = Frame(root)
quiz_start3.config(bg="GRAY")
quiz_start3.config(height=864, width=1540)

starting3 = Label(quiz_start3, image=now, bd=0)
starting3.pack()

star3 = ImageTk.PhotoImage(file="C:/Users/kenneth/Pictures/Saved Pictures/STARR.jpg")
start_quiz3 = Label(quiz_start3, text="Q U I Z  T I M E !", font=("Fixedsys", 60), bg="BLUE", fg="#0000FF", compound="center", image=star3, bd=0)
start_quiz3.place(x=380, y=100)

to_start3 = Button(quiz_start3, text="START", command=no_3, bg="#98F5FF")
to_start3.place(x=650, y=630)
to_start3.config(height=5, width=30)

#

q3 = Frame(root)
q3.config(bg="GRAY")
q3.config(height=864, width=1540)

hys4 = Label(q3, image=ok, bd=0)
hys4.pack()


question3 = Label(q3)
question3.place(x=100, y=100)
question3.config(font=("Arial", 30))

answer3 = Entry(q3)
answer3.place(x=300, y=300)
answer3.config(width=50)

done3 = Button(q3, text="NEXT QUESTION")
done3.place(x=400, y=500)
done3.config(height=10, width=20)
done3.config(font=("Fixedsys", 10), bg="#FFFACD", fg="#8B8386")

######### C2 B2

chap2_quiz2 = Button(topic_con_btns2, text="QUIZ 4", font=("Fixedsys", 30), fg="BLACK", bg="#8B0000", command=into_4)
chap2_quiz2.place(x=670, y=540)

quiz_start4 = Frame(root)
quiz_start4.config(bg="GRAY")
quiz_start4.config(height=864, width=1540)

starting4 = Label(quiz_start4, image=now, bd=0)
starting4.pack()

star4 = ImageTk.PhotoImage(file="C:/Users/kenneth/Pictures/Saved Pictures/STARR.jpg")
start_quiz4 = Label(quiz_start4, text="Q U I Z  T I M E !", font=("Fixedsys", 60), bg="BLUE", fg="#0000FF", compound="center", image=star4, bd=0)
start_quiz4.place(x=380, y=100)

to_start4 = Button(quiz_start4, text="START", command=no_4, bg="#98F5FF")
to_start4.place(x=650, y=630)
to_start4.config(height=5, width=30)

#

q4 = Frame(root)
q4.config(bg="GRAY")
q4.config(height=864, width=1540)

hys5 = Label(q4, image=ok, bd=0)
hys5.pack()


question4 = Label(q4)
question4.place(x=100, y=100)
question4.config(font=("Arial", 30))

answer4 = Entry(q4)
answer4.place(x=300, y=300)
answer4.config(width=50)

done4 = Button(q4, text="NEXT QUESTION")
done4.place(x=400, y=500)
done4.config(height=10, width=20)
done4.config(font=("Fixedsys", 10), bg="#FFFACD", fg="#8B8386")

######### C2 F2

chap2_quiz_final2 = Button(topic_con_btns2, text="FINAL QUIZ 2", font=("Fixedsys", 30), fg="BLACK", bg="#212121",
                           command=into_final2)
chap2_quiz_final2.place(x=610, y=680)
# chap2_quiz_final2.config(height=0, width=10)

quiz_start_final2 = Frame(root)
quiz_start_final2.config(bg="GRAY")
quiz_start_final2.config(height=864, width=1540)

sfq2 = Label(quiz_start_final2, image=sref, bd=0)
sfq2.pack()


lb2 = Label(quiz_start_final2, text="F I N A L  Q U I Z", font=("Fixedsys", 60), fg="GREEN")
lb2.place(x=400, y=100)


to_start_final2 = Button(quiz_start_final2, text="START", font=("Fixedsys", 10),bg="#48D1CC", fg="#FAF0E6", command=final_no_2)
to_start_final2.place(x=700, y=500)
to_start_final2.config(height=5, width=15)

#

q_final2 = Frame(root)
q_final2.config(bg="GRAY")
q_final2.config(height=864, width=1540)

hys6 = Label(q_final2, image=ok, bd=0)
hys6.pack()


final_question2 = Label(q_final2)
final_question2.place(x=100, y=100)
final_question2.config(font=("Arial", 30))

final_answer2 = Entry(q_final2)
final_answer2.place(x=300, y=300)
final_answer2.config(width=50)

final_done2 = Button(q_final2, text="NEXT QUESTION")
final_done2.place(x=400, y=500)
final_done2.config(height=10, width=20)
final_done2.config(font=("Fixedsys", 10), bg="#FFFACD", fg="#8B8386")

# CHAPTER 3 TOPIC

topic_con_btns3 = Frame(root, height=1080, width=1980)

third = ImageTk.PhotoImage(file="C:/Users/kenneth/Pictures/Saved Pictures/THIRD.jpg")
t1 = Label(topic_con_btns3, image=third, bd=0)
t1.place(x=0, y=0)

back6 = Button(topic_con_btns3, text="🏠", font=(15), bg="#36648B", command=back_top3)
back6.config(height=2, width=5)
back6.pack(anchor="nw")

chap3_top1 = Button(topic_con_btns3, text="TOPIC 11", font=("Fixedsys", 30), fg="BLACK", bg="#98F5FF", command=t11)
chap3_top1.place(x=630, y=350)

tpc11 = Canvas(root, height=1080, width=1980, scrollregion=(0, 0, 10000, 10000),)

detail11 = """"
A binary number system is one of the four types of number system. In computer applications, 
where binary numbers are represented by only two symbols or digits, i.e. 0 (zero) and 1(one). 
The binary numbers here are expressed in the base-2 numeral system. For example, (101)2 is a binary number. 
Each digit in this system is said to be a bit. Learn about the number system here.
\n
Table of Contents:
- Definition
- Table
- How to Calculate Binary Numbers
- Positions
- Binary Arithmetic Operations
- Binary Addition
- Binary Subtraction
- Binary Multiplication
- Binary Division

Number System is a way to represent numbers in computer architecture. There are four different types of the number system, 
such as:

Binary number system (base 2)
Octal number system (base 8) 
Decimal number system(base 10)
Hexadecimal number system (base 16).

Let us discuss what is a binary number system, conversion from one system to other systems,  
table, positions, binary operations such as addition, subtraction, multiplication, and division, uses and solved 
examples in detail.


What is a Binary Number System?

Binary Number System: According to digital electronics and mathematics, a binary number is defined as a number that 
is expressed in the binary system or base 2 numeral system. It describes numeric values by two separate symbols; 1 
(one) and 0 (zero). The base-2 system is the positional notation with 2 as a radix.

The binary system is applied internally by almost all latest computers and computer-based devices because of its 
direct implementation in electronic circuits using logic gates. Every digit is referred to as a bit. 

Example: Convert 4 in binary.

Solution: 

4 in binary is (100)2.

Here, 4 is represented in the decimal number system, where we can represent the number using the digits from 0-9. 
However, in a binary number system, we use only two digits, such as 0 and 1.

Now, let’s discuss how to convert 4 in binary number system. The following steps help to convert 4 in binary.

Step 1: First, divide the number 4 by 2. Use the integer quotient obtained in this step as the dividend for 
the next step. Continue this step, until the quotient becomes 0.

Dividend

Remainder

4/2 = 2

0

2/2 = 1

0

1/2 = 0

1

Step 2: Now, write the remainder in reverse chronological order. (i.e from bottom to top).

Here, the Least Significant Bit (LSB) is 0 and the Most Significant Bit (MSB) is 1.

Hence, the decimal number 4 in binary is 1002

So, if we want to find how many bits does 4 in binary have? we have to count the number of zeros and ones. 

So, 4 in binary is 1002. Here, there are 2 zeroes and 1 one. Hence, we have 3 bits.

Therefore, the number of bits does 4 in binary have is 3.

What is Bit in Binary Number?
A single binary digit is called a “Bit”. A binary number consists of several bits. Examples are:

10101 is a five-bit binary number
101 is a three-bit binary number
100001 is a six-bit binary number
Facts to Remember:
Binary numbers are made up of only 0’s and 1’s.
A binary number is represented with a base-2
A bit is a single binary digit.

Binary Numbers Table
Some of the binary notations of lists of decimal numbers from 1 to 30,  are mentioned in the below list.

Number	Binary Number	Number	Binary Number	Number	Binary Number
1	       1	11	     1011	  21	10101
2	      10	12	     1100	  22	10110
3	      11	13	     1101	  23	10111
4	     100	14	     1110	  24	11000
5	     101	15	     1111	  25	11001
6	     110	16	     10000	  26	11010
7	     111	17	     10001	  27	11011
8	     1000	18	     10010	  28	11100
9	     1001	19	     10011	  29	11101
10	     1010	20	     10100	  30	11110

How to Calculate Binary Numbers
For example, the number to be operated is 1235.

Thousands	Hundreds	Tens	Ones
1	           2	      3	      5
This indicates,

1235 = 1 × 1000 + 2 × 100 + 3 × 10 + 5 × 1

Given,

1000	= 103 = 10 × 10 × 10
100	= 102 = 10 × 10
10	= 101 = 10
1	= 100 (any value to the exponent zero is one)
The above table can be described as,

Thousands	Hundreds	Tens	Ones
103	102	101	100
1	2	3	5
Hence,

1235 = 1 × 1000 + 2 × 100 + 3 × 10 + 5 × 1

= 1 × 103 + 2 × 102 + 3 × 101 + 5 × 100

The decimal number system operates in base 10, wherein the digits 0-9 represent numbers. 
In binary system operates in base 2 and the digits 0-1 represent numbers, and the base is known as radix. 
Put differently, and the above table can also be shown in the following manner.

Thousands	Hundreds	Tens	Ones
Decimal	103	102	101	100
Binary	23	22	21	20
We place the digits in columns 100, 101 and so on in base 10. When there is a need to put a value higher 
than 9 in the form of 10(n+1) for instance, to add 10 to column 100, you need to add 1 to the column 101.

We place the digits in columns 20, 21 and so on in base 2. To place a value that is higher than 1 in 2n, 
you need to add 2(n+1). For instance, to add 3 to column 20, you need to add 1 to column 21.


Position in Binary Number System
In the Binary system, we have ones, twos, fours etc…

For example 1011.110

It is shown like this:

1 × 8 + 0 × 4 + 1 × 2 + 1 + 1 × ½ + 1 × ¼ + 0 × 1⁄8

= 11.75 in Decimal

To show the values greater than or less than one, the numbers can be placed to the left or right of the point.

For 10.1, 10 is a whole number on the left side of the decimal, and as we move more left, the number place gets bigger (Twice).

The first digit on the right is always Halves ½ and as we move more right, the number gets smaller (half as big).

In the example given above:

“10” shows ‘2’ in decimal.
“.1” shows ‘half’.
So, “10.1” in binary is 2.5 in decimal.

Binary Arithmetic Operations
Like we perform the arithmetic operations in numerals, in the same way, we can perform addition, subtraction, 
multiplication and division operations on Binary numbers. Let us learn them one by one.

Binary Addition
Adding two binary numbers will give us a binary number itself. It is the simplest method. Addition of two 
single-digit binary number is given in the table below.

Binary Numbers	Addition
0	0	0
0	1	1
1	0	1
1	1	0; Carry →1
Let us take an example of two binary numbers and add them.

For example: Add 11012 and 10012.
Solution: Binary Addition

single-digit binary number is given in the table below.

Binary Numbers	Subtraction
0	0	0
0	1	1; Borrow 1
1	0	1
1	1	0
Let us take an example of two binary numbers and subtract them.

Example: Subtract 11012, and 10102.

Solution: 11012 – 10102 = 00112

Binary Multiplication
The multiplication process is the same for the binary numbers as it is for numerals. Let us understand it with example.

Example: Multiply 11012 and 10102.

Solution: Binary Multiplication

Binary Division
The binary division is similar to the decimal number division method. We will learn with an example here.

Example: Divide 10102 by 102

Solution: Binary Division

Uses of Binary Number System
Binary numbers are commonly used in computer applications. All the coding and languages in computers such as 
C, C++, Java, etc. use binary digits 0 and 1 to write a program or encode any digital data. The computer understands 
only the coded language. Therefore these 2-digit number system is used to represent a set of data or information in 
discrete bits of information.
"""

info11 = Label(tpc11, text=detail11, font=("Arial", 25), fg="BLACK", justify="left", anchor="n", wraplength=1500)
info11.place(x=50, y=100)

tpc11.create_window(1000, 5200, window=info11)

out11 = Button(tpc11, text="🏠", font=(15), command=back_t3)
out11.config(height=2, width=5)
out11.place(x=0, y=0)

canvas14 = Canvas(tpc11, borderwidth=0, background="#ffffff")
scrollbar14 = Scrollbar(tpc11, orient="vertical", command=canvas14.yview)
scrollable_frame14 = Frame(canvas14)

tpc11.bind_all(
    "<Configure>",
    lambda e: tpc11.configure(
        scrollregion=tpc11.bbox("all")
    )
)
tpc11.bind_all("<MouseWheel>", on_mousewheel)
scrollable_frame14.bind_all()

canvas14.bind_all("<MouseWheel>", on_mousewheel)

#

######################## CHAPTER3 QUIZ BTNS

############## C3 B1

chap3_quiz1 = Button(topic_con_btns3, text="QUIZ 5", font=("Fixedsys", 30), fg="BLACK", bg="#00BFFF", command=into_5)
chap3_quiz1.place(x=250, y=150)

quiz_start5 = Frame(root)
quiz_start5.config(bg="GRAY")
quiz_start5.config(height=864, width=1540)

starting5 = Label(quiz_start5, image=now, bd=0)
starting5.pack()

star5 = ImageTk.PhotoImage(file="C:/Users/kenneth/Pictures/Saved Pictures/STARR.jpg")
start_quiz5 = Label(quiz_start5, text="Q U I Z  T I M E !", font=("Fixedsys", 60), bg="BLUE", fg="#0000FF", compound="center", image=star5, bd=0)
start_quiz5.place(x=380, y=100)

to_start5 = Button(quiz_start5, text="START", command=no_5, bg="#98F5FF")
to_start5.place(x=650, y=630)
to_start5.config(height=5, width=30)

#

q5 = Frame(root)
q5.config(bg="GRAY")
q5.config(height=864, width=1540)

hys7 = Label(q5, image=ok, bd=0)
hys7.pack()


question5 = Label(q5)
question5.place(x=100, y=100)
question5.config(font=("Arial", 30))

answer5 = Entry(q5)
answer5.place(x=300, y=300)
answer5.config(width=50)

done5 = Button(q5, text="NEXT QUESTION")
done5.place(x=400, y=500)
done5.config(height=10, width=20)
done5.config(font=("Fixedsys", 10), bg="#FFFACD", fg="#8B8386")

########## C3 B2


chap3_quiz2 = Button(topic_con_btns3, text="QUIZ 6", font=("Fixedsys", 30), fg="BLACK", bg="#00BFFF", command=into_6)
chap3_quiz2.place(x=1150, y=150)

quiz_start6 = Frame(root)
quiz_start6.config(bg="GRAY")
quiz_start6.config(height=864, width=1540)


starting6 = Label(quiz_start6, image=now, bd=0)
starting6.pack()

star6 = ImageTk.PhotoImage(file="C:/Users/kenneth/Pictures/Saved Pictures/STARR.jpg")
start_quiz6 = Label(quiz_start6, text="Q U I Z  T I M E !", font=("Fixedsys", 60), bg="BLUE", fg="#0000FF", compound="center", image=star6, bd=0)
start_quiz6.place(x=380, y=100)

to_start6 = Button(quiz_start6, text="START", command=no_6, bg="#98F5FF")
to_start6.place(x=650, y=630)
to_start6.config(height=5, width=30)

#

q6 = Frame(root)
q6.config(bg="GRAY")
q6.config(height=864, width=1540)

hys8 = Label(q6, image=ok, bd=0)
hys8.pack()


question6 = Label(q6)
question6.place(x=100, y=100)
question6.config(font=("Arial", 30))

answer6 = Entry(q6)
answer6.place(x=300, y=300)
answer6.config(width=50)

done6 = Button(q6, text="NEXT QUESTION")
done6.place(x=400, y=500)
done6.config(height=10, width=20)
done6.config(font=("Fixedsys", 10), bg="#FFFACD", fg="#8B8386")

######## C3 F3

chap3_quiz_final3 = Button(topic_con_btns3, text="FINAL QUIZ 3", font=("Fixedsys", 30), fg="BLACK", bg="#00688B",
                           command=into_final3)
chap3_quiz_final3.place(x=600, y=700)

quiz_start_final3 = Frame(root)
quiz_start_final3.config(bg="GRAY")
quiz_start_final3.config(height=864, width=1540)

sfq3 = Label(quiz_start_final3, image=sref, bd=0)
sfq3.pack()



lb3 = Label(quiz_start_final3, text="F I N A L  Q U I Z", font=("Fixedsys", 60), fg="GREEN")
lb3.place(x=400, y=100)


to_start_final3 = Button(quiz_start_final3, text="START", font=("Fixedsys", 10),bg="#48D1CC", fg="#FAF0E6", command=final_no_3)
to_start_final3.place(x=700, y=500)
to_start_final3.config(height=5, width=15)

#

q_final3 = Frame(root)
q_final3.config(bg="GRAY")
q_final3.config(height=864, width=1540)

hys9 = Label(q_final3, image=ok, bd=0)
hys9.pack()


final_question3 = Label(q_final3)
final_question3.place(x=100, y=100)
final_question3.config(font=("Arial", 30))

final_answer3 = Entry(q_final3)
final_answer3.place(x=300, y=300)
final_answer3.config(width=50)

final_done3 = Button(q_final3, text="NEXT QUESTION")
final_done3.place(x=400, y=500)
final_done3.config(height=10, width=20)
final_done3.config(font=("Fixedsys", 10), bg="#FFFACD", fg="#8B8386")

# FINAL EXAM BUTTON

final_exam = Button(home_window, text="FINAL EXAM", font=("Fixedsys", 30), fg="DARK BLUE", bg="#8B1A1A", command=into_exam)
final_exam.place(x=650, y=700)

start_exam = Frame(root)
start_exam.config(bg="GRAY")
start_exam.config(height=864, width=1540)

last = ImageTk.PhotoImage(file="C:/Users/kenneth/Pictures/Saved Pictures/GREEN.jpg")
last1 = Label(start_exam, image=last, bd=0)
last1.place(x=0, y=0)

lb4 = Label(start_exam, text="F I N A L  E X A M", font=("Fixedsys", 60), fg="GREEN")
lb4.place(x=400, y=100)

to_start_exam = Button(start_exam, text="START", command=exam1)
to_start_exam.place(x=700, y=500)
to_start_exam.config(height=5, width=25)

#

q_exam = Frame(root)
q_exam.config(bg="GRAY")
q_exam.config(height=864, width=1540)

hys10 = Label(q_exam, image=ok, bd=0)
hys10.pack()


ques_exam = Label(q_exam)
ques_exam.place(x=100, y=100)
ques_exam.config(font=("Arial", 30))

ans_exam = Entry(q_exam)
ans_exam.place(x=300, y=300)
ans_exam.config(width=50)

done_exam = Button(q_exam, text="NEXT QUESTION")
done_exam.place(x=400, y=500)
done_exam.config(height=10, width=20)
done_exam.config(font=("Fixedsys", 10), bg="#FFFACD", fg="#8B8386")


######################

log_out = Button(home_window, text="LOG OUT", font=("Fixedsys", 10), bg="#FFE4C4", fg="BLACK", command=out)
log_out.place(x=1300, y=0)
log_out.config(height=5, width=30)

####################


####################

if __name__ == '__main__':
    frame.place(x=550, y=250)

root.mainloop()
