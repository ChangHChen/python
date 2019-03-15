dict = {}
while True:
    key = input("キーを入力してください:")
    if key == "END":
        break
    val = input("値を入力してくだいさい:")
    dict[key] = val
for i in dict:
    print(i, dict[i])