class Books(object):
    def __init__(self, title, arthur):
        self.title = title
        self.arthur = arthur

    def __str__(self):
        return f"[Books] 「{self.title} by {self.arthur}」"


book1 = Books("白夜行", "東野　圭吾")
book2 = Books("ZOO", "乙一")
book3 = Books("ドグラ・マグラ", "夢野　久作")

print(f"""**今日のオススメは**
{book1}
{book2}
{book3}""")
