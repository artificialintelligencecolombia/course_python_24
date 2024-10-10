from tkinter import *

GREEN = '#b1d9c4'
# ---------------------------- GUI ------------------------------- #

# Window configuration
window = Tk()  # Initializes the main window
window.title("Flashy")
window.config(bg=GREEN, padx=50, pady=50)

canvas = Canvas(window, width=800, height=526, bg= GREEN)
canvas.pack()  # Displays and centers the canvas in the window

card_front_image = PhotoImage(file='./images/card_front.png')  # Loads the lock image from a file
canvas.create_image(400,263, image=card_front_image)



# window.mainloop() is required to display the window
window.mainloop()