from tkinter import Frame, Label, Entry, StringVar, Button, TOP, LEFT, END


class PauseContinueButton(Button):
    def __init__(self, master, status0, status1, send):
        self.text = StringVar()
        super().__init__(master, textvariable=self.text, command=self.rev,
                         width=8, font=("Helvetica", 12))
        self.status = [status0, status1]
        self.current = 0
        self.send = send
        self.text.set(self.status[self.current])

    def rev(self):
        if self.current == 0:
            self.current = 1
        else:
            self.current = 0
        self.text.set(self.status[self.current])
        self.send(self.current)


class FancyTimeDownCounter(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.master.title("Time Down Counter 2.0")
        self.temp = 0
        self.detect = 0

        self.time_left = StringVar()
        Label(self, textvariable=self.time_left, width=18,
              font=("Helvetica", 18)).pack(side=TOP)
        self.time_left.set(self.temp)

        self.input = Entry(self, width=8, font=("Helvetica", 14))
        self.input.pack(side=TOP)

        frame = Frame(self).pack(side=TOP)
        Button(frame, text="Start", command=self.start,
               font=("Helvetica", 12)).pack(side=LEFT)
        self.p_c_button = PauseContinueButton(frame, "Pause", "Continue", self.receive)
        self.p_c_button.pack(side=LEFT)
        Button(frame, text="Reset", command=self.reset,
               font=("Helvetica", 12)).pack(side=LEFT)
        Button(frame, text="Quit", command=self.master.destroy,
               font=("Helvetica", 12)).pack(side=LEFT)

    def start(self):
        # pauseの状態（pause/continueボタンがcontinueを示しているとき）で、
        # またstartを押すと、pause/continueボタンをpauseを回復命令
        if self.detect == 1:
            self.p_c_button.rev()
        self.temp = int(self.input.get())
        self.time_left.set(self.temp)
        self.receive(1)
        self.receive(0)

    def count_down(self):
        if self.detect == 0:
            if self.temp > 0:
                self.temp -= 0.001
                # 時々-0.001になることがあって、考えても分からないため、
                # この零より小さくなったら、零にするという命令を書いた。
                if self.temp <= 0:
                    self.temp = 0
                    self.time_left.set(self.temp)
                else:
                    temp = f"{self.temp:.3f}"
                    self.time_left.set(temp)
                    self.after(1, self.count_down)

    def receive(self, trans):
        self.detect = trans
        if self.detect == 0:
            self.count_down()

    def reset(self):
        self.input.delete(0, END)
        self.temp = 0
        self.time_left.set(self.temp)


FancyTimeDownCounter().mainloop()
