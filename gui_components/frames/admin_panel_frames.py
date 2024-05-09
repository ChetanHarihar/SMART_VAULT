import tkinter as tk
from tkinter import ttk
import os

class EmployeeManagement(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(bg="#E8E9EB", width=600, height=430)
        self.pack_propagate(False)
        self.init_ui()

    def init_ui(self):
        self.label_frame = tk.LabelFrame(self, text="Add User", width=590, height=130)
        self.label_frame.pack_propagate(False)
        self.label_frame.pack()

        self.add_emp_frame = tk.Frame(self.label_frame)
        self.add_emp_frame.pack()

        # Labels
        self.name_label = tk.Label(self.add_emp_frame, text="Name:")
        self.name_label.grid(row=0, column=0, sticky="w")
        self.uid_label = tk.Label(self.add_emp_frame, text="UID:")
        self.uid_label.grid(row=1, column=0, sticky="w")

        # Entry Boxes
        self.name_entry = tk.Entry(self.add_emp_frame, width=25)
        self.name_entry.grid(row=0, column=1)
        self.uid_entry = tk.Entry(self.add_emp_frame, width=25)
        self.uid_entry.grid(row=1, column=1)

        # Radio Button
        self.role_var = tk.IntVar()
        self.admin_btn = tk.Radiobutton(self.add_emp_frame, text="Admin", variable=self.role_var, value=1)
        self.admin_btn.grid(row=2, column=0, sticky="w")
        self.employee_btn = tk.Radiobutton(self.add_emp_frame, text="Employee", variable=self.role_var, value=2)
        self.employee_btn.grid(row=2, column=1, sticky="w")
        self.role_var.set(1)

        # Buttons
        self.clear_btn = tk.Button(self.add_emp_frame, text="Clear", command=self.clear_fields)
        self.clear_btn.grid(row=3, column=0, padx=5, pady=5)
        self.add_btn = tk.Button(self.add_emp_frame, text="Add", command=self.add_user, state="disabled")
        self.add_btn.grid(row=3, column=1, padx=5, pady=5)

        # Bind events to Entry fields
        self.name_entry.bind("<KeyRelease>", self.validate_input)
        self.uid_entry.bind("<KeyRelease>", self.validate_input)

    def validate_input(self, event=None):
        name = self.name_entry.get()
        uid = self.uid_entry.get()
        
        if name and uid:
            self.add_btn.config(state="normal")
        else:
            self.add_btn.config(state="disabled")

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.uid_entry.delete(0, tk.END)
        self.validate_input()

    def add_user(self):
        name = self.name_entry.get()
        uid = self.uid_entry.get()
        role = self.role_var.get()
        employee_details = [name, uid, role]
        print("User details:", employee_details)


class InventoryManagement(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(bg="#E8E9EB", width=600, height=430)
        self.pack_propagate(False)
        self.init_ui()

    def init_ui(self):
        pass

# If this file is run directly for testing purposes
if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style(root)

    # build the path to the theme file
    theme_path = os.path.join("/home/pi/Python/SMART_VAULT", "theme", "forest-light.tcl")

    root.tk.call("source", theme_path)
    style.theme_use("forest-light")
    
    main_frame = InventoryManagement(root)
    main_frame.pack()
    
    root.mainloop()