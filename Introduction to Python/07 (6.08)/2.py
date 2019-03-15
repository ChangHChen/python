class Reg_polygon(object):
    def __init__(self, edges, length):
        self.edges = edges
        self.length = length
        self.perimeter = self.edges * self.length

    def __str__(self):
        return f"[Reg_polygon] 辺の数：{self.edges},　辺の長さ：{self.length}, 周囲の長さは:{self.perimeter}"


polygon1 = Reg_polygon(3, 20)
polygon2 = Reg_polygon(4, 25)
polygon3 = Reg_polygon(5, 20)

print(f"""{polygon1}
{polygon2}
{polygon3}""")
