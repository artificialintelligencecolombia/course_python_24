# Import libraries
from tkinter import *
import os
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


# ---------------------------- 1.UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Password Generator 2.0")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


# Canvas widget for the image's storage
canvas = Canvas(width=200, height=200)

# Get the absolute path of the logo img
img_path = os.path.join(os.path.dirname(__file__), "logo.png") # Get the directory path of the current Python script file -> Concatenate it with the image file name "logo.png" to construct the full absolute path to the image file.
lock_img = PhotoImage(file=img_path) # Loads the image from a file
canvas.create_image(100,100, image=lock_img)
canvas.pack()

# Labels
website = Label(text="Website:")
website.pack()

email = Label(text="Email:")
email.pack()

passwd = Label(text="Password: ")
passwd.pack()

# Entries
website_entry = Entry()
website_entry.pack()

email_entry = Entry()
email_entry.pack()

passwd_entry = Entry()
passwd_entry.pack()

# Buttons
add_btn = Button(text="Add")
add_btn.pack()

genpass_btn = Button(text="Generate Password")
genpass_btn.pack()

window.mainloop()