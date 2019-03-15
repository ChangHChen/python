class Vehicle(object):
    def __init__(self, energy, wheels, color):
        self.energy = energy
        self.wheels = wheels
        self.color = color
        self.odo = 0

    def __str__(self):
        return f"[Vehicle], Energy: {self.energy}, Wheels: {self.wheels}. Color: {self.color}"

    def run(self, distance):
        self.odo += distance


print(f"instanceを生成した")
v1 = Vehicle("gasoline", 4, "Black")
v2 = Vehicle("sunshine", 2, "Sliver")
print(f"""V1:{v1}
V2:{v2}
""")

print("v1を走らせる")
for dist in range(100, 501, 80):
    v1.run(dist)
    print(f"v1の走行距離は{v1.odo}")
print()

print("v2のカラーを変える")
v2.color = "Black"
print("v2の色は", v2.color)
print(v2)
