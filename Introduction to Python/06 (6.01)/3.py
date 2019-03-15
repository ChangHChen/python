import random
count = {"赤": 0, "白": 0, "黄": 0}
result = {"赤": "はずれ", "白": "当たり", "黄": "大当たり"}
value = ""
balls = ("赤 "*5 + "白 "*3 + "黄 " * 1)
balls = balls.split()


def func():
    n = random.randrange(9)
    count[balls[n]] += 1
    return balls[n]


ran_time = []
for times in range(5):
    ran_time.append(random.randrange(1000))
for i in range(1000):
    if i in ran_time:
        op = func()
        print(f"{i + 1}回の結果は：{op}が出ました\n{result[op]}です")
    else:
        func()

for item in count.keys():
    count[item] = count[item] / 1000
    print("{}玉の割合は{:.2%}でした".format(item, count[item]))
