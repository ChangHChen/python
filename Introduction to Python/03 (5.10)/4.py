print("*ｙを入力すると、次へ進む*")
x = []
y = []
while True:
    item = input("xの項目：")
    if item == "y":
        break
    x.append(int(item))
print("x =", x)
print("*ENDを入力すると、次へ進む*")
while True:
    item = input("yの項目：")
    if item == "END":
        break
    y.append(int(item))
print("y =", y)
z = []
for i in range(len(x)):
    if x[i] not in z:
        z.append(x[i])
for j in range(len(y)):
    if y[j] not in z:
        z.append(y[j])
print("z =", z)

