from tkinter import Frame, StringVar, Label, Button, LEFT, TOP
import random


class RockPaperScissors(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.master.title("Rock Paper Scissors")
        self.item = ["✊", "✌", "✋"]
        self.rule = ["アイコです", "貴方の負けです", "貴方の勝ちです"]
        self.hum = 0
        self.com = 0

        self.result = StringVar()
        self.progress = StringVar()
        Label(self, textvariable=self.progress, width=30,
              font=("Helvetica", 14)).pack(side=TOP)
        self.progress.set("じゃんけんしましょう")
        Label(self, textvariable=self.result,
              font=("Helvetica", 14)).pack(side=TOP)

        frame = Frame(self)
        frame.pack(side=TOP)
        Button(frame, text="グー", command=self.rock,
               font=("Helvetica", 10)).pack(side=LEFT)
        Button(frame, text="チョキ", command=self.scissors,
               font=("Helvetica", 10)).pack(side=LEFT)
        Button(frame, text="パー", command=self.paper,
               font=("Helvetica", 10)).pack(side=LEFT)
        Button(frame, text="quit", command=self.master.destroy,
               font=("Helvetica", 10)).pack(side=LEFT)

    def rock(self):
        self.hum = 0
        self.activate()

    def scissors(self):
        self.hum = 1
        self.activate()

    def paper(self):
        self.hum = 2
        self.activate()

    def activate(self):
        self.com = random.randrange(3)
        text1 = f"私は{self.item[self.com]}です、貴方は{self.item[self.hum]}です"
        text2 = f"{self.rule[(self.hum + 3 - self.com) % 3]}"

        self.progress.set(text1)
        self.result.set(text2)


RockPaperScissors().mainloop()
