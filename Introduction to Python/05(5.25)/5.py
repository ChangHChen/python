def fact(n):
    if n == 0:
        return 1
    else:
        total = 1
        for i in range(1, n+1):
            total *= i
        return total


while True:
    n = int(input("正整数を入力してください："))
    print(f"n! = {fact(n)}")