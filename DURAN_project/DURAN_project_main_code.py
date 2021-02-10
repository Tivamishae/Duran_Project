import tkinter as tk
import re
import sqlite3


# Connects to database
def everything():
    conn = sqlite3.connect('Members of DURAN.db')
    c = conn.cursor()

    # UI Setup
    global UI
    UI = tk.Tk()
    UI.geometry("700x500+200+150")
    UI.title("-Registrera dig som en medlem hos DURAN-")

    # Variables for storing name and social security number gathered from the user.
    input_name = tk.StringVar()
    input_social_numb = tk.StringVar()
    input_username = tk.StringVar()
    input_password = tk.StringVar()
    input_password_repeat = tk.StringVar()

    # UI elements 2.
    # - Name
    name_label = tk.Label(UI, text='Förnamn och efternamn:', font=('calibre', 10, 'bold'))
    name_entry = tk.Entry(UI, textvariable=input_name, font=('calibre', 10, 'normal'))
    name_label.grid(row=0, column=0)
    name_entry.grid(row=0, column=1)

    # - Social security number
    social_secnumb_label = tk.Label(UI, text='Personnummer yyyy-mm-dd-xxxx:', font=('calibre', 10, 'bold'))
    social_secnumb_entry = tk.Entry(UI, textvariable=input_social_numb, font=('calibre', 10, 'normal'))
    social_secnumb_label.grid(row=1, column=0)
    social_secnumb_entry.grid(row=1, column=1)

    # - Username
    name_label = tk.Label(UI, text='Användarnamn:', font=('calibre', 10, 'bold'))
    name_entry = tk.Entry(UI, textvariable=input_username, font=('calibre', 10, 'normal'))
    name_label.grid(row=3, column=0)
    name_entry.grid(row=3, column=1)

    # - Password
    name_label = tk.Label(UI, text='Lösenord:', font=('calibre', 10, 'bold'))
    name_entry = tk.Entry(UI, show='*', textvariable=input_password, font=('calibre', 10, 'normal'))
    name_label.grid(row=4, column=0)
    name_entry.grid(row=4, column=1)

    # - Password repeat
    name_label = tk.Label(UI, text='Repetera lösenordet:', font=('calibre', 10, 'bold'))
    name_entry = tk.Entry(UI, show='*', textvariable=input_password_repeat, font=('calibre', 10, 'normal'))
    name_label.grid(row=5, column=0)
    name_entry.grid(row=5, column=1)

    # - Guide text
    guide_label1 = tk.Label(UI, text='         Vid två förnamn eller efternamn så skrivs de             ',
                            font=('calibre', 8, 'bold'))
    guide_label1.grid(row=7, column=0)
    guide_label2 = tk.Label(UI, text='tillsammans med hjälp av ett bindesstreck "-".', font=('calibre', 8, 'bold'))
    guide_label2.grid(row=8, column=0)

    # - Placeholder label to give the window UI structure.
    structurelabel = tk.Label(UI, fg='white', text='--------------------------------------------------------',
                              font=('calibre', 12, 'bold'))
    structurelabel.grid(row=6, column=1)

    # - Tells the user to follow the instructions.
    invalid_ssn3 = tk.Label(UI, text='Skriv in ditt namn och personnummer', font=('calibre', 12, 'bold'))
    invalid_ssn3.grid(row=6, column=1)

    # - Variable connected to the invalid_SSN functions.
    label_variable = 0

    # Functions:
    # - First function which adds a text saying the SSN is invalid.
    def invalid_SSN():
        label_cover_1 = tk.Label(UI, fg='white', text='--------------------------------------------------------',
                                 font=('calibre', 12, 'bold'))
        label_cover_1.grid(row=6, column=1)
        invalid_ssn = tk.Label(UI, text='Personnummret är ogiltigt', font=('calibre', 12, 'bold'))
        invalid_ssn.grid(row=6, column=1)

    # - Second function which adds a text saying the SSN is invalid.
    def invalid_SSN2():
        label_cover_2 = tk.Label(UI, fg='white', text='--------------------------------------------------------',
                                 font=('calibre', 12, 'bold'))
        label_cover_2.grid(row=6, column=1)
        invalid_ssn2 = tk.Label(UI, text='Organisera personnummret som yyyy-mm-dd-xxxx', font=('calibre', 12, 'bold'))
        invalid_ssn2.grid(row=6, column=1)

    # - Third function which adds a text saying the SSN is invalid.
    def invalid_SSN3():
        label_cover_3 = tk.Label(UI, fg='white', text='--------------------------------------------------------',
                                 font=('calibre', 12, 'bold'))
        label_cover_3.grid(row=6, column=1)
        invalid_ssn3 = tk.Label(UI, text='Använd endast siffror för personnummret', font=('calibre', 12, 'bold'))
        invalid_ssn3.grid(row=6, column=1)

    # - First function which adds a text saying the name is invalid.
    def invalid_name():
        label_cover_3 = tk.Label(UI, fg='white', text='--------------------------------------------------------',
                                 font=('calibre', 12, 'bold'))
        label_cover_3.grid(row=6, column=1)
        invalid_name1 = tk.Label(UI, text='Använd endast bokstäver för namnet', font=('calibre', 12, 'bold'))
        invalid_name1.grid(row=6, column=1)

    # - second function which adds a text saying the name is invalid.
    def invalid_name2():
        label_cover_4 = tk.Label(UI, fg='white', text='--------------------------------------------------------',
                                 font=('calibre', 12, 'bold'))
        label_cover_4.grid(row=6, column=1)
        invalid_name2 = tk.Label(UI, text='Namnet är för kort', font=('calibre', 12, 'bold'))
        invalid_name2.grid(row=6, column=1)

    # - Third function which adds a text saying the name is invalid.
    def invalid_name3():
        label_cover_5 = tk.Label(UI, fg='white', text='--------------------------------------------------------',
                                 font=('calibre', 12, 'bold'))
        label_cover_5.grid(row=6, column=1)
        invalid_name3 = tk.Label(UI, text='Skriv både förnamn och efternamn', font=('calibre', 12, 'bold'))
        invalid_name3.grid(row=6, column=1)

    # - Fourth function which adds a text saying the name is invalid.
    def invalid_name4():
        label_cover_6 = tk.Label(UI, fg='white', text='--------------------------------------------------------',
                                 font=('calibre', 12, 'bold'))
        label_cover_6.grid(row=6, column=1)
        invalid_name4 = tk.Label(UI, text='Du har ett mellanslag felplacerat i namnet', font=('calibre', 12, 'bold'))
        invalid_name4.grid(row=6, column=1)

    # - Function which adds a text telling the user not to forget their SSN.
    def dont_forget_SSN():
        dont_forget_SSN_cover = tk.Label(UI, fg='white',
                                         text='--------------------------------------------------------',
                                         font=('calibre', 12, 'bold'))
        dont_forget_SSN_cover.grid(row=6, column=1)
        dont_forget_SSN = tk.Label(UI, text='Glöm inte att skriva ditt personnummer', font=('calibre', 12, 'bold'))
        dont_forget_SSN.grid(row=6, column=1)

    # - Function which adds a text telling the user not to forget their name.
    def dont_forget_name():
        dont_forget_name_cover = tk.Label(UI, fg='white',
                                          text='--------------------------------------------------------',
                                          font=('calibre', 12, 'bold'))
        dont_forget_name_cover.grid(row=6, column=1)
        dont_forget_name = tk.Label(UI, text='Glöm inte att skriva ditt namn', font=('calibre', 12, 'bold'))
        dont_forget_name.grid(row=6, column=1)

    def dont_forget_username():
        dont_forget_username_cover = tk.Label(UI, fg='white',
                                              text='--------------------------------------------------------',
                                              font=('calibre', 12, 'bold'))
        dont_forget_username_cover.grid(row=6, column=1)
        dont_forget_username = tk.Label(UI, text='Glöm inte att skriva ditt användarnamn', font=('calibre', 12, 'bold'))
        dont_forget_username.grid(row=6, column=1)

    # - Function whichs adds a text telling the user their written password and repeated password does not match.
    def password_error1():
        password_error1_cover = tk.Label(UI, fg='white',
                                         text='--------------------------------------------------------',
                                         font=('calibre', 12, 'bold'))
        password_error1_cover.grid(row=6, column=1)
        password_error1 = tk.Label(UI, text='Lösenordet matchar inte', font=('calibre', 12, 'bold'))
        password_error1.grid(row=6, column=1)

    def password_error2():
        password_error2_cover = tk.Label(UI, fg='white',
                                         text='--------------------------------------------------------',
                                         font=('calibre', 12, 'bold'))
        password_error2_cover.grid(row=6, column=1)
        password_error2 = tk.Label(UI, text='Lösenordet är för kort', font=('calibre', 12, 'bold'))
        password_error2.grid(row=6, column=1)

    def password_error3():
        password_error3_cover = tk.Label(UI, fg='white',
                                         text='--------------------------------------------------------',
                                         font=('calibre', 12, 'bold'))
        password_error3_cover.grid(row=6, column=1)
        password_error3 = tk.Label(UI, text='Lösenordet innehåller mellanslag', font=('calibre', 12, 'bold'))
        password_error3.grid(row=6, column=1)

    def username_error():
        username_error1_cover = tk.Label(UI, fg='white',
                                         text='--------------------------------------------------------',
                                         font=('calibre', 12, 'bold'))
        username_error1_cover.grid(row=6, column=1)
        username_error1 = tk.Label(UI, text='Användarnamnet får inte innehålla mellanslag',
                                   font=('calibre', 12, 'bold'))
        username_error1.grid(row=6, column=1)

    def username_error2():
        username_error2_cover = tk.Label(UI, fg='white',
                                         text='--------------------------------------------------------',
                                         font=('calibre', 12, 'bold'))
        username_error2_cover.grid(row=6, column=1)
        username_error2 = tk.Label(UI, text='Glöm inte användarnamnet', font=('calibre', 12, 'bold'))
        username_error2.grid(row=6, column=1)

    def username_taken():
        username_taken_cover = tk.Label(UI, fg='white', text='--------------------------------------------------------',
                                        font=('calibre', 12, 'bold'))
        username_taken_cover.grid(row=6, column=1)
        username_taken = tk.Label(UI, text='Användarnamnet används redan', font=('calibre', 12, 'bold'))
        username_taken.grid(row=6, column=1)

    def SSN_taken():
        SSN_taken_cover = tk.Label(UI, fg='white', text='--------------------------------------------------------',
                                   font=('calibre', 12, 'bold'))
        SSN_taken_cover.grid(row=6, column=1)
        SSN_taken = tk.Label(UI, text='Personnummret används redan', font=('calibre', 12, 'bold'))
        SSN_taken.grid(row=6, column=1)

    # - Function which removes old UI and creates a new one with given elements.
    def registration():
        UI.destroy()
        global UI2
        UI2 = tk.Tk()
        UI2.geometry("700x500+200+150")
        UI2.title("Tack")
        UI2['bg'] = 'green'
        registered = tk.Label(UI2, bg='green', fg='white', text=(
        "Tack " + str(input_name.get()) + ", du är nu registrerad som en medlem hos DURAN."),
                              font=('calibre', 16, 'bold'))
        registered.grid(row=1, column=0)
        sub_btn4 = tk.Button(UI2, highlightbackground='green', text='Logga in', command=already_registered2)
        sub_btn4.grid(row=1, column=2)
        add_user_to_database()

    # - Function which opens database and adds user into it.
    def add_user_to_database():
        yyyy_mm_dd_xxxx = str(input_social_numb.get())
        name = str(input_name.get())
        username = str(input_username.get())
        password = str(input_password.get())
        locating_var = "DURAN"
        conn = sqlite3.connect('Members of DURAN.db')

        c = conn.cursor()

        # - Adds user
        c.execute("INSERT INTO Registered_members_DURAN VALUES (?, ?, ?, ?, ?)",
                  (yyyy_mm_dd_xxxx, name, username, password, locating_var))

        conn.commit()

        # - Closes database
        conn.close()

    # - Function for button press.
    def submit():
        # * Asks the user for their social security number and splits it into 4 variables yyyy, mm, dd, xxxx.
        yyyy_mm_dd_xxxx = str(input_social_numb.get())
        chunks = yyyy_mm_dd_xxxx.split('-')

        # * Puts the previous splits together and splits it again letter by letter.
        yyyymmddxxxx = chunks[0] + chunks[1] + chunks[2] + chunks[3]

        def splitword(word):
            return [char for char in word]

        # * Calculates the first part of the social security number algorithm.
        amountlist = list(
            (int(yyyymmddxxxx[2]) * 2, int(yyyymmddxxxx[3]), int(yyyymmddxxxx[4]) * 2, int(yyyymmddxxxx[5]),
             int(yyyymmddxxxx[6]) * 2, int(yyyymmddxxxx[7]), int(yyyymmddxxxx[8]) * 2, int(yyyymmddxxxx[9]),
             int(yyyymmddxxxx[10]) * 2))

        # * Calculates the second part of the social security number algorithm.
        # * Predetermines the value of "x" to = 0.
        x = 0
        # * Iterates all elements in amountlist and separates any numbers with two digits, otherwise they are left as they are. It then adds them together into variable "x".
        for i in amountlist:
            if len(str(i)) == 2:
                split_dual_number = splitword(str(i))
                for i in split_dual_number:
                    x = x + int(i)
            else:
                x = x + i

        # * X is now the added number of all individual digits inside amountlist and by doing the below we split the number we get into two.
        split_final_number = (splitword(str(x)))

        # * Definition which finalizes whether or not your social security number is valid or not.
        def validity_checker():
            if (int(split_final_number[1])) == int(yyyymmddxxxx[11]) and (int(split_final_number[1])) == 0:
                registration()
            else:
                friend_of_10 = 10 - (int(split_final_number[1]))
                if friend_of_10 == int(yyyymmddxxxx[11]):
                    registration()
                else:
                    invalid_SSN()

        # * Starts validity checker
        validity_checker()

    # - First function which checks if Social Security Number is written incorrectly. It checks if there are 15 symbols present.
    def SSN_checker():
        yyyy_mm_dd_xxxx = str(input_social_numb.get())
        if len(yyyy_mm_dd_xxxx) == 0:
            dont_forget_SSN()
        else:
            if len(yyyy_mm_dd_xxxx) < 15:
                invalid_SSN2()
            elif len(yyyy_mm_dd_xxxx) > 15:
                invalid_SSN2()
            else:
                chunks = yyyy_mm_dd_xxxx.split('-')
                yyyymmddxxxx = chunks[0] + chunks[1] + chunks[2] + chunks[3]
                if not re.match("^[0-9]*$", yyyymmddxxxx):
                    invalid_SSN3()
                else:
                    SSN_checker2()

    # - Second function which checks if Social Security number is written incorrectly. It checks if there are 3 "-" present and if they are placed correctly.
    def SSN_checker2():
        b = 0
        yyyy_mm_dd_xxxx = str(input_social_numb.get())
        for i in yyyy_mm_dd_xxxx:
            if i == "-":
                b = b + 1
        if b == 3 and list(yyyy_mm_dd_xxxx)[4] == "-" and list(yyyy_mm_dd_xxxx)[7] == "-" and list(yyyy_mm_dd_xxxx)[
            10] == "-":
            username_checker()
        else:
            invalid_SSN()

    # - First function which checks if name is valid.
    def name_checker():
        name = str(input_name.get())
        x = 0
        if len(name) == 0:
            dont_forget_name()
        else:
            for i in name:
                if i == " ":
                    x = x + 1
            if x == 0:
                invalid_name3()

            else:
                split_replaced_name = name.split(" ")
                if len(split_replaced_name[0]) < 2 or len(split_replaced_name[1]) < 2:
                    invalid_name4()
                else:
                    spaces = 0
                    for i in name:
                        if i == " ":
                            spaces = spaces + 1
                    if spaces == 1:
                        name_checker2()
                    else:
                        invalid_name3()

    # - Second function which checks if name is valid.
    def name_checker2():
        name = str(input_name.get())
        split_name1 = name.split(" ")
        attached_name1 = split_name1[0] + split_name1[1]
        line = 0
        for i in name:
            if i == "-":
                line = line + 1
        if line == 1:
            split_name2 = attached_name1.split("-")
            attached_name2 = split_name2[0] + split_name2[1]

            if not re.match("^[A-ö]*$", attached_name2):
                invalid_name()
            else:
                name_checker3()
        elif line == 2:
            split_name2 = attached_name1.split("-")
            attached_name2 = split_name2[0] + split_name2[1] + split_name2[2]

            if not re.match("^[A-ö]*$", attached_name2):
                invalid_name()
            else:
                name_checker3()

        else:
            if not re.match("^[A-ö]*$", attached_name1):
                invalid_name()
            else:
                name_checker3()

    # - Third function which checks if name is valid.
    def name_checker3():
        name = str(input_name.get())
        if "-" in name:
            replaced_name = name.replace(" ", "-")
            split_replaced_name = replaced_name.split("-")
            if len(split_replaced_name[0]) < 2 or len(split_replaced_name[1]) < 2 or len(split_replaced_name[2]) < 2:
                invalid_name2()
            else:
                SSN_checker()
        else:
            SSN_checker()

    # - First function which checks if password and repeated password matches eachother
    def password_checker():
        password = str(input_password.get())
        password_repeat = str(input_password_repeat.get())
        if password == password_repeat:
            password_checker2()
        else:
            password_error1()

    # - Second function which checks if password is possible.
    def password_checker2():
        password = str(input_password.get())
        if len(password) < 8:
            password_error2()
        else:
            password_checker3()

    # - Third function which checks if password is possible
    def password_checker3():
        password = str(input_password.get())
        x = 0
        for i in password:
            if i == " ":
                x = x + 1
            else:
                pass
        if x == 1 or x > 1:
            password_error3()
        else:
            SSN_checker_database()

    def username_checker():
        username = str(input_username.get())
        if username == "":
            dont_forget_username()
        else:
            username_checker2()

    def username_checker2():
        username = str(input_username.get())
        x = 0
        for i in username:
            if i == " ":
                x = x + 1
            else:
                pass
        if x == 1 or x > 1:
            username_error()
        else:
            username_checker3()

    def username_checker3():
        username = str(input_username.get())
        if username == "":
            username_error2()
        else:
            username_checker4()

    def username_checker4():
        username = str(input_username.get())
        c.execute("SELECT * FROM Registered_members_DURAN WHERE locating_var='DURAN'")
        user_list = c.fetchall()
        x = 0
        if user_list == []:
            password_checker()
        else:
            for i in user_list:
                if i[2] == username:
                    x = x + 1
                else:
                    pass
            if x == 1:
                username_taken()
            else:
                conn.commit()
                password_checker()

    def SSN_checker_database():
        SSN = str(input_social_numb.get())
        c.execute("SELECT * FROM Registered_members_DURAN WHERE locating_var='DURAN'")
        user_list = c.fetchall()
        x = 0
        if user_list == []:
            submit()
        else:
            for i in user_list:
                if i[0] == SSN:
                    x = x + 1
                else:
                    pass
            if x == 1:
                SSN_taken()
            else:
                conn.commit()
                submit()

    # UI elements 3.
    # - Button
    sub_btn = tk.Button(UI, text='Fortsätt', command=name_checker)
    sub_btn.grid(row=7, column=1)

    # - Button 2
    sub_btn2 = tk.Button(UI, text='Redan registrerad?', command=already_registered)
    sub_btn2.grid(row=8, column=1)

    # Infinite UI loop.
    UI.mainloop()

