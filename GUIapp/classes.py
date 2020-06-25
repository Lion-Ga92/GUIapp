import tkinter as tk


class GUIapp_pg2:
    def __init__(self, task1, task2):
        self.task1 = task1
        self.task2 = task2

    def main_gui(self, window_2):
        self.window_2 = window_2
        window_2.title("Task tracker app")
        self.frame_a = tk.Frame(master=window_2)
        self.frame_a.grid(row=0, column=0)
        self.frame_b = tk.Frame(master=window_2)
        self.frame_b.grid(row=0, column=1)

        self.label = tk.Label(master=self.frame_a, text=self.task1, relief=tk.RAISED, bg="red", fg="white",
                              borderwidth=1, width=8)
        self.label.pack()

        self.label_b = tk.Label(master=self.frame_a, text=self.task2, relief=tk.RAISED, bg="red", fg="white",
                              borderwidth=1, width=8)
        self.label_b.pack()

        self.entry = tk.Entry(master=self.frame_b,relief=tk.GROOVE, borderwidth=1, width=20)
        self.entry.pack()

        self.entry_b = tk.Entry(master=self.frame_b, relief=tk.GROOVE, borderwidth=1, width=20)
        self.entry_b.pack()
        self.window_2.mainloop()


