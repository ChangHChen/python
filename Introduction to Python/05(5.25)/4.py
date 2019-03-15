def abs_val(x):
    if x < 0:
        return -x
    else:
        return x
while True:
    x = float(input("x:"))
    print(f"の絶対値は：{abs_val(x)}")