import tkinter as tk
from login_panel import LoginPanel
from settings.config import *


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry(SCREEN_SIZE)
    root.title("Main Application")
    
    # Create an instance of LoginPanel and pack it into the root window
    app = LoginPanel(root)
    app.pack()
    
    root.mainloop()