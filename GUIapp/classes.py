import tkinter as tk


class GUIapp_pg2:
    def __init__(self, task1, task2):
        self.task1 = task1
        self.task2 = task2

    def main_gui(self, window_2):
        self.window_2 = window_2
        window_2.title("Task tracker app")
        self.frabe_a = tk.Frame(master=window_2)
        self.frabe_a.grid(row=0, column=3, sticky="ew")
        self.frame_b = tk.Frame(master=window_2)
        self.frame_b.grid(row=1, column=2)
        self.frame_c = tk.Frame(master=window_2)
        self.frame_c.grid(row=1, column=3)
        self.labelMain = tk.Label(master=self.frabe_a, text="Welcome, please check off your tasks", relief=tk.RAISED,
                                  borderwidth=1, bg="green", fg="white",)
        self.labelMain.grid(row=0, column=0)

        self.label = tk.Label(master=self.frame_b, text=self.task1, relief=tk.RAISED, bg="red", fg="white",
                              borderwidth=1, width=8)
        self.label.grid(row=0, column=0)

        self.label_b = tk.Label(master=self.frame_b, text=self.task2, relief=tk.RAISED, bg="red", fg="white",
                              borderwidth=1, width=8)
        self.label_b.grid(row=1, column=0)

        self.str_check = tk.StringVar()
        """string_total = "Today completed tasks: \n """

        def add_values():
            print(self.str_check.get())

        self.Checkbutton = tk.Checkbutton(master=self.frame_c, text="Check if complete", variable=self.str_check,
                                          command=add_values, onvalue="hello", offvalue="bye")
        self.Checkbutton.pack()






        '''self.Checkbutton_b = tk.Entry(master=self.frame_c, relief=tk.GROOVE, borderwidth=1, width=20)
        self.entry_b.grid(row=1, column=0)'''
        self.window_2.mainloop()






