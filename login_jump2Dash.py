# import libraries - pygame, tkinter and other python files
import pygame

from tkinter import *
from tkinter import messagebox
from tkinter import font as tkFont

from re import fullmatch

from login_signup import signup
from login_signup import verify_login
from launch_game import launch


# play background sound
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()

pygame.mixer.music.load('sound/music.wav')
pygame.mixer.music.play(-1, 0.0, 5000)

# dispay main login window and set it's properties
root = Tk()

root.title('Login Jump Jump Dash')
root.geometry('700x550+310+130')
root.resizable(False, False)

btn_font = tkFont.Font(family='Bauhaus 93', size='14', weight='bold')
label_font = tkFont.Font(family='Bauhaus 93', size='16', weight='bold')
signup_font = tkFont.Font(family='Bauhaus 93', size='14', weight='bold')

bg = PhotoImage(file="img/sky.png")

# creating canvas to draw banner and backgorund image
canvas1 = Canvas(root, width=700,
                 height=550)
canvas1.place(x=0, y=0)
canvas1.create_image(0, 0, image=bg,
                     anchor="nw")

canvas1.create_rectangle(
    610, 140, 100, 55, outline='brown', width=10, fill='orange')


canvas1.create_text(350, 100, text="JUMP JUMP DASH",
                    font=('Bauhaus 93', '38', 'bold'), fill="white")


# frame container of login form and sign up form
# discarded and loaded dynamically on button click
bottomFrame = Frame(root, bg="#ffeabd")
bottomFrame.place(x=168, y=320)


# called when Login button is clicked
def initializeLogin():
    login_form()


# called when Sign up button is clicked
def initializeSignUp():
    signup_form()


# called when Play Guest button is clicked
def playGuest():
    root.destroy()
    launch()


# Login button
button1 = Button(root, text="Login", font=btn_font,
                 bg="#f7dda1", fg="brown", command=initializeLogin)
button1.place(x=150, y=200)

# Sign up buton
button2 = Button(root, text="Sign Up", font=btn_font,
                 bg="#f7dda1", fg="brown", command=initializeSignUp)
button2.place(x=270, y=200)


# Play guest button
button3 = Button(root, text="Play Guest", font=btn_font,
                 bg="#f7dda1", fg="brown", command=playGuest)
button3.place(x=420, y=200)


# Exit Button
buttonExit = Button(root, text="Exit", font=('Bauhaus 93', '8', 'normal'),
                    bg="#f7dda1", fg="brown", command=root.destroy)
buttonExit.place(x=670, y=5)


# Form loaded when Login button is clicked
def login_form():
    print('inside load form')
    clear_frame()
    loginFrame = Frame(bottomFrame, bg="#ffeabd")
    loginFrame.grid(row=0, column=0)
    label_Name = Label(loginFrame, text="Name", font=label_font, fg="brown")
    label_Password = Label(loginFrame, text="Password",
                           font=label_font, fg="brown")
    global entry_name
    entry_name = Entry(loginFrame, font=label_font)
    global entry_password
    entry_password = Entry(loginFrame, show="*", font=label_font)

    label_Name.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))
    label_Password.grid(row=1, column=0, padx=(10, 10), pady=(10, 10))

    entry_name.grid(row=0, column=1, padx=(10, 10), pady=(10, 10))
    entry_password.grid(row=1, column=1, padx=(10, 10), pady=(10, 10))

    bottomFrame.place(x=168, y=320)

    # check credentials when Get Started button is clicked
    login_button = Button(bottomFrame, text="Get Started!",
                          font=label_font, bg="#f7dda1", fg="brown", command=check_login_creds)
    login_button.grid(row=2, column=0, padx=(25, 10), pady=(10, 10))


