"""
This is a GUI chat window which creates server and client windows
We use tkinter module to create a GUI with buttons which redirects 
to python terminal.

> Author: Team-3
"""

# Import necessary libraries
import tkinter as tk
from tkinter import *
import subprocess

# Create tkinter object
main = tk.Tk()

# Name the window
main.title("Chat Application")

# Set the dimensions
main.geometry("300x250+500+150")

# Set icon
main.iconbitmap("./images/icon.ico")

# Do not allow window resizing
main.resizable(width=False, height=False)

# Load background image and set it
background_image = PhotoImage(file="./images/bg.png")
background = Label(main, image=background_image,bd=-1)
background.place(x=0, y=0)

# Define client process
def start_client():
    subprocess.call('start client.py', shell=True)

# Define server process
def start_server():
    subprocess.call('start server.py', shell=True)

# Create a button to start server
btn = tk.Button(main, text ="Start server", height=2, width=10, command = start_server)
btn.grid(row=1, column=0, pady=100, padx = 38)

# Create a button to start client
btn = tk.Button(main, text ="Start new client",  height=2, width=14, command = start_client)
btn.grid(row=1, column=1, pady=100, padx = 0)

# Run the app until user exits
main.mainloop()