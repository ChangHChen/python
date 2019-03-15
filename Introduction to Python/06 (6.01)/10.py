import random
game = {0: "パー", 1: "チョキ", 2: "グー"}
player = {"P": "パー", "C": "チョキ", "G": "グー"}
trans = {"パー": 0, "チョキ": 1, "グー": 2}
result = {0: "あいこです", 1: "あなたの勝ちです", 2: "わたしの勝ちです"}


def rule(a, b):
    if a == b:
        return 0
    else:
        if a > b:
            if a == 2 and b == 0:
                return 2
            else:
                return 1
        else:
            if a == 0 and b == 2:
                return 1
            else:
                return 2


while True:
    print("グーならばG， チョキならばC，パーならばPを入力してください")
    n = input("どれにしますか?")
    x = random.randrange(3)
    print(f"あなたは{player[n]},わたしは{game[x]}を出しました")
    m = trans[player[n]]
    print(result[rule(m, x)], "\n")
