# Import libraries
from tkinter import *
import os
import random
import string
import json
from tkinter import messagebox # Allows to use popups

# Json format is the most popular structure for transferring data. Its similar to dictionaries.
# Json is composed of a list of nested dictionaries with the key: value data structure.

# ---------------------------- 2. PASSWORD GENERATOR ------------------------------- #
def pass_generator():
    # List of charaters that will componse the passwords
    character_list = string.ascii_letters + string.punctuation + string.digits

    # Define the passwd lenght
    pass_len = random.randint(16,20)

    # Generate the passwd using list comprehension
    password = ''.join(random.choice(character_list) for _ in range(pass_len))

    passwd_entry.delete(0, END)  # Clear the entry widget
    passwd_entry.insert(0, password)  # Insert the generated password

    
# ---------------------------- 3. SAVE PASSWORD ------------------------------- #

# Path of the JSON file.
data_file = "./intermediateiii/json_password_managerii/pswd_manager.json"

def test():
    # Get the values of the entries
    website_str = website_entry.get()
    email_str = email_entry.get()
    psswd_str = passwd_entry.get()

    new_record = {
        website_str: {
            "email": email_str,
            "password": psswd_str}
    }

    try:
        # Read JSON data
        with open(data_file, "r") as f:
            # 1. Reading current data
            data = json.load(f)  # Loads JSON data into a Python dict

    except (FileNotFoundError, json.JSONDecodeError):
        # If the file doesn't exist or is empty/corrupt, create a new file in write mode and store the first record
        with open(data_file, "w") as f:
            json.dump(new_record, f, indent=4)

    else:
        # 2. Update the python dict with new data
        data.update(new_record)

        with open(data_file,"w") as f:
            # 3. Saving the data
            json.dump(data, f, indent=4) # Allow me to store JSON UPDATED data directly into a file.
            # indent=4 creates indentation for better readability

    finally:
        # Clear the already saved content of the widgets
        website_entry.delete(0, END)
        email_entry.delete(0, END)
        passwd_entry.delete(0, END)

# ---------------------------- 4. SEARCH DATA ------------------------------- #

def find_password():
    # Get the value from the website account
    search = website_entry.get()

    if len(search) == 0:
        messagebox.showwarning(title="Warning", message="Missing information. Please complete it.")
    else:
        # Read JSON data
        with open(data_file, "r") as f:
        # Reading current data
            dict = json.load(f)  # Loads JSON data into a Python dict
            
            if search in dict:
                email = dict[search]["email"]
                psswd = dict[search]["password"]
                
                # Info message
                messagebox.showinfo(title=f"search", message=f"Email: {email} \nPassword: {psswd}")
            else:
                print("No data")

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
website_entry.grid(row=1, column=1)

email_entry = Entry(width=35)
email_entry.insert(0, "user@example.com") # 0,'end' refers to the position where the text will be inserted
email_entry.grid(row=2, column=1, columnspan=2)

passwd_entry = Entry(width=21)
passwd_entry.grid(row=3, column=1, columnspan=2)

# Buttons
add_btn = Button(text="Add", width=36, command=test)
add_btn.grid(row=4, column=1, columnspan=3)

genpass_btn = Button(text="Generate Password", command=pass_generator)
genpass_btn.grid(row=3, column=3)

search_btn = Button(text='Search', command=find_password)
search_btn.grid(row=1, column=3)

window.mainloop()