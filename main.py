#!/home/pi/Python/base/bin/python 

# above is the path of the virtual environment

import tkinter as tk
from tkinter import ttk
from settings.config import *
import os
from login_panel import LoginPanel


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry(SCREEN_SIZE)
    style = ttk.Style(root)

    # build the path to the theme file
    theme_path = os.path.join("/home/pi/Python/SMART_VAULT", "theme", "forest-light.tcl")

    root.tk.call("source", theme_path)
    style.theme_use("forest-light")
    
    # Create an instance of LoginPanel and pack it into the root window
    app = LoginPanel(root)
    app.pack()

    app.update_datetime()
    
    root.mainloop()