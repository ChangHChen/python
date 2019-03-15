result = {}
for i in range(10):
    result[i] = 0

with open("data.txt", mode="r", encoding="utf-8") as f:
    for raw_line in f:
        line = raw_line.rstrip()
        level = 0
        while True:
            if int(line) < level * 10 + 10:
                break
            level += 1
        if level == 10:
            level -= 1
        result[level] += 1

for item in range(10):
    if item == 9:
        print(f"{item*10:2d} ~ {item*10+10:3d}| {'*' * result[item]}")
    else:
        print(f"{item*10:2d} ~ {item*10+9:3d}| {'*' * result[item]}")



