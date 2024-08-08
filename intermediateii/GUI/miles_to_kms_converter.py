# Create a GUI window for a converter from miles to kilometers

from tkinter import *

# Define the action for the button click
def calculate():
    output_label["text"]= str(round(float(input.get()) * 1.6, 2))

window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Entry
input = Entry(width=10)
input.get()
input.grid(column=1, row=0)

# Miles label
miles_label = Label(text="Miles", font=("Arial", 18))
miles_label.grid(column=2, row=0)

# equal_to label
equal_to_label = Label(text="is equal to", font=("Arial", 18))
equal_to_label.grid(column=0, row=1)

# output label
output_label = Label(text="0", font=("Arial", 18))
output_label.grid(column=1, row=1)

# kms label
kms_label = Label(text="kms", font=("Arial", 18))
kms_label.grid(column=2, row=1)

#Button
button = Button(text="Calculate", font=("Arial", 14), command=calculate)
button.grid(column=1, row=2)

window.mainloop()