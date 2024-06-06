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

def confirm_remove_user():
    result = messagebox.askokcancel("Confirmation", "Are you sure you want to remove the User?")
    # returns true if user presses OK
    return result

def confirm_remove_category():
    result = messagebox.askokcancel("Confirmation", "Are you sure you want to remove the Category?")
    # returns true if user presses OK
    return result

def confirm_remove_item():
    result = messagebox.askokcancel("Confirmation", "Are you sure you want to remove the Item?")
    # returns true if user presses OK
    return result

def confirm_item_restock():
    result = messagebox.askokcancel("Confirmation", "Are the Items added, confirm restock?")
    # returns true if user presses OK
    return result

def confirm_remove_rack():
    result = messagebox.askokcancel("Confirmation", "Are you sure you want to remove the Rack?")
    # returns true if user presses OK
    return result

def confirm_remove_ip():
    result = messagebox.askokcancel("Confirmation", "Are you sure you want to remove the placed Item?")
    # returns true if user presses OK
    return result

def show_error_message_box(title, message):
    messagebox.showerror(title, message)

def show_success_message_box(message):
    messagebox.showinfo("Success", message)


if __name__ == "__main__":
    root = tk.Tk()

    exit_button = tk.Button(root, text="Exit", command=confirm_exit)
    exit_button.pack(pady=20)

    pickup_button = tk.Button(root, text="Confirm Pickup", command=confirm_pickup)
    pickup_button.pack(pady=20)

    remove_user = tk.Button(root, text="Remove user", command=confirm_remove_user)
    remove_user.pack(pady=20)

    root.mainloop()