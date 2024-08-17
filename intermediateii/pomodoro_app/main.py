from tkinter import *
import time
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 10
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0 # reps increments every time start_timer() is called for each phase (work, break or long break)
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_pomodoro():
    global reps, timer
    reps = 0
    window.after_cancel(timer)
    label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text="", fg=GREEN)

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
        label.config(text="Rest", fg=PINK)
        countdown(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        label.config(text="Break", fg=RED)
        countdown(SHORT_BREAK_MIN)    
    else:
        label.config(text="Work", fg=GREEN)
        countdown(WORK_MIN)
    
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
        global timer 
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer() # each time the phase finishes, it calls the start_timer function once again, so it wont stop.
        global reps
        if reps % 2 == 0:
            checkmark_text = checkmark_label.cget("text")  # Get the current text in the label
            checkmark_label.config(text=checkmark_text + "✔")  # Append a checkmark

# ---------------------------- 1.UI SETUP ------------------------------- #
# Window configuration
window = Tk()  # Initializes the main window
window.title("Pomodoro")  # Sets the title of the window
window.config(padx=100, pady=50, bg=YELLOW)  # Configures padding of the content and background color for window

# Timer label
label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=("Arial", 48))
label.grid(column=1, row=0)

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
checkmark_label = Label(text="",fg=GREEN, bg=YELLOW, font=("Arial", 32))
checkmark_label.grid(column=1, row=3)

# Keep the window open. This line of code has to be at the end of the script
window.mainloop()  # Starts the Tkinter event loop