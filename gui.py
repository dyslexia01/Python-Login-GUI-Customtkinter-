
import pywinstyles
from pathlib import Path
import importlib
import os,sys
import customtkinter
import tkinter
from tkinter import messagebox
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel

relativeLocate = os.getcwd()
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")

OUTPUT_PATHforget = Path(__file__).parent
ASSETS_PATHforget = OUTPUT_PATHforget / Path(r"assets\frame2")

OUTPUT_PATHconfirm = Path(__file__).parent
ASSETS_PATHconfirm = OUTPUT_PATHconfirm / Path(r"assets\frame3")

window = customtkinter.CTk()

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def relative_to_assetsForget(path: str) -> Path:
    return ASSETS_PATHforget / Path(path)

def relative_to_assetsCONFIRM(path: str) -> Path:
    return ASSETS_PATHconfirm / Path(path)

def Create_Acc():
    window.destroy()
    os.system('gui1.py')

def create_Forget_Pass():
    # Destroy the existing canvas
    canvas.delete("all")
    button_1.destroy()
    button_2.destroy()
    button_3.destroy()
    entry_1.destroy()
    entry_2.destroy()
    Forget_Pass()



def create_Confirm():
    Valid = False

    for i in range(0, len(username)):
        if entry_1F.get() in username[i] and entry_2F.get() in emailReset[i]:
            Valid = True

    if Valid == True:
            global TempUser
            TempUser = entry_1F.get()
            print(TempUser)

            canvas.delete("all")
            entry_1F.destroy()
            entry_2F.destroy()
            entry_3F.destroy()
            button_1F.destroy()
            Confirm_Pass()
    else:
        messagebox.showerror(title="Error", message="Invalid Credentials.")

def Go_Back_Login():
    State = False
    if entry_2C.get() != entry_1C.get():
        messagebox.showerror(title="Error", message="Please confirm by writing the same password again.")
    else:
        State = True

    if State == True:
        for i in range(0, len(username)):
            if TempUser in username[i]:
                password[i] = password[i].replace(password[i], entry_1C.get())

        print(entry_1C.get())
        print(password)

        Passchange = open(r"assets\credentials\password.ini", 'w')
        for i in range(0, len(password)):
            Passchange.write(f"{password[i]}")
        Passchange.close()

        # Destroy the existing canvas
        canvas.delete("all")
        button_1C.destroy()
        entry_1C.destroy()
        entry_2C.destroy()

        login_page()