def already_registered2():
    UI2.destroy()
    already_registered_to()

def already_registered():
    UI.destroy()
    already_registered_to()

def already_registered_to():
    global UI5
    UI5 = tk.Tk()
    UI5.geometry("700x500+200+150")
    UI5.title("Var vänlig logga in")
    UI5['bg'] = 'white'

    input_username_login = tk.StringVar()
    input_password_login = tk.StringVar()


    structure_label = tk.Label(UI5, fg='white', text='--------------------------------------------------------',
                               font=('calibre', 12, 'bold'))
    structure_label.grid(row=1, column=1)

    username_login_label = tk.Label(UI5, text='Användarnamn:', font=('calibre', 10, 'bold'))
    username_login_entry = tk.Entry(UI5, textvariable=input_username_login, font=('calibre', 10, 'normal'))
    username_login_label.grid(row=0, column=1)
    username_login_entry.grid(row=0, column=2)

    password_label = tk.Label(UI5, text='Lösenord:', font=('calibre', 10, 'bold'))
    password_entry = tk.Entry(UI5, show='*', textvariable=input_password_login, font=('calibre', 10, 'normal'))
    password_label.grid(row=1, column=1)
    password_entry.grid(row=1, column=2)

    def username_checker_login():
        conn = sqlite3.connect('Members of DURAN.db')
        c = conn.cursor()
        username_login = str(input_username_login.get())
        password_login = str(input_password_login.get())
        c.execute("SELECT * FROM Registered_members_DURAN WHERE locating_var='DURAN'")
        user_list = c.fetchall()
        x = 0
        if user_list == []:
            no_account_registered_yet()
        else:
            for i in user_list:
                if i[2] == username_login:
                    x = x + 1
                    global matched_account
                    matched_account = i
                else:
                    pass
            if x == 1:
                if matched_account[3] == password_login:
                    log_in()
                else:
                    password_does_not_match()
            else:
                no_account_matched_username()


    sub_btn3 = tk.Button(UI5, text='Tillbaka', command=go_back)
    sub_btn3.grid(row=0, column=0)
    sub_btn5 = tk.Button(UI5, text='Logga in', command=username_checker_login)
    sub_btn5.grid(row=2, column=2)

    UI5.mainloop()

