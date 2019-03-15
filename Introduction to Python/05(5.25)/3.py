def func1(x, y):
    z = x**2 + y**2
    return z
while True:
    x = int(input("x:"))
    y = int(input("y:"))
    print(f"xの二乗 + yの二乗 = {func1(x,y)}\n")