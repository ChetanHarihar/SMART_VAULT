
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("800x480")

style = ttk.Style(root)
root.tk.call("source", "forest-light.tcl")
style.theme_use("forest-light")


def switch_page(page):
    for widget in frame_container.winfo_children():
        widget.forget()

    page.pack()


main_frame = tk.Frame(root, width=800, height=480, bg="#E8E9EB")
main_frame.pack_propagate(False)
main_frame.pack()

sidebar = tk.Frame(main_frame, width=200, height=480, bg="#00563B")
sidebar.pack_propagate(False)
sidebar.grid(row=0, column=0)

exit_btn = tk.Button(sidebar, text="Exit", relief="flat")
exit_btn.pack(pady=(10, 0))

btn_container = tk.Frame(sidebar)
btn_container.pack(pady=(100, 0))

btn1 = tk.Button(btn_container, text="Inventory Management", relief='flat', command=lambda: switch_page(frame1))
btn1.pack()
btn2 = tk.Button(btn_container, text="Employee Management", relief='flat', command=lambda: switch_page(frame2))
btn2.pack()
btn3 = tk.Button(btn_container, text="Item Placement Management", relief='flat', command=lambda: switch_page(frame3))
btn3.pack()
btn4 = tk.Button(btn_container, text="Record Viewing", relief='flat', command=lambda: switch_page(frame4))
btn4.pack()
btn5 = tk.Button(btn_container, text="Trouble Shooting", relief='flat', command=lambda: switch_page(frame5))
btn5.pack()

frame_container = tk.Frame(main_frame, bg="#E8E9EB", width=600, height=480)
frame_container.pack_propagate(False)
frame_container.grid(row=0, column=1)

frame1 = tk.Frame(frame_container, bg="#E8E9EB", width=600, height=480)
frame1.pack_propagate(False)
frame1.pack()

label1 = tk.Label(frame1, text="Inventory Management")
label1.pack()


frame2 = tk.Frame(frame_container, bg="#E8E9EB", width=600, height=480)
frame2.pack_propagate(False)

label2 = tk.Label(frame2, text="Employee Management")
label2.pack()


frame3 = tk.Frame(frame_container, bg="#E8E9EB", width=600, height=480)
frame3.pack_propagate(False)

label3 = tk.Label(frame3, text="Item Placement Management")
label3.pack()


frame4 = tk.Frame(frame_container, bg="#E8E9EB", width=600, height=480)
frame4.pack_propagate(False)

label4 = tk.Label(frame4, text="Record Viewing")
label4.pack()


frame5 = tk.Frame(frame_container, bg="#E8E9EB", width=600, height=480)
frame5.pack_propagate(False)

label5 = tk.Label(frame5, text="Trouble Shooting")
label5.pack()

root.mainloop()