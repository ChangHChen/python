from tkinter import Frame, StringVar, Label, Button, TOP, BOTTOM, LEFT


class Counter(object):
    def __init__(self, value):
        self.val = value

    def up(self):
        self.val += 1

    def down(self):
        self.val -= 1
        if count.val < 0:
            self.val = 0

    def __str__(self):
        return f"{self.val}"


count = Counter(0)


class UpDownCounter(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.master.title("Up Down Counter")

        self.result = StringVar()
        Label(self, textvariable=self.result, font=("Helvetica", 36)).pack(side=TOP)
        self.result.set(count)

        frame = Frame()
        frame.pack(side=BOTTOM)
        Button(frame, text="Plus 1", command=self.plus_one, font=("Helvetica", 24)).pack(side=LEFT)
        Button(frame, text="Minus 1", command=self.minus_one, font=("Helvetica", 24)).pack(side=LEFT)
        Button(frame, text="Quit", command=self.dismiss, font=("Helvetica", 24)).pack()

    def plus_one(self):
        count.up()
        self.result.set(count)

    def minus_one(self):
        count.down()
        self.result.set(count)

    def dismiss(self):
        self.master.destroy()


UpDownCounter().mainloop()
