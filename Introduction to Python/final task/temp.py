
# ついにこんなに長いプログラムになってしまった、詳しくnoteを書きたかったが、試験期間で、復習のなめ時間がかかるため、
# できなかった、申し訳ございません。
#　大変であったが、ほんとにいい経験だと思う。
import random

card_color = {"r" : "Red", "b" :"Black", "d": "Diamond", "c" : "Club"}
card_front = {0: "A", 1 : "A", 2 : "2", 3 : "3", 4 : "4", 5 : "5", 6 : "6", 7 : "7", 8 : "8", 9 : "9",
         10 : "10", 11 : "J", 12 : "Q", 13 : "K"}
colors = ["r", "b", "d", "c"]
status = ["ready", "stand", "Bust", "Blackjack"]
triggers = ["lost", "won", "got a Blackjack", "got a drew"]


class Card(object):
    def __init__(self, front, color):
        self.front = front
        self.color = color

    def __str__(self):
        return f"[{card_color[self.color]} {card_front[self.front]}]"



def set_up_decks(deck_amount):
    all_cards = []
    for amount in range(deck_amount):
        for color in colors:
            for front in range(1, 14):
                all_cards.append(Card(front, color))
    for card in all_cards:
        if 1 < card.front < 10:
            dontwant = 1
            break
    while dontwant == 1:
        for card in all_cards:
            if 1 < card.front < 13:
                all_cards.remove(card)
                break
        dontwant = 0
        for card in all_cards:
            if 1 < card.front < 13:
                dontwant = 1
                break

    print(len(all_cards))
    return all_cards

def shuffle(deck):
    temp_deck = []
    while len(deck) > 0:
        temp = random.randrange(len(deck))
        temp_deck.append(deck[temp])
        del(deck[temp])
    return temp_deck

def value(card):
    if card.front == 1:
        return 11
    elif card.front > 9:
        return 10
    elif card.front == 0:
        return 1
    else:
        return card.front


class Player(object):
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.bets = 0
        self.status = 0
        self.hand = []
        self.point = 0
        self.if_ace_in_hand = 0

    def __str__(self):
        return f"<{self.name}> is owning ${str(self.money)}"

    def deal(self):
        self.hand.append(current_cards[0])
        del (current_cards[0])

    def detective_ace(self):
        for card in self.hand:
            if card.front == 1:
                self.if_ace_in_hand = 1
                break
            else:
                self.if_ace_in_hand = 0

    def count(self):
        self.point = 0
        self.detective_ace()
        for card in self.hand:
            self.point += value(card)
        while self.point > 21 and self.if_ace_in_hand == 1:
            # 二枚aceを持つ場合、一枚ずつでpointを1点にしてみる、もし21点以下になったら、二枚目のaceをまだ10点とみなす
            for card in self.hand:
                if card.front == 1:
                    card.front = 0
                    break
            self.point = 0
            for card in self.hand:
                self.point += value(card)
            self.detective_ace()
        return self.point

    def check(self):
        if self.point > 21:
            self.status = 2
        if len(self.hand) == 2:
            if (self.hand[0].front == 1 and self.hand[1].front > 9) or \
                    (self.hand[0].front > 9 and self.hand[1].front == 1):
                self.status = 3

    def show(self):
        print(f"<{self.name}> is holding:")
        for every_card in self.hand:
            print(every_card)
        print(self.count(),"\n")

    def bet(self, num):
        while num > self.money:
            num = int(input("not enough money, try again:"))
        self.money -= num
        self.bets += num

    def win_or_lose(self, trigger):
        if trigger == 1:
            self.money += (2 * self.bets)
        elif trigger == 2:
            self.money += (3 * self.bets)
        elif trigger == 3:
            self.money += self.bets
        self.bets = 0
        print(f"<{self.name}> {triggers[trigger]}, <{self.name}> is owning ${self.money} now\n")


name_list = ["Euler", "Gauss", "Galois", "Sheldon", "Humphrey", "Bernard Woolley", "Peter"]
round_count = 1
current_cards = set_up_decks(6)
current_cards = shuffle(current_cards)
human_players = []
print("**** welcome to BlackJack table ****")
print("6 decks of cards has been shuffled")
money = int(input("how much is the set up money?\n"))
while money < 1:
    money = int(input("set up money must be positive, try again: "))
members = int(input("how many players am I facing?(1-7)\n"))
while members < 1 or members > 7:
    members = int(input("error, try again(1-7): "))
for i in range(members):
    player = Player(name_list[i], money)
    human_players.append(player)
computer = Player("House", 0)

while True:
    print(f"** this is game <{round_count}> **")
    round_count += 1
    players_have_money = []
    for goldmine in human_players:
        if goldmine.money == 0:
            print(f"{goldmine.name} is broken")
        else:
            players_have_money.append(goldmine)
            goldmine.status = 0
            goldmine.hand = []
            goldmine.point = 0

    if len(players_have_money) > 0:
        computer.status = 0
        computer.hand = []
        for everyone in players_have_money:
            print(everyone)
            amount = int(input(f"how much does <{everyone.name}> bet?\n"))
            everyone.bet(amount)
            print(f"<{everyone.name}> made a bet of ${everyone.bets}\n")
        for i in range(2):
            computer.deal()
            for everyone in players_have_money:
                everyone.deal()
        for who_bet in players_have_money:
            print(computer.name, ": [Facing Down]", computer.hand[1])
            who_bet.check()
            who_bet.show()
            if who_bet.status == 3:
                print(status[who_bet.status])
                who_bet.win_or_lose(2)
            while who_bet.status != 3:
                if who_bet.status == 2:
                    print(status[who_bet.status])
                    who_bet.win_or_lose(0)
                    break
                elif who_bet.status == 1:
                    break
                else:
                    while who_bet.status == 0:
                        command = input(f"what would <{who_bet.name}> do?('h' for hit, 's' for stand)\n")
                        if command == "h":
                            who_bet.deal()
                            who_bet.show()
                            who_bet.check()
                            if who_bet.point == 21:
                                who_bet.status = 1
                        if command == "s":
                            who_bet.status = 1
        players_left = []
        for who_left in players_have_money:
            if who_left.status == 1:
                players_left.append(who_left)
        if len(players_left) > 0:
            computer.show()
            computer.check()
            if computer.status == 3:
                print(f"<{computer.name}> got {status[computer.status]}, all the players left lose")
                for fighter in players_left:
                        fighter.win_or_lose(0)
            while computer.status != 3:
                if computer.status == 2:
                    print(f"<{computer.name}> busted, all the players left win")
                    for survivor in players_left:
                            survivor.win_or_lose(1)
                    break
                elif computer.status == 1:
                    print(computer.name, computer.point)
                    for final_ones in players_left:
                        print(final_ones.name, final_ones.point)
                        if computer.point > final_ones.point:
                            final_ones.win_or_lose(0)
                        elif computer.point < final_ones.point:
                            final_ones.win_or_lose(1)
                        else:
                            final_ones.win_or_lose(3)
                    break
                else:
                    while computer.status == 0:
                        while computer.point < 17:
                            computer.deal()
                            print(f"<{computer.name}> took one more card")
                            computer.show()
                            computer.check()
                        if computer.status != 2:
                            computer.status = 1
        else:
            print("no player left, start next round\n")
    else:
        print("everyone is broken, time for bed")
        break
