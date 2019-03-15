import random
with open("data0501.txt", mode="w", encoding="utf-8") as f:
    for i in range(10):
        rnd = random.randrange(1000)
        print(f"{i+1:2d}番の乱数:{rnd:4d}")
        s = f"{rnd:4d}\n"
        f.write(s)