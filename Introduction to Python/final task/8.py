# こう書いたら、ランニング時間が想像以上にかかってしまった（2，3分ぐらい）。
# このプログラムより、鉛筆でやるのが逆に速い。
# もっといい書き方があるかもしれないと思った。考え出したら、改めて書き直す。


def find_the_number(num):
    x = 1
    while True:
        if x < 21:
            if num % x == 0:
                x += 1
            else:
                break
        else:
            return "true"


num = 20
while True:
    if find_the_number(num) != "true":
        num += 1
    else:
        break

print(f"1から20までのすべての整数で割りきれる最小の数は：{num}")
