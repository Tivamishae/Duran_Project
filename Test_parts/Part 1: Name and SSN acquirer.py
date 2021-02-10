from tkinter import *


# Predetermined strings.
bidding_1 = ("Please write your social security number on the line: ")
bidding_2 = ("Please write your first name: ")
error_1 = ("Error! Only numbers allowed!")
error_2 = ("Error! Please write your social security number with 12 numbers organized as yyyymmddxxxx.")
error_3 = ("Error! Use only letters in your name.")
error_4 = ("Error! Invalid name.")
error_5 = ("Error! Please answer with either yes or no.")
input_name = ("")
input_str = ("")
statement_2 =("Everything seems to be working fine then, thank you for your contribution.")
statement_3 = ("Try again.")
question_1 = ("Is this correct? ")



# User interface elements.
UI = Tk()
UI.title('Social Security Number Registry')
UI.geometry("500x400+20+20")
lbl=Label(UI, text="Please follow the steps below.", fg='black', font=("Helvetica", 16))
lbl.place(x=150, y=10)
txtfld=Entry(UI, bd=2)
txtfld.place(x=150, y=70)
txtfld.bind('<KeyPress-a>', print("HI"))
UI.mainloop()


# Asks the user for his/her social security number and checks it's validity.
def social_security_number():
    global input_str
    input_str = input(bidding_1)

    if not re.match("^[0-9]*$", input_str):
        print(error_1)
        social_security_number()

    elif len(input_str) > 12:
        print(error_2)
        social_security_number()

    elif len(input_str) < 12:
        print(error_2)
        social_security_number()

    else:
        name()


# Asks the user for his/her name and checks it's validity.
def name():
    global input_name
    input_name = input(bidding_2)

    if not re.match("^[A-ö]*$", input_name):
        print(error_3)
        name()

    elif len(input_name) < 2:
        print(error_4)
        name()

    else:
        control()


# Asks the user if the information given is correct repeats the first function if it is wrong, otherwise it turns the program of.
def control():

    # Dependent variable: This variable depends on the variables "input_name" and "input_str" and therefore it has to stay inside this function.
    statement_1 = ("Your name is " + input_name + " and your social security number is " + input_str + ".")

    print(statement_1)
    input_yes_no = input(question_1)

    if input_yes_no == ("Yes"):
        print(statement_2)
        quit()

    elif input_yes_no == ("yes"):
        print(statement_2)
        quit()

    elif input_yes_no == ("No"):
        print(statement_3)
        social_security_number()

    elif input_yes_no == ("no"):
        print(statement_3)
        social_security_number()

    else:
        print(error_5)
        control()


# Runs the first function.

social_security_number()



