
from Terms_Conditions import Terms_Conditions_Gaming
from pathlib import Path
import os, sys
import customtkinter
import tkinter
from tkinter import messagebox
from customtkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, CHECKBUTTON, IntVar

relativeLocate = os.getcwd()
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = customtkinter.CTk()
window.geometry("344x234")
window.title("Account Creation")
window.configure(bg = "#FFFFFF")


def create_acc():
    global TermsValue
    TermsValue = False

    if TermsValue == False:
        Terms_Conditions_Gaming()
        TermsValue = True

    if TermsValue == True:
        with open(
                r'assets\credentials\username.ini',
                'a') as user1:
            user1.write(f"{(entry_1.get())}\n")
        with open(
                r'assets\credentials\password.ini',
                'a') as pass1:
            pass1.write(f"{(entry_2.get())}\n")

        with open(
                r'assets\credentials\email.ini',
                'a') as email:
            email.write(f"{(entry_3.get())}\n")
        window.destroy()

        user1.close()
        pass1.close()
        email.close()
        os.system('gui.py')

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 293,
    width = 430,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    215.0,
    147.0,
    image=image_image_1
)

canvas.create_text(
    215.0,
    4.0,
    anchor="nw",
    text="Create Account",
    fill="#000000",
    font=("RobotoRoman SemiBold", 27 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    197.0,
    83.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#ECECEC",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=44.0,
    y=73.0,
    width=306.0,
    height=23.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    197.0,
    132.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#ECECEC",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=44.0,
    y=122.0,
    width=306.0,
    height=23.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    196.5,
    181.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#ECECEC",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=43.0,
    y=171.0,
    width=307.0,
    height=23.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    196.5,
    230.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#ECECEC",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=43.0,
    y=220.0,
    width=307.0,
    height=23.0
)

canvas.create_text(
    41.0,
    55.0,
    anchor="nw",
    text="Username",
    fill="#000000",
    font=("RobotoRoman Light", 13 * -1)
)

canvas.create_text(
    41.0,
    103.0,
    anchor="nw",
    text="Password",
    fill="#000000",
    font=("RobotoRoman Light", 13 * -1)
)

canvas.create_text(
    41.0,
    152.0,
    anchor="nw",
    text="Email",
    fill="#000000",
    font=("RobotoRoman Light", 13 * -1)
)

canvas.create_text(
    40.0,
    202.0,
    anchor="nw",
    text="School Name",
    fill="#000000",
    font=("RobotoRoman Light", 13 * -1)
)

canvas.create_text(
    219.0,
    36.0,
    anchor="nw",
    text="Enhance your learning",
    fill="#000000",
    font=("RobotoRoman Regular", 13 * -1)
)

def Terms_Conditions():
    os.system('Terms_Conditions.py')

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=Terms_Conditions,
    relief="flat"
)
button_1.place(
    x=293.0,
    y=260.0,
    width=58.0,
    height=17.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=create_acc,
    relief="flat"
)
button_2.place(
    x=40.0,
    y=255.0,
    width=74.0,
    height=28.0
)

canvas.create_text(
    180.0,
    263.0,
    anchor="nw",
    text="Terms and Conditions",
    fill="#000000",
    font=("RobotoRoman Regular", 10 * -1)
)

#Check box for terms and conditions, lol who cares
#check_var = customtkinter.StringVar(value="off")
#checkbox = customtkinter.CTkCheckBox(window,text="I agree to the terms and conditions",font=("RobotoRoman Regular", 10 * -1),
                                     #checkbox_width=15,checkbox_height=15, variable=check_var,
                                     #onvalue="on", offvalue="off")
#checkbox.pack(padx=100,pady=100)


#canvas.create_rectangle(
    #67.0,
    #205.0,
    #81.0,
    #219.0,
    #fill="#FFFFFF",
    #outline="")


window.resizable(False, False)
window.mainloop()
