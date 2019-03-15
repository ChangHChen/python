ques ={}
ques[0] = """いつも何をチャレンジしている国はどこ？
    １.中国    ２．朝鮮    ３．アメリカ"""
ques[1] = """おじいちゃんとする球技は何？
    １.ゲートボール    ２．ゴルフ    ３．ソフトボール"""
ques[2] = """「？」に入る食べ物は何？　５÷２＝「？」
    １．チーズ   ２．ご飯    ３．チキン"""
answer = {0: 2, 1: 3, 2: 2}
count = 0

for i in range(len(ques.keys())):
    print(ques[i])
    ans = int(input("答えの番号を入力ください："))
    if ans == answer[i]:
        print("正解です！\n")
        count += 1
    else:
        print("残念、不正解です\n")

result = count / len(ques.keys())
print("正解率は{0:.1%}でした".format(result))