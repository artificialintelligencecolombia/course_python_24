import tkinter as tk

# Window setup
window = tk.Tk()
window.title("Flashy")
window.config(bg='#b1d9c4', padx=50, pady=50)

# Canvas (card area) creation
canvas = tk.Canvas(window, width=800, height=526, bg='#b1d9c4', highlightthickness=0)  # Card background area
card_front_image = tk.PhotoImage(file='./images/card_front.png')  # Card image
canvas.create_image(400, 263, image=card_front_image)  # Center card image
canvas.grid(row=0, column=0, columnspan=2)  # Place canvas

# Text on canvas (inside the card)
canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"), fill="black")  # Top label
canvas.create_text(400, 263, text="trouve", font=("Arial", 60, "bold"), fill="black")  # Centered label

# Buttons outside the card
left_button = tk.Button(window, text="❌", font=("Arial", 30))  # Left button
left_button.grid(row=1, column=0, padx=50, pady=50)

right_button = tk.Button(window, text="✅", font=("Arial", 30))  # Right button
right_button.grid(row=1, column=1, padx=50, pady=50)

# Main loop to display window
window.mainloop()
