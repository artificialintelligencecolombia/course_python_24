from tkinter import *
from tkinter import messagebox # Allows to use popups

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
# Creates the function that will store the data
def save():
    # Retrieve the current text from the Entry widget
    website_str = website_input.get() 
    email_str = usr_email.get()
    passwd_str = passwd_input.get()
    
    # Checks if there's missing information and pop ups a confirmation message
    if len(website_str) == 0 or len(passwd_str) == 0:
        messagebox.showwarning(title="Warning", message="Missing information. Please complete it.")
    else:
        is_ok = messagebox.askokcancel(title=f"{website_str}", message=f"Email: {email_str} \nPassword: {passwd_str} \n\n Click 'ok' to save.")
        if is_ok:
            # Opens the file and append the information in each line
            with open('data.txt', 'a') as f:
                f.write(f"{website_str} | {email_str} | {passwd_str} \n")
                f.close() # 'with open', f.close() is not necessary
                
            # Clear the content of the Entry widgets after saving the data
            website_input.delete(0, END)  # Clear the website input field
            usr_email.delete(0, END)      # Clear the email input field
            passwd_input.delete(0, END)   # Clear the password input field

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
website_input.focus() # automatically set the keyboard focus on the widget
website_input.grid(row=1, column=1, columnspan=2)

usr_email = Entry(width=35)
usr_email.insert(0, "@example.com") # 0,'end' refers to the position where the text will be inserted
usr_email.grid(row=2, column=1, columnspan=2)

passwd_input = Entry(width=21)
passwd_input.grid(row=3, column=1, sticky="w")

# Buttons
genpass_btn = Button(text="Generate Password")
genpass_btn.grid( row=3, column=2)

add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(row=4, column=1, columnspan=2)
 

# Keep the window open. This line of code has to be at the end of the script
window.mainloop()  # Starts the Tkinter event loop
