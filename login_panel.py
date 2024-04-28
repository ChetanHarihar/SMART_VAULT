import tkinter as tk
from gui_components.widgets.buttons import RoleButton  
from gui_components.frames.scan_frames import ScanFrame
from gui_components.frames.login_frame import LoginPage
import queue

class LoginPanel(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(width=800, height=480)
        self.role = None
        self.scan_data = queue.Queue()
        self.init_ui()

    def init_ui(self):
        # create and pack login frame
        self.login_frame = LoginPage(self)
        self.login_frame.pack()

        # Create and pack button container
        self.btn_container = tk.Frame(self.login_frame, bg="white")
        self.btn_container.pack()

        # Create and pack employee and admin buttons using RoleButton class
        self.employee_btn = RoleButton(self.btn_container, role="employee", command= lambda: self.set_role("employee"))
        self.employee_btn.pack(side=tk.LEFT, padx=(0, 50))
        self.admin_btn = RoleButton(self.btn_container, role="admin", command= lambda: self.set_role("admin"))
        self.admin_btn.pack(side=tk.RIGHT, padx=(50, 0))
    
    def set_role(self, role):
        if role == "employee":
            self.role = 2
        elif role == "admin":
            self.role = 1
        self.scan_frame()

    def scan_frame(self):
        self.login_frame.pack_forget()
        self.scan_frame = ScanFrame(self)
        self.scan_frame.pack()

    def start_scan(self):
        pass

    def check_scan_result(self, scan_data):
        pass


# If this file is run directly for testing purposes
if __name__ == "__main__":
    root = tk.Tk()
    
    # Create an instance of LoginPage and pack it into the root window
    main_frame = LoginPanel(root)
    main_frame.pack()
    
    root.mainloop()