def Confirm_Pass():

    window.title("Confirm")

    image_image_1 = PhotoImage(
        file=relative_to_assetsCONFIRM("image_1.png"))
    image_1 = canvas.create_image(
        244.0,
        147.0,
        image=image_image_1
    )

    canvas.create_text(
        86.0,
        15.0,
        anchor="nw",
        text="Set a New Password",
        fill="#000000",
        font=("RobotoRoman SemiBold", 27 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assetsCONFIRM("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        218.0,
        122.5,
        image=entry_image_1
    )

    global entry_1C
    entry_1C = Entry(
        bd=0,
        bg="#ECECEC",
        fg="#000716",
        highlightthickness=0
    )
    entry_1C.place(
        x=65.0,
        y=112.0,
        width=306.0,
        height=23.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assetsCONFIRM("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        218.5,
        181.5,
        image=entry_image_2
    )

    global entry_2C
    entry_2C = Entry(
        bd=0,
        bg="#ECECEC",
        fg="#000716",
        highlightthickness=0
    )
    entry_2C.place(
        x=65.0,
        y=171.0,
        width=307.0,
        height=23.0
    )

    canvas.create_text(
        62.0,
        94.0,
        anchor="nw",
        text="New Password",
        fill="#000000",
        font=("RobotoRoman Light", 13 * -1)
    )

    canvas.create_text(
        62.0,
        155.0,
        anchor="nw",
        text="Confirm Password",
        fill="#000000",
        font=("RobotoRoman Light", 13 * -1)
    )

    canvas.create_text(
        86.0,
        47.0,
        anchor="nw",
        text="Something memorable...",
        fill="#000000",
        font=("RobotoRoman Regular", 13 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assetsCONFIRM("button_1.png"))

    global button_1C
    button_1C = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=Go_Back_Login,
        relief="flat"
    )
    button_1C.place(
        x=62.0,
        y=221.0,
        width=77.0,
        height=33.0
    )
    #window.resizable(False, False)
    window.mainloop()

def Forget_Pass():

    window.title("Forget Password")

    image_image_1 = PhotoImage(
        file=relative_to_assetsForget("image_1.png"))
    image_1 = canvas.create_image(
        244.0,
        147.0,
        image=image_image_1
    )

    canvas.create_text(
        77.0,
        13.0,
        anchor="nw",
        text="Forgot Password?",
        fill="#000000",
        font=("RobotoRoman SemiBold", 27 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assetsForget("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        173.5,
        104.5,
        image=entry_image_1
    )
    global entry_1F
    entry_1F = Entry(
        bd=0,
        bg="#ECECEC",
        fg="#000716",
        highlightthickness=0
    )
    entry_1F.place(
        x=54.0,
        y=94.0,
        width=239.0,
        height=23.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assetsForget("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        173.5,
        159.5,
        image=entry_image_2
    )

    global entry_2F

    entry_2F = Entry(
        bd=0,
        bg="#ECECEC",
        fg="#000716",
        highlightthickness=0
    )
    entry_2F.place(
        x=54.0,
        y=149.0,
        width=239.0,
        height=23.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assetsForget("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        236.5,
        217.5,
        image=entry_image_3
    )

    global entry_3F

    entry_3F = Entry(
        bd=0,
        bg="#ECECEC",
        fg="#000716",
        highlightthickness=0
    )
    entry_3F.place(
        x=54.0,
        y=207.0,
        width=365.0,
        height=23.0
    )

    canvas.create_text(
        51.0,
        77.0,
        anchor="nw",
        text="Username",
        fill="#000000",
        font=("RobotoRoman Light", 13 * -1)
    )

    canvas.create_text(
        51.0,
        131.0,
        anchor="nw",
        text="Email",
        fill="#000000",
        font=("RobotoRoman Light", 13 * -1)
    )

    canvas.create_text(
        51.0,
        188.0,
        anchor="nw",
        text="Additional Information for further assist.  [OPTIONAL]",
        fill="#000000",
        font=("RobotoRoman Light", 13 * -1)
    )

    canvas.create_text(
        77.0,
        46.0,
        anchor="nw",
        text="Reset here",
        fill="#000000",
        font=("RobotoRoman Regular", 13 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assetsForget("button_1.png"))

    global button_1F
    button_1F = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=create_Confirm,
        relief="flat"
    )
    button_1F.place(
        x=51.0,
        y=246.0,
        width=74.0,
        height=28.0
    )
    #window.resizable(False, False)
    window.mainloop()


def login_page():
    global user1 , username
    with open(r"assets\credentials\username.ini", 'r') as user1:
        username = user1.readlines()

    global pass1, password, PassChange
    with open(r"assets\credentials\password.ini", 'r') as pass1:
        password = pass1.readlines()

    global email, emailReset
    with open(r"assets\credentials\email.ini", 'r') as email:
        emailReset = email.readlines()

    window.title("Login")
    window.geometry("390x235")
    window.configure(bg="#FFFFFF")

    def login():
        Valid = False
        for i in range(0, len(username)):
            if entry_1.get() in username[i] and entry_2.get() in password[i]:
                Valid = True

        if Valid == True:
            messagebox.showinfo(title="Login Success", message="You successfully logged in.")
        else:
            messagebox.showerror(title="Error", message="Invalid login.")

    global canvas
    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=293,
        width=488,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        83.00002062320527,
        146.00003346955663,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        408.0,
        146.0,
        image=image_image_2
    )

    canvas.create_text(
        115.0,
        87.0,
        anchor="nw",
        text="Log in",
        fill="#000000",
        font=("RobotoRoman Bold", 28 * -1)
    )

    canvas.create_text(
        194.0,
        11.0,
        anchor="nw",
        text="MPSK",
        fill="#000000",
        font=("SourceSerifPro SemiBold", 35 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        247.5,
        158.5,
        image=entry_image_1
    )

    global entry_1

    entry_1 = Entry(
        bd=0,
        bg="#ECECEC",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=119.0,
        y=148.0,
        width=257.0,
        height=23.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        247.0,
        208.5,
        image=entry_image_2
    )

    global entry_2

    entry_2 = Entry(
        bd=0,
        bg="#ECECEC",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=118.0,
        y=198.0,
        width=258.0,
        height=23.0
    )

    canvas.create_text(
        116.0,
        128.0,
        anchor="nw",
        text="Username",
        fill="#000000",
        font=("RobotoRoman Light", 13 * -1)
    )

    canvas.create_text(
        115.0,
        177.0,
        anchor="nw",
        text="Password",
        fill="#000000",
        font=("RobotoRoman Light", 13 * -1)
    )

    canvas.create_text(
        147.0,
        54.0,
        anchor="nw",
        text="For IGCSE students, by an IGCSE student",
        fill="#000000",
        font=("SourceSerifPro SemiBold", 10 * -1)
    )

    canvas.create_rectangle(
        192.0,
        16.0,
        285.0,
        17.0,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        193.0,
        46.0,
        288.0,
        47.0,
        fill="#000000",
        outline="")

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))

    global button_1

    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=login,
        relief="flat"
    )
    button_1.place(
        x=173.0,
        y=250.0,
        width=67.16618347167969,
        height=25.6678466796875
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))

    global button_2

    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=Create_Acc,
        relief="flat"
    )
    button_2.place(
        x=244.0,
        y=257.0,
        width=70.0,
        height=12.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))

    global button_3

    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=create_Forget_Pass,
        relief="flat"
    )
    button_3.place(
        x=311.0,
        y=225.0,
        width=68.0,
        height=10.0
    )
    window.resizable(False, False)
    window.mainloop()

if __name__ == "__main__":
    login_page()
