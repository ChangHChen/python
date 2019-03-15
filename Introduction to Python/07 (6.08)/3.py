class Counter(object):
    def __init__(self):
        self.count = 0

    def up(self):
        self.count += 1

    def down(self):
        self.count -= 1

    def __str__(self):
        return f"[Counter] カウンタの値：{self.count}"


event = Counter()
print('*** Enter "result" to show result ***')
while True:
    x = input('Enter "up" or "down" to count:')
    if x == "result":
        print(event)
        break
    elif x == 'up':
        event.up()
    elif x == 'down':
        event.down()
    else:
        print("error try again")
