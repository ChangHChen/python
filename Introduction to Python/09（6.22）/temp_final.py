from tkinter import Frame, Button, Label, StringVar, LEFT


class ReversibleButton(Button):
    def __init__(self, master, myid, status, notify):
        self.text = StringVar()
        super().__init__(master, textvariable=self.text, command=self.rev,
                         font=("Helvetica", 24))
        self.id = myid
        self.notify = notify
        self.status = status
        self.show()

    def rev(self):
        if self.status == 0:
            self.status = 1
        else:
            self.status = 0
        self.show()
        self.notify(self.id)

    def show(self):
        if self.status == 0:
            self.text.set("○")
        else:
            self.text.set("×")


class RevButtonApp(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        frame = Frame(self)
        frame.pack()
        self.buttons = []
        for i in range(5):
            button = ReversibleButton(frame, i, i % 2, self.notify)
            button.pack(side=LEFT)
            self.buttons.append(button)

        self.message = StringVar()
        Label(self, textvariable=self.message).pack()

    def notify(self, buttonid):
        text = f"Button #{buttonid:d}"
        self.message.set(text)
        for button in self.buttons:
            if button.status != 1:
                break
        else:
            self.message.set("すべてのボタンが×に何ました")


RevButtonApp().mainloop()
