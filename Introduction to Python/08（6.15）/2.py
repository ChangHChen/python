from tkinter import Frame, Label, LEFT


class GuiApp(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        Label(self, text="Red is on fire", fg="red", font=("Helvetica", 36)).pack(side=LEFT)
        Label(self, text="Yellow don't give up", fg="yellow", font=("Helvetica", 36)).pack(side=LEFT)
        Label(self, text="whatever", fg="green", font=("Helvetica",  36)).pack(side=LEFT)


GuiApp().mainloop()
