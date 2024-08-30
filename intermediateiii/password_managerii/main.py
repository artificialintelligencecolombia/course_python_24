# Import libraries
from tkinter import *
import os
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- 2. SAVE PASSWORD ------------------------------- #

# Get the values of the entries
def test():
    website_str = website_entry.get()
    email_str = email_entry.get()
    psswd_str = passwd_entry.get()

    with open("./intermediateiii/password_managerii/pswd_manager.txt", "a") as f:
        f.write(f"{website_str} | {email_str} | {psswd_str}")

# ---------------------------- 1.UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Password Generator 2.0")
window.config(padx=20, pady=20)


# Canvas widget for the image's storage
canvas = Canvas(width=200, height=200)

# Get the absolute path of the logo img
img_path = os.path.join(os.path.dirname(__file__), "logo.png") # Get the directory path of the current Python script file -> Concatenate it with the image file name "logo.png" to construct the full absolute path to the image file.
lock_img = PhotoImage(file=img_path) # Loads the image from a file
canvas.create_image(100,100, image=lock_img)
canvas.grid(row=0, column=1, columnspan=2)

# Labels
website = Label(text="Website:")
website.grid(row=1, column=0)

email = Label(text="Email:")
email.grid(row=2, column=0)

passwd = Label(text="Password: ")
passwd.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)

passwd_entry = Entry(width=21)
passwd_entry.grid(row=3, column=1)

# Buttons
add_btn = Button(text="Add", width=36, command=test)
add_btn.grid(row=4, column=1, columnspan=2)

genpass_btn = Button(text="Generate Password")
genpass_btn.grid(row=3, column=2)

window.mainloop()