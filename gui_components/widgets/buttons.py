import tkinter as tk
from PIL import Image, ImageTk

class RoleButton(tk.Button):
    # Load and resize images for admin and employee roles
    emp = Image.open('/home/pi/Python/SMART_VAULT/assets/employee.png').resize((100, 100))
    admin = Image.open('/home/pi/Python/SMART_VAULT/assets/admin.png').resize((100, 100))

    def __init__(self, master=None, role=None, command=None, **kwargs):
        super().__init__(master, **kwargs)

        # Convert images to PhotoImage and store them as attributes
        self.emp_image = ImageTk.PhotoImage(RoleButton.emp)
        self.admin_image = ImageTk.PhotoImage(RoleButton.admin)

        if role == 'admin':
            self.config(image=self.admin_image, borderwidth=0, background="white", activebackground="white",command=command)
        elif role == 'employee':
            self.config(image=self.emp_image, borderwidth=0, bg="white", activebackground="white", command=command)


class ExitButton(tk.Button):
    # Load and resize exit image
    exit = Image.open('/home/pi/Python/SMART_VAULT/assets/exit_button.png').resize((25, 25))

    def __init__(self, master=None, command=None,**kwargs):
        super().__init__(master, **kwargs)

        # Convert images to PhotoImage and configure
        self.exit_image = ImageTk.PhotoImage(ExitButton.exit)
        self.config(image=self.exit_image, borderwidth=0, bg="white", activebackground="white", command=command)


if __name__ == "__main__":

    root = tk.Tk()

    # Create a RoleButton 
    admin_btn = RoleButton(root, role='admin')
    admin_btn.pack()

    # Create a RoleButton 
    emp_btn = RoleButton(root, role='employee')
    emp_btn.pack()

    # Create a ExitButton
    exit_btn = ExitButton(root)
    exit_btn.pack()

    root.mainloop()