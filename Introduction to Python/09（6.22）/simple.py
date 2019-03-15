# ex06
from tkinter import Frame, Button, Label, StringVar, LEFT


class RevButtonApp(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        frame = Frame(self)
        frame.pack()
        # ボタンを5個作る
        self.buttons = []
        for i in range(5):
            button = ReversibleButton(frame, i, i % 2, self.notify)
            button.pack(side=LEFT)
            self.buttons.append(button)

        self.message = StringVar()
        Label(self, textvariable=self.message).pack()

    # ボタンからの通知を受け取る
    def notify(self, buttonId):
        # 押されたボタンの番号を表示
        text = f"Button #{buttonId:d}"
        self.message.set(text)
        # ボタンの状態をチェック
        for button in self.buttons:
            if button.status != 1:
                break
        else:
            self.message.set("すべてのボタンが×になりました")


# 新しいボタンクラス
class ReversibleButton(Button):
    def __init__(self, master, myid, status, notify):
        self.text = StringVar()    # ボタンの表示用
        super().__init__(master, textvariable=self.text, command=self.rev,
                         font=("Helvetica", 24))
        self.id = myid
        self.notify = notify
        self.status = status       # 0は○，1は×を表す
        self.show()                # ボタン上に表示する

    # 自分を裏返す処理
    def rev(self):
        if self.status == 0:
            self.status = 1
        else:
            self.status = 0
        self.show()
        self.notify(self.id)    # どのボタンが押されたかを通知する

    # ボタンにマークを表示
    def show(self):
        if self.status == 0:
            self.text.set("○")
        else:
            self.text.set("×")


RevButtonApp().mainloop()