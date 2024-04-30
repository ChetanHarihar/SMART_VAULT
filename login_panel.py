import tkinter as tk
from gui_components.widgets.buttons import RoleButton  
from gui_components.frames.login_frame import LoginPage
from gui_components.frames.scan_frames import ScanFrame
from gui_components.frames.scan_frames import ResultFrame
from services.rfid_module import scan_rfid, check_scan_result
import threading
import queue

class LoginPanel(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(width=800, height=480)
        self.role = None
        self.scan_data = queue.Queue()
        self.user_data = None
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

        self.success_frame = ResultFrame(self, result=1)
        self.failed_frame = ResultFrame(self, result=0)
    
    def set_role(self, role):
        if role == "employee":
            self.role = 2
        elif role == "admin":
            self.role = 1
        self.scan_and_validate()

    def scan_and_validate(self):
        self.login_frame.pack_forget()
        self.scan_frame = ScanFrame(self)
        self.scan_frame.pack()

        # Creating and starting the RFID scanning thread
        scan_thread = threading.Thread(target=self.scan_and_handle_result)
        scan_thread.start()

    def scan_and_handle_result(self):
        scan_rfid(self.scan_data)  # Perform RFID scanning
        
        # Get the result after scanning
        result = check_scan_result(q=self.scan_data, role=self.role)

        # Handle the result
        self.handle_scan_result(result)

    def handle_scan_result(self, result):
        if result:
            self.scan_frame.pack_forget()
            self.success_frame.pack()
            # Display the employee or admin panel
        else:
            self.scan_frame.pack_forget()
            self.failed_frame.pack()
            # Restart scan after 5 seconds
            self.after(5000, self.restart_scan)

    def restart_scan(self):
        self.failed_frame.pack_forget()
        self.login_frame.pack()  # Display login frame again


# If this file is run directly for testing purposes
if __name__ == "__main__":
    root = tk.Tk()
    
    # Create an instance of LoginPage and pack it into the root window
    main_frame = LoginPanel(root)
    main_frame.pack()
    
    root.mainloop()