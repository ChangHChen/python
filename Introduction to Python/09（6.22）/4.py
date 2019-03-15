from tkinter import Frame, Button, Label, StringVar, TOP, LEFT
import random


class ButtonWithTwoSides(Button):
    def __init__(self, master, num, back1, back2, send):
        self.text = StringVar()
        super().__init__(master, textvariable=self.text, width=8, height=3, command=self.rev,
                         font=("Helvetica", 12))
        self.all_sides = [num, back1, back2]
        self.status = 0
        self.text.set(self.all_sides[self.status])
        self.send = send

    def rev(self):
        self.text.set(self.all_sides[self.status])
        self.send(self.all_sides[0], self.status)


class FortuneTelling(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.master.title("Fortune Telling 2.0")
        self.conversation = ["おめでとう", "惜しい", "もう一回やったら",
                             "次は、きっと", "運が悪いね", "どうなるか"]
        self.counter = 1
        self.result = 0
        self.buttons = []
        self.buttons_pressed = []

        self.label_text = StringVar()
        Label(self, textvariable=self.label_text,
              font=("Helvetica", 36)).pack(side=TOP)

        frame = Frame(self)
        frame.pack(side=TOP)

        for i in range(5):
            button = ButtonWithTwoSides(frame, i, "あたり", "はずれ", self.receive)
            button.pack(side=LEFT)
            self.buttons.append(button)
        Button(frame, text="Reset", command=self.reset,
               width=8, height=3, font=("Helvetica", 12)).pack(side=LEFT)

        self.all_set()

    def all_set(self):
        self.result = random.randrange(5)
        for button in self.buttons:
            button.status = 2
        self.buttons[self.result].status = 1
        self.label_text.set(self.conversation[-1])

    def receive(self, num, x):
        if num not in self.buttons_pressed:
            if x == 1:
                self.label_text.set(self.conversation[0])
                for button in self.buttons:
                    button.text.set(button.all_sides[button.status])
                    self.buttons_pressed.append(button.all_sides[0])
            elif x == 2:
                self.label_text.set(self.conversation[self.counter])
                self.counter += 1
                self.buttons_pressed.append(num)

    def reset(self):
        for button in self.buttons:
            button.status = 0
            button.text.set(button.all_sides[button.status])
        self.counter = 1
        self.buttons_pressed = []
        self.all_set()


FortuneTelling().mainloop()
