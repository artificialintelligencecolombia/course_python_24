# tkinter is alreday preinstalled in the python library

import tkinter

# Create a new window
root = tkinter.Tk()
root.title("My first GUI")
root.minsize(500,300) # (width,height) -> Set the initial size of the window. Still, we're able to maximize and scale the window size larger based on the content dimensions.

# Create a label
my_label = tkinter.Label(root, text="This is a Python GUI", font=('Calibri',18, 'normal'))
my_label.pack() # Add the widget to the window

my_button = tkinter.Button(root, text='Click me')
my_button.pack()  # .pack() method is primarily used for positioning, resizing and styling widgets within a parent container
# .pack() method in Tkinter does share some similarities with CSS in terms of layout and positioning.

# Keep the window open. This line of code has to be at the end of the script
root.mainloop()



# -> TKINTER COMPONENTS
# Root Window: The main window of your application
# root = tk.Tk()

# Frame: A container widget to group and organize other widgets
# frame = tk.Frame(root)

# Label: Displays text or an image
# label = tk.Label(root, text="This is a label")

# Button: A clickable button
# button = tk.Button(root, text="Click Me")

# Entry: A single-line text field
# entry = tk.Entry(root)

# Text: A multi-line text field
# text = tk.Text(root)

# Canvas: A widget for drawing shapes, images, or other complex layouts
# canvas = tk.Canvas(root)

# Listbox: A list from which a user can select one or more items
# listbox = tk.Listbox(root)

# Menu: A drop-down menu
# menu = tk.Menu(root)

# Menubutton: A button that, when clicked, shows a menu
# menubutton = tk.Menubutton(root, text="Menu")

# Scrollbar: Adds scrolling capability to other widgets
# scrollbar = tk.Scrollbar(root)

# Checkbutton: A checkbox that can be checked or unchecked
# checkbutton = tk.Checkbutton(root, text="Check Me")

# Radiobutton: A radio button for selecting one option from a set
# radiobutton = tk.Radiobutton(root, text="Option 1", value=1)

# Scale: A slider to select a numeric value
# scale = tk.Scale(root, from_=0, to=100)

# Spinbox: An entry widget with up/down arrows to select from a range of values
# spinbox = tk.Spinbox(root, from_=0, to=10)

# Message: A widget to display multiline text
# message = tk.Message(root, text="This is a message")

# Toplevel: A separate window on top of the main window
# toplevel = tk.Toplevel(root)

# PanedWindow: A container widget that can be split into resizable panes
# panedwindow = tk.PanedWindow(root)

# LabelFrame: A frame with a label that can contain other widgets
# labelframe = tk.LabelFrame(root, text="Label Frame")

# MessageBox: A pop-up dialog box for messages (usually imported from tkinter.messagebox)
# messagebox.showinfo("Title", "This is a message box")