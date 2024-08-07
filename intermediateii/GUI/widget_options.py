# In Tkinter widgets we have 2 groups of options:
# Standard Options: list of options that are common to many widgets
# Widget specific Options: the options of that particular widget

import tkinter

# Create a new GUI
root = tkinter.Tk()
root.title("Python GUI")
root.minsize(600,400)

# Setting Options
# Options control the features of the widget. They can be set in 3 ways:
my_label = tkinter.Label(root, text='This is a label', font=("Arial", 18, "italic"))

my_label["fg"] = 'white'
my_label["bg"] = 'black' # After object creation, treating the option like a dictionary index

my_label.config(padx=50, pady=50, relief="raised", borderwidth=5) #Use .config method to update multiple attributes

my_label.pack()

# Buttons (Event listener)
# For getting the button widget to work, we can create a function that tells the button what to do and attach the function to a event listener

# Define the action for the button click
def clicking_btn():
    # This function is called when the "Click Here" button is clicked
    print("You just clicked the button")
    my_label["text"]='Button got clicked' # or mylabel.config(text="Button got clicked")

def entry_to_label():
    # This function is called when the "Replace Label" button is clicked
    # It retrieves the text from the entry widget and updates the label
    my_label["text"]= input.get()
    pass

# Create the entry widget for inputs
input = tkinter.Entry(width=40)
input.get() # return the input as a string
input.pack(pady=10)
    
# Create the button widget and attach the event listener
click_button = tkinter.Button(root, text="Click Here", command=clicking_btn)
click_button.pack()

entry_button = tkinter.Button(root, text='Replace label', command=entry_to_label)
entry_button.pack()

# Keep the window open. This line of code has to be at the end of the script
root.mainloop()