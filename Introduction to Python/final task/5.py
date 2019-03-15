coins = [500, 100, 50, 10, 5, 1]
coin_count = {}
for coin in coins:
    coin_count[coin] = 0

while True:
    print('***"END"が入力されたら、終了する***')
    amount = input("金額を入力してください：")
    if amount == "END":
        break
    else:
        standard = 0
        amount = int(amount)
        while amount > 0:
            current_coin = coins[standard]
            if amount >= current_coin:
                amount -= current_coin
                coin_count[current_coin] += 1
            else:
                standard += 1
    print(f"円の支払いために必要な硬貨は：")
    for coin in coins:
        print(f"{coin:3d}円：{coin_count[coin]}枚")
        coin_count[coin] = 0
    print(f"\n")
