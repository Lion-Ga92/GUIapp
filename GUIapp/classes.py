import tkinter as tk


class GUIapp_pg2:
    def __init__(self, task1, task2):
        self.task1 = task1
        self.task2 = task2

    def main_gui(self, window_2):
        window_2.title("Task tracker app")
        self.frabe_a = tk.Frame(master=window_2)
        self.frabe_a.grid(row=0, column=2, sticky="ew")
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

        def doSomething():
            if Variable_one.get() == 1:
                print("Hello World")
            elif Variable_one.get() == 0:
                print("Good bye")

        Variable_one = tk.IntVar()

        self.Checkbutton = tk.Checkbutton(master=self.frame_b, text="I do something", onvalue=1, offvalue=0,
                                          variable=Variable_one, command=doSomething)

        self.Checkbutton.grid(row=0, column=1)

        def doSomething_2():
            if Variable_one.get() == 1:
                print("Hello World")
            elif Variable_one.get() == 0:
                print("Good bye")

        Variable_two = tk.IntVar()

        self.Checkbutton = tk.Checkbutton(master=self.frame_b, text="I do something", onvalue=1, offvalue=0,
                                          variable=Variable_two, command=doSomething_2)

        self.Checkbutton.grid(row=1, column=1)