# Form loaded when Sign up button is clicked
def signup_form():
    print('inside load form')
    clear_frame()
    signupFrame = Frame(bottomFrame, bg="#ffeabd")
    signupFrame.grid(row=1, column=0)
    label_Name = Label(signupFrame, text="Name", font=signup_font, fg="brown")
    label_Password = Label(signupFrame, text="Password",
                           font=signup_font, fg="brown")
    label_ConfirmPassword = Label(
        signupFrame, text="Confirm Password", font=signup_font, fg="brown")
    global entry_name
    entry_name = Entry(signupFrame, font=signup_font)
    global entry_password
    entry_password = Entry(signupFrame, show="*", font=signup_font)
    global entry_ConfirmPassword
    entry_ConfirmPassword = Entry(signupFrame, show="*", font=signup_font)

    label_Name.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))
    label_Password.grid(row=1, column=0, padx=(10, 10), pady=(10, 10))
    label_ConfirmPassword.grid(row=2, column=0, padx=(10, 10), pady=(10, 10))

    entry_name.grid(row=0, column=1, padx=(10, 10), pady=(10, 10))
    entry_password.grid(row=1, column=1, padx=(10, 10), pady=(10, 10))
    entry_ConfirmPassword.grid(row=2, column=1, padx=(10, 10), pady=(10, 10))

    label_info = Label(
        bottomFrame, text="Enter a combination of alphanumeric and special characters",
        font=('Bauhaus 93', '10', 'normal'), fg="brown", bg="#ffeabd")
    label_info.grid(row=0, column=0, padx=(10, 10), pady=(0, 0))

    bottomFrame.place(x=140, y=300)

    # validates and inserts when Sign up button is clicked on form
    signup_button = Button(bottomFrame, text="Sign Up",
                           font=signup_font, bg="#f7dda1", fg="brown", command=sign_up_db)
    signup_button.grid(row=2, column=0, padx=(25, 10), pady=(10, 10))


# discard bottom frame before loading a new contents
def clear_frame():
    for widgets in bottomFrame.winfo_children():
        widgets.destroy()


# check credentials when Get Started button is clicked
def check_login_creds():
    username = entry_name.get().strip()
    passw = entry_password.get().strip()
    if passw != "" and username != "":
        if fullmatch(r'[A-Za-z0-9_@#$%^&-+=]{8,25}', passw) and fullmatch(r'[A-Za-z0-9_@#$%^&-+=]{5,25}', username):
            # Call verify_login method from login_signup.py imported
            login_status = verify_login(username, passw)
            if login_status == 1:
                # if login is successful, destroy the login screen and launch the game
                root.destroy()
                launch()
            elif login_status == 2:
                messagebox.showerror(
                    "Invalid", "Invalid PASSWORD. Try again!!")
            elif login_status == 3:
                messagebox.showerror(
                    "Invalid", "Invalid USERNAME. Try again!!")
            else:
                print("invalid creds")
                messagebox.showerror(
                    "Some Exception", "Some error occurred, contact Admin!")
        else:
            messagebox.showerror(
                "Length of characters", "Username and password has maximum 5-25 characters.\nPassword should be have 8-25 characters minimum.")
    else:
        messagebox.showerror(
            "Credentials Missing", "Enter username and password to Login")


# validates and inserts when Sign up button is clicked on form
def sign_up_db():
    username = entry_name.get().strip()
    passw = entry_password.get().strip()
    confirm_passw = entry_ConfirmPassword.get().strip()

    if username != "" and passw != "" and confirm_passw != "":
        if fullmatch(r'[A-Za-z0-9_@#$%^&-+=]{5,25}', username):
            if fullmatch(r'[A-Za-z0-9_@#$%^&-+=]{8,25}', passw):
                # match
                if passw == confirm_passw:
                    # Call signup method from login_signup.py imported
                    signup_status = signup(username, passw)
                    if signup_status == 1:
                        # if signup successful, redirect to login
                        messagebox.showinfo(
                            "Singup Successful", "Signed Up successfully. Proceed to Login!!")
                        login_form()
                    elif signup_status == 2:
                        messagebox.showerror(
                            "Player name taken", "Player name already taken, try another one!!")
                    else:
                        messagebox.showerror(
                            "Some error", "Some error occurred, contact Admin!")
                else:
                    messagebox.showerror(
                        "Credentials Missing", "Password doesn't match Confirm Password")
            else:
                messagebox.showerror(
                    "Password format", "Passowrd should: \n\t- Be atleast 8-25 characters in length\n\t- Contain alphanumeric\n\t-Have atleast 1 special character.")
        else:
            messagebox.showerror(
                "Length of characters", "Username should have maximum 5-25 characters.")
    else:
        messagebox.showerror(
            "Credentials Missing", "Enter username, password and Confirm Password to Sign Up.")


root.mainloop()
