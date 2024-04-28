import tkinter as tk
from tkinter import messagebox

def confirm_exit():
    result = messagebox.askokcancel("Confirmation", "Are you sure you want to exit?")
    # returns true if user presses OK
    return result

def confirm_pickup():
    result = messagebox.askyesno("Confirm Pickup", "Are you sure you want to confirm the pickup?")
    # returns true if user presses Yes
    return result


if __name__ == "__main__":
    root = tk.Tk()

    exit_button = tk.Button(root, text="Exit", command=confirm_exit)
    exit_button.pack(pady=20)

    pickup_button = tk.Button(root, text="Confirm Pickup", command=confirm_pickup)
    pickup_button.pack(pady=20)

    root.mainloop()