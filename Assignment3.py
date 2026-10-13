# Program Name: Assignment3.py
# Student Name: Julien McDaniel
# Assignment Number: Lab 3
# Due Date: 10/12/2026
# Purpose: This program opens a window that changes Miles per Gallon into
#          Kilometers per Liter. The answer updates while the user types.
#          Blank boxes and letters do not crash the program.

import tkinter as tk

# Runs every time a key is let go in the box
def update(event):
    try:
        km = float(box.get()) * 0.425143707
        answer.config(text=str(round(km, 2)) + " km/L")
    except ValueError:
        # Covers a blank box or letters
        answer.config(text="Type a number")

# Set up the window
win = tk.Tk()
win.title("Gas Mileage Converter")

# Label, typing box, and answer stacked top to bottom
tk.Label(win, text="Enter MPG:").pack(pady=5)
box = tk.Entry(win)
box.pack(padx=40)
answer = tk.Label(win, text="Type a number", fg="blue")
answer.pack(pady=10)

# Check the box after every key press
box.bind("<KeyRelease>", update)

win.mainloop()
