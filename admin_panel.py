import tkinter as tk
from tkinter import ttk
import os
from gui_components.widgets import msgbox
from gui_components.widgets.buttons import ExitButton
from gui_components.widgets.treeview import TreeView
from gui_components.frames.nav_bar import NavBar
from settings.config import *


class AdminPanel(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(width=800, height=480)
        self.root = master
        self.init_ui()

    def init_ui(self):
        # create and pack nav_bar frame
        self.nav_bar = NavBar(self)
        self.nav_bar.pack(padx=(2.5, 2.5), pady=(5,2.5))
    
        # Create and pack exit button
        self.exit_btn = ExitButton(self.nav_bar, activebackground="white", command=self.exit)
        self.exit_btn.pack(side=tk.LEFT, padx=(10, 0))

        # user info label
        self.user_label = tk.Label(self.nav_bar, text=f"Logged in as: ", font=('times new roman', 12, 'bold'), bg="white")
        self.user_label.pack(side=tk.LEFT, padx=(20, 0))

        # Create and pack frame container
        self.main_container = tk.Frame(self, width=800, height=430)
        self.main_container.pack_propagate(False)
        self.main_container.pack(padx=(2.5, 2.5), pady=(2.5,5))

        self.side_menu = tk.Frame(self.main_container, width=200, height=480, bg="#00563B")
        self.side_menu.pack_propagate(False)
        self.side_menu.grid(row=0, column=0)

        self.frame_container = tk.Frame(self.main_container, bg="#E8E9EB", width=600, height=480)
        self.frame_container.pack_propagate(False)
        self.frame_container.grid(row=0, column=1)

    def exit(self):
        if msgbox.confirm_exit():
            self.root.destroy()

    def update_datetime(self):
        self.nav_bar.update_datetime()


# If this file is run directly for testing purposes
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry(SCREEN_SIZE)
    style = ttk.Style(root)

    # build the path to the theme file
    theme_path = os.path.join("/home/pi/Python/SMART_VAULT", "theme", "forest-light.tcl")

    root.tk.call("source", theme_path)
    style.theme_use("forest-light")
    
    # Create an instance of EmployeePanel and pack it into the root window
    main_frame = AdminPanel(root)
    main_frame.pack()

    main_frame.update_datetime()
    
    root.mainloop()