from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- 1.UI SETUP ------------------------------- #
# Window configuration
window = Tk()  # Initializes the main window
window.title("Pomodoro")  # Sets the title of the window
window.config(padx=100, pady=50, bg=YELLOW)  # Configures padding and background color

# Timer label
miles_label = Label(text="Timer", font=("Arial", 48))
miles_label.grid(column=1, row=0)

# Canvas storage for image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # Creates the canvas with specified dimensions and color
tomato_img = PhotoImage(file="tomato.png")  # Loads the tomato image
canvas.create_image(100, 112, image=tomato_img)  # Places the image on the canvas
canvas.create_text(100, 128, text="00:00", fill="white", font=(FONT_NAME, 36, "bold"))  # Adds text to the canvas
canvas.grid(column=1, row=1)  # Displays the canvas in the window

# Buttons
def actionbtn1():
    print("Do something")
    
def actionbtn2():
    print("Do something")

# Configuration for buttons
button = Button(text="Start", command=actionbtn1)
button.grid(column=0, row=2)
button = Button(text="Reset", command=actionbtn2)
button.grid(column=2, row=2)

# Checklist label
miles_label = Label(text="✔", font=("Arial", 32))
miles_label.grid(column=1, row=3)

# Keep the window open. This line of code has to be at the end of the script
window.mainloop()  # Starts the Tkinter event loop