from tkinter import *
import time
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0 # reps increments every time start_timer() is called for each phase (work, break or long break)

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_pomodoro():
    global reps
    reps = 0
    countdown(0) # immediately update the timer display to 00:00 when the reset button is pressed.
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# reps = 1 -> 25 min
# reps = 2 -> 5 min
# reps = 3 -> 25 min
# reps = 4 -> 5 min
# reps = 5 -> 25 min
# reps = 6 -> 5 min
# reps = 7 -> 25 min
# reps = 8 -> 15 min

# This function triggers the countdown process by calling the countdown function with the time in seconds
def start_timer():
    global reps # refer to global variable
    reps += 1 
    if reps % 8 == 0: # handles de long break after every 8 phases. It ensures the timer to continue indefinitely.
        countdown(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
    else:
        countdown(WORK_MIN * 60)
    
# ---------------------------- 2.COUNTDOWN MECHANISM ------------------------------- # 
# Create a timer
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min == 0:
        count_min = f"0{count_min}"
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}") # updates the text on the canvas (widget) with the formatted time.
    
    # Recursive Call: If count is greater than 0, the function schedules another call to countdown after 1000 milliseconds (1 second) with the decremented count.
    if count > 0: 
        window.after(1000, countdown, count - 1)

# ---------------------------- 1.UI SETUP ------------------------------- #
# Window configuration
window = Tk()  # Initializes the main window
window.title("Pomodoro")  # Sets the title of the window
window.config(padx=100, pady=50, bg=YELLOW)  # Configures padding of the content and background color for window

# Timer label
miles_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=("Arial", 48))
miles_label.grid(column=1, row=0)

# Canvas storage for image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # Creates the canvas with specified dimensions and color
tomato_img = PhotoImage(file="tomato.png")  # Loads the tomato image
canvas.create_image(100, 112, image=tomato_img)  # Places the image on the canvas
timer_text = canvas.create_text(100, 128, text="00:00", fill="white", font=(FONT_NAME, 36, "bold"))  # 'timer_text' as a variable that allows to access it and update its text with the countdown time
canvas.grid(column=1, row=1)  # Displays the canvas in the window

# Configuration for buttons
button1 = Button(text="Start", font=("Arial", 16, "bold"), command=start_timer)
button1.grid(column=0, row=2)
button2 = Button(text="Reset", font=("Arial", 16, "bold"), command=reset_pomodoro)
button2.grid(column=2, row=2)

# Checklist label
miles_label = Label(text="✔", fg=GREEN, bg=YELLOW, font=("Arial", 32))
miles_label.grid(column=1, row=3)

# Keep the window open. This line of code has to be at the end of the script
window.mainloop()  # Starts the Tkinter event loop