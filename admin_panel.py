import tkinter as tk
from tkinter import ttk
import os
from gui_components.widgets import msgbox
from gui_components.widgets.treeview import TreeView
from gui_components.widgets.buttons import ExitButton
from gui_components.frames.nav_bar import NavBar
from gui_components.frames.admin_panel_frames import *
from services import database
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

        self.side_menu = tk.Frame(self.main_container, width=200, height=430, bg="#00563B")
        self.side_menu.pack_propagate(False)
        self.side_menu.grid(row=0, column=0)

        self.btns_container = tk.Frame(self.side_menu, bg="#00563B")
        self.btns_container.pack(pady=(120, 0))

        emp_man_btn = tk.Button(self.btns_container, text="Employee Management", bg="#00563B", fg="white", relief='flat', highlightbackground="#00563B", width=200)
        emp_man_btn.pack()

        inv_man_btn = tk.Button(self.btns_container, text="Inventory Management", bg="#00563B", fg="white", relief='flat', highlightbackground="#00563B", width=200)
        inv_man_btn.pack()

        ip_man_btn = tk.Button(self.btns_container, text="Item Placement Management", bg="#00563B", fg="white", relief='flat', highlightbackground="#00563B", width=200)
        ip_man_btn.pack()

        ts_btn = tk.Button(self.btns_container, text="Trouble Shooting", bg="#00563B", fg="white", relief='flat', highlightbackground="#00563B", width=200)
        ts_btn.pack()

        self.frame_container = tk.Frame(self.main_container, bg="#E8E9EB", width=600, height=430)
        self.frame_container.pack_propagate(False)
        self.frame_container.grid(row=0, column=1)

        self.emp_man_frame = EmployeeManagement(self.frame_container)
        self.emp_man_frame.add_btn.config(command=self.add_user)
        self.emp_man_frame.pack()

        # create tree view to display the list of users
        # Create a frame to pack the cart treeview
        self.user_treeview_frame = tk.Frame(self.emp_man_frame)
        self.user_treeview_frame.pack()

        self.user_treeview = TreeView(self.user_treeview_frame, height=9)

        # Create columns
        self.user_treeview["columns"] = ("ID", "User Name", "UID", "Role")
        self.user_treeview.column("#0", width=0, stretch=tk.NO)  # Hide the cart_tree column
        self.user_treeview.column("ID", width=40, anchor=tk.CENTER)
        self.user_treeview.column("User Name", width=200, anchor=tk.W)
        self.user_treeview.column("UID", width=150, anchor=tk.W)
        self.user_treeview.column("Role", width=70, anchor=tk.CENTER)

        # Create headings
        self.user_treeview.heading("ID", text="ID")
        self.user_treeview.heading("User Name", text="User Name", anchor=tk.W)
        self.user_treeview.heading("UID", text="UID", anchor=tk.W)
        self.user_treeview.heading("Role", text="Role", anchor=tk.CENTER)

        self.show_user_info()

        # remove button
        self.remove_btn = tk.Button(self.emp_man_frame, text="Remove", command=self.remove_user)
        self.remove_btn.pack()

    def exit(self):
        if msgbox.confirm_exit():
            self.root.destroy()

    def switch_frame(self, frame):
        for widget in self.frame_container.winfo_children():
            widget.forget()
        frame.pack()

    def update_datetime(self):
        self.nav_bar.update_datetime()

    def add_user(self):
        name = self.emp_man_frame.name_entry.get()
        uid = self.emp_man_frame.uid_entry.get()
        role = self.emp_man_frame.role_var.get()
        self.employee_details = [name, uid, role]
        # check for integrity and add the data to database
        success, message = database.add_user(self.employee_details[0], self.employee_details[1], self.employee_details[2])
        if success:
            msgbox.show_success_message_box(message)
        else:
            msgbox.show_error_message_box("Error", message)
        # show the updated list
        self.show_user_info()

    def delete_treeview_items(self, treeview):
        for item in treeview.get_children():
            treeview.delete(item)

    def show_user_info(self):
        self.delete_treeview_items(self.user_treeview)
        # get the user data from database
        user_data = database.get_user_details()
        # insert all user data in the user Treeview
        for i, item in enumerate(user_data, start=1):
            if i % 2 == 0:
                self.user_treeview.insert("", "end", values=(f"{item[0]}", f"{item[1]}", f"{item[2]}", f"{'Admin 'if item[3] == 1 else 'Employee'}"), tags=('evenrow',))
            else:
                self.user_treeview.insert("", "end", values=(f"{item[0]}", f"{item[1]}", f"{item[2]}", f"{'Admin 'if item[3] == 1 else 'Employee'}"), tags=('oddrow',))

    def remove_user(self):
        # remove the selected user and update the treeview
        selected_item = self.user_treeview.focus()
        if selected_item:
            item_values = self.user_treeview.item(selected_item, 'values')
            # get the id of the user
            user_id = item_values[0]
            if msgbox.confirm_remove_user():
                database.remove_user_by_id(user_id)
            else:
                pass
        # show the updated list
        self.show_user_info()


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