def go_back():
    UI5.destroy()
    everything()

def go_back2():
    UI5.destroy()
    everything()

def password_does_not_match():
    label_cover_1 = tk.Label(UI5, fg='white', text='--------------------------------------------------------',
                             font=('calibre', 12, 'bold'))
    label_cover_1.grid(row=6, column=1)
    invalid_ssn = tk.Label(UI5, text='Lösenordet matchar inte användarnamnet', font=('calibre', 12, 'bold'))
    invalid_ssn.grid(row=6, column=1)


def no_account_registered_yet():
    label_cover_1 = tk.Label(UI5, fg='white', text='--------------------------------------------------------',
                             font=('calibre', 12, 'bold'))
    label_cover_1.grid(row=6, column=1)
    invalid_ssn = tk.Label(UI5, text='Inget konto är registrerat', font=('calibre', 12, 'bold'))
    invalid_ssn.grid(row=6, column=1)

def no_account_matched_username():
    label_cover_1 = tk.Label(UI5, fg='white', text='--------------------------------------------------------',
                             font=('calibre', 12, 'bold'))
    label_cover_1.grid(row=6, column=1)
    invalid_ssn = tk.Label(UI5, text='Inget konto registrerat med det användarnamnet', font=('calibre', 12, 'bold'))
    invalid_ssn.grid(row=6, column=1)

def log_in():
    UI5.destroy()
    global UI6
    UI6 = tk.Tk()
    UI6.geometry("700x500+200+150")
    UI6.title("Välkommen tillbaka " + matched_account[2] + ".")

    sub_btn6 = tk.Button(UI6, text='Logga ut', command=log_out)
    sub_btn6.grid(row=0, column=0)
    sub_btn_game1 = tk.Button(UI6, text='Profil', command=profile)
    sub_btn_game1.grid(row=0, column=1)

def log_out():
    UI6.destroy()
    already_registered_to()

def profile():
    profile_name = tk.Label(UI5, fg='white', text=(str(input_username.get())),
                             font=('calibre', 12, 'bold'))
    profile_name.grid(row=6, column=1)

everything()