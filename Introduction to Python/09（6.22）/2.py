from tkinter import Frame, Label, StringVar, Entry, Button, TOP, LEFT, END


class Calculator(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.master.title("Calculator")

        self.result = StringVar()
        Label(self, textvariable=self.result, width=20,
              font=("Helvetica", 14)).pack(side=TOP)
        self.result.set("整数を入力してください")

        frame1 = Frame(self)
        frame1.pack(side=TOP)
        self.num1 = Entry(frame1, font=("Helvetica", 12))
        self.num1.pack(side=TOP)
        self.num2 = Entry(frame1, font=("Helvetica", 12))
        self.num2.pack(side=TOP)

        frame2 = Frame(self)
        frame2.pack(side=TOP)
        Button(frame2, text="加算", command=self.addition,
               font=("Helvetica", 10)).pack(side=LEFT)
        Button(frame2, text="減算", command=self.subtraction,
               font=("Helvetica", 10)).pack(side=LEFT)
        Button(frame2, text="乗算", command=self.multiplication,
               font=("Helvetica", 10)).pack(side=LEFT)
        Button(frame2, text="除算", command=self.division,
               font=("Helvetica", 10)).pack(side=LEFT)

    def addition(self):
        x = int(self.num1.get())
        y = int(self.num2.get())
        result = f"{x:d} + {y:d} = {x + y:d}"
        self.result.set(result)
        self.reset()

    def subtraction(self):
        x = int(self.num1.get())
        y = int(self.num2.get())
        result = f"{x:d} - {y:d} = {x - y:d}"
        self.result.set(result)
        self.reset()

    def multiplication(self):
        x = int(self.num1.get())
        y = int(self.num2.get())
        result = f"{x:d} * {y:d} = {x * y:d}"
        self.result.set(result)
        self.reset()

    def division(self):
        x = int(self.num1.get())
        y = int(self.num2.get())
        result = f"{x:d} / {y:d} = {x / y:.2f}"
        self.result.set(result)
        self.reset()

    def reset(self):
        list_temp = [self.num1, self.num2]
        # 数の個数がこれ以上増えたら、リストを使たほうがしやすくなる。現在はちょっと無駄だが。
        for i in list_temp:
            i.delete(0, END)


Calculator().mainloop()
