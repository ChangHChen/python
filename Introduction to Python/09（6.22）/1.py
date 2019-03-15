from tkinter import Frame, StringVar, Label, Entry, Button, TOP, LEFT, END


class CountDownTimer(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.master.title("Count Down Timer")

        self.time_left = StringVar()
        Label(self, textvariable=self.time_left, font=("Helvetica", 24)).pack(side=TOP)

        self.input = Entry(self, font=("Helvetica", 24))
        self.input.pack(side=TOP)

        frame = Frame(self)
        frame.pack()
        Button(frame, text="start", command=self.activate, font=("Helvetica", 18)).pack(side=LEFT)
        Button(frame, text="quit", command=self.master.destroy, font=("Helvetica", 18)).pack()

    def activate(self):
        self.set()
        self.after(1000, self.count_down)

    def set(self):
        self.trans = int(self.input.get())
        self.time_left.set(int(self.trans))
        self.input.delete(0, END)

    def count_down(self):
        if self.trans > 0:
            self.trans -= 1
            self.time_left.set(self.trans)
            self.after(1000, self.count_down)


CountDownTimer().mainloop()
