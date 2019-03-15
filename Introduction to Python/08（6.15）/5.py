from tkinter import Frame, Label, StringVar, Button, LEFT, TOP, BOTTOM
import random

backside = ["あたり", "はずれ", "どうなるか"]


class WhichOne(object):
    def __init__(self):
        self.m1 = 0
        self.m2 = 0

    def activate(self):
        self.m1 = random.randrange(2)
        self.m2 = 1 - self.m1


which_one = WhichOne()


class TryYourLuck(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.master.title("運試し")

        self.result = StringVar()
        Label(self, textvariable=self.result, font=("Helvetica", 36)).pack(side=TOP)

        self.result.set(backside[2])
        which_one.activate()

        frame = Frame()
        frame.pack(side=BOTTOM)

        Button(frame, text="こっちか？", command=self.left, font=("Helvetica", 24)).pack(side=LEFT)
        Button(frame, text="こっちか？？", command=self.right, font=("Helvetica", 24)).pack(side=LEFT)
        Button(frame, text="もう一回", command=self.reset, font=("Helvetica", 24)).pack(side=LEFT)
        Button(frame, text="もういい", command=self.dismiss, font=("Helvetica", 24)).pack(side=LEFT)

    def left(self):
        self.result.set(backside[which_one.m1])

    def right(self):
        self.result.set(backside[which_one.m2])

    def reset(self):
        self.result.set(backside[2])
        which_one.activate()

    def dismiss(self):
        self.master.destroy()


TryYourLuck().mainloop()
