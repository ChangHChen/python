import random
from tkinter import Frame, StringVar,Label, Button, LEFT, TOP, BOTTOM

fortune = ["大吉", "吉", "小吉", "凶", "諦めないで", "運を見てみないか"]


def pick_one(any_list):
    x = random.randrange(len(any_list) - 1)
    return any_list[x]


class FortuneTelling(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.master.title("御神籤")

        self.fortune = StringVar()
        Label(self, textvariable=self.fortune, font=("Helvetica", 36)).pack(side=TOP)

        frame = Frame()
        frame.pack(side=BOTTOM)
        Button(frame, text="引く", command=self.pick).pack(side=LEFT)
        Button(frame, text="もういい", command=self.dismiss).pack(side=LEFT)

        self.fortune.set(fortune[-1])

    def pick(self):
        self.fortune.set(pick_one(fortune))

    def dismiss(self):
        self.master.destroy()


FortuneTelling().mainloop()
