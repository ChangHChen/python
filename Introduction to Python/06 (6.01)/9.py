import random
x = random.randrange(1, 101)
count = 0
print("***正解は１以上１００以下の整数です***")
while True:
    y = int(input("数を入力してください："))
    count += 1
    if y > x:
        print("大きすぎます")
    elif y < x:
        print("小さすぎます")
    else:
        print("おめでとう、正解です")
        print(f"貴方は{count}回目で正解でした")
        break
