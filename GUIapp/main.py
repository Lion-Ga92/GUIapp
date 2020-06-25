import tkinter as tk

from GUIapp.classes import GUIapp_pg2


def deal_with_clear():
    entry.delete(0, tk.END)
    entry_b.delete(0, tk.END)

def deal_with_login():

    if (name_entry == "Luis") and (pass_entry == "1234"):
        window.destroy()

    new_window()

window = tk.Tk()
window.title("Tamales LLC")
frame_A = tk.Frame(master=window, width=20, height=10)
frame_A.pack()

frame_b = tk.Frame(master=window, width=20, height=10)
frame_b.pack()

label_a = tk.Label(master=frame_A, text="Tamales Garcia", width=20, height=1)
label_a.pack()

label_b = tk.Label(master=frame_A, text="Welcome please sign in:", relief=tk.GROOVE, borderwidth=1)
label_b.pack()

label_c = tk.Label(master=frame_b, text="name:", width=8,  relief=tk.GROOVE, borderwidth=1)
label_c.grid(row=0, column=0)

entry = tk.Entry(master=frame_b, width=20, bg="pink", relief=tk.RAISED, borderwidth=2)
entry.grid(row=0, column=1)
name_entry = entry.get()

label_d = tk.Label(master=frame_b, text="password:", relief=tk.GROOVE, borderwidth=1)
label_d.grid(row=1, column=0)

entry_b = tk.Entry(master=frame_b, width=20, bg="pink", relief=tk.RAISED, borderwidth=2)
entry_b.grid(row=1, column=1)
pass_entry = entry_b.get()

button_a = tk.Button(master=frame_b, text="Log in", width=6, relief=tk.GROOVE, borderwidth=1, command=deal_with_login)
button_a.grid(row=3, column=1)

button_b = tk.Button(master=frame_b, text="Clear", width=6, relief=tk.GROOVE, borderwidth=1, command=deal_with_clear)
button_b.grid(row=4, column=1)

def new_window():
    my_gui = GUIapp_pg2("Cut corn", "peel corn")
    my_gui.main_gui(window_2= tk.Tk())

"""Testing"""


window.mainloop()