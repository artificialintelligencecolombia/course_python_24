from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

# Window configuration
window = Tk()  # Initializes the main window
window.title("Password Manager App")  # Sets the title of the window
window.config(padx=50, pady=50) # Adds padding around the window

# Canvas storage for image
canvas = Canvas(width=200, height=200)  # Creates the canvas with specified dimensions 
lock_img = PhotoImage(file="./logo.png")  # Loads the lock image from a file
canvas.create_image(100, 100, image=lock_img)  # Places the image at the center of the canvas
canvas.grid(row=0, column=1, columnspan=2)

# Labels
website = Label(text="Website:")
website.grid(row=1, column=0)

usr = Label(text="Email/Username:")
usr.grid(row=2, column=0)

passwd = Label(text="Password:")
passwd.grid(row=3, column=0)

# Entries
website_input = Entry(width=35)
print(website_input.get()) # Retrieves the current text from the Entry widget
website_input.grid(row=1, column=1, columnspan=2)

usr_input = Entry(width=35)
print(usr_input.get()) # Retrieves the current text from the Entry widget
usr_input.grid(row=2, column=1, columnspan=2)

passwd_input = Entry(width=21)
print(passwd_input.get()) # Retrieves the current text from the Entry widget
passwd_input.grid(row=3, column=1, sticky="w")

# Buttons
genpass_btn = Button(text="Generate Password")
genpass_btn.grid( row=3, column=2)

add_btn = Button(text="Add", width=36)
add_btn.grid(row=4, column=1, columnspan=2)
 

# Keep the window open. This line of code has to be at the end of the script
window.mainloop()  # Starts the Tkinter event loop
