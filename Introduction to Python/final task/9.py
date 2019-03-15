# このルールによって、容易に考えられるのは二つのプレーヤがそれぞれの行動を出すことのを1roundとすると
# このroundの中に、第二プレーヤが当該roundの総行動数を４にすることができる。
# 相手が最後の一本を取ると、自分の勝利になる。つまり自分が取った後、残りが一本なら、もう必ず勝利である。
# 先roundの考えを加えると、自分が取った後、残りが1+４N本の状況が望うましい。
# このような考えをもとにcomputer先行なら、computerが必ず勝利。人間が勝利を取れるため、先行で２本を取るしかできません。

import random
total = 23
all_player = ["computer", "あなた"]
game_name = 1


def com_move(num):
    list = []
    x = 0
    for i in range(6):
        if num < 1 + (4*i):
            list.append("<")
        elif num > 1 + (4*i):
            list.append(">")
        elif num == 1 + (4*i):
            list.append("=")
    #  もし人間から1+4N本の残りを取られたら、できることは人間がこの後最優の動きを出さないことを願いしかないので
    # このroundには、ランドムのマーチを取る
    if "=" in list:
        if current_total < 3:
            return 1 + random.randrange(current_total)
        else:
            return 1 + random.randrange(3)
    else:
        for i in range(6):
            if list[i] == ">":
                x = i
        return num - (1 + 4*x)


while True:
    current_total = total
    hum_round = com_round = 1
    player = random.randrange(2)
    print(f"*第{game_name}局ゲーム\n先攻は{all_player[player]}*")
    while True:
        print(f"*残りは{current_total}本です*")
        if current_total == 0:
            break
        else:
            if player == 0:
                move = com_move(current_total)
                print(f"{all_player[player]}の第{com_round}手:\n{move:3d}本引きました")
                current_total -= move
                com_round += 1
                player = 1
            elif player == 1:
                hum_move = int(input("*何本引きますか？(1-3本):* "))
                while hum_move > 3 or hum_move < 1:
                    hum_move = int(input("*error,改めて入力してください：* "))
                while hum_move > current_total:
                    print("*残り以上に引きことはできない*")
                    hum_move = int(input("*改めて入力してください：* "))
                print(f"{all_player[player]}の第{hum_round}手:\n{hum_move:3d}本引きました")
                current_total -= hum_move
                hum_round += 1
                player = 0
    if player == 0:
        print(f"\n*あなたの負けです*")
    else:
        print(f"\n*おめでとう、あなたの勝利です*")
    again = input("*もう一局しませんか？(Y/N):* ")
    while again != "Y" and again != "N":
            again = input("*error,改めて入力してください(Y/N)：* ")
    if again == "N":
        break
    elif again == "Y":
        game_name += 1
        print(f"\n")
