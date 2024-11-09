import random
import time


def CreateDeck():
    deck = []
    for suit in ['Cơ', 'Rô', 'Chuồn', 'Bích']:
        for value in range(2, 11):
            deck.append((str(value), suit))
        for face in ['J', 'Q', 'K', 'A']:
            deck.append((face, suit))
    return deck


def DealHand(deck):
    return [deck.pop(), deck.pop()]


def Scores(hand):
    score = 0
    A = 0
    for card, suit in hand:
        if card in ['J', 'Q', 'K']:
            score += 10
        elif card == 'A':
            score += 10
            A += 1
        else:
            score += int(card)
    while score > 21 and A:
        score -= 10
        A -= 1
    return score


def Play(Money):
    deck = CreateDeck()
    random.shuffle(deck)
    Player = DealHand(deck)
    Boss = DealHand(deck)
    PlayerScore = Scores(Player)
    BossScore = Scores(Boss)
    bet = int(input("Bạn cược bao nhiêu cho ván này (¬_¬”) : "))
    if Money < bet:
        print("Không đủ tiền")
        return Play(Money)

    print(f"Bài của bạn: {', '.join(f'{card} {suit}' for card, suit in Player)} ----> {PlayerScore} điểm")
    time.sleep(1)
    print(f"Bài của Nhà cái : [? , ?] ( ￣︿￣) ")
    print("――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")

    while True:
        if PlayerScore > 21:
            print("Bạn đã thua")
            Money -= bet
            PlayAgain = input("Bạn muốn chơi ván mới không(っ˘ڡ˘ς)?(y/n): ").strip().lower()
            if PlayAgain == "y":
                print("――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
                print(f"   ︻┳═一 Bạn hiện có : ${Money}")
                Again(Money)
            elif PlayAgain == "n":
                return Money
        action = input("Dằn hay Rút? (d/r): ").strip().lower()
        if action == "r":
            Player.append(deck.pop())
            PlayerScore = Scores(Player)
            print(f"Bài của bạn: {', '.join(f'{card} {suit}' for card, suit in Player)} ----> {PlayerScore} điểm")
            print("――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
        elif action == "d":
            if PlayerScore < 16:
                print("Chưa đủ điểm")
                continue
            else:
                break

    while BossScore < 15:
        Boss.append(deck.pop())
        BossScore = Scores(Boss)

    print("――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
    print(f"Bài của bạn: {', '.join(f'{card} {suit}' for card, suit in Player)} ----> {PlayerScore} điểm")

    print("Bài của Nhà cái là: ", end="")
    for card, suit in Boss:
        print(f"{card} {suit}", end=" ")
        time.sleep(1)
    print(f"---> {BossScore} điểm")

    if BossScore > 21:
        print("――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
        print("---> Nhà Cái quát! Bạn thắng!( ￣▽￣).")
        print(f"Số tiền thắng là ${bet}")
        print("――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
        Money += bet
    elif PlayerScore > BossScore:
        print("――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
        print("---> Bạn thắng!( ￣▽￣)")
        print(f"Số tiền thắng là ${bet}")
        print("――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
        Money += bet
    elif PlayerScore < BossScore:
        print("――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
        print("---> Nhà Cái ăn!(>_<)")
        print(f"Số tiền thua là ${bet}")
        print("――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
        Money -= bet
    else:
        print("――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
        print("---> Huề!(・ω・)")
        print("――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")

    PlayAgain = input("Bạn muốn chơi ván mới không(っ˘ڡ˘ς)?(y/n): ").strip().lower()
    if PlayAgain == "y":
        print("――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
        print(f"   ︻┳═一 Bạn hiện có : ${Money}")
        Again(Money)
    elif PlayAgain == "n":
        return Money


def Again(Money):
    Play(Money)


if __name__ == "__main__":
    Money = 1000
    print("===========================Xì Dách===========================")
    Welcome = "   ◕‿◕ Chào mừng bạn đến với trò chơi xì dách ◕‿◕"
    for char in Welcome:
        print(char, end="")
        time.sleep(0.02)
    print()
    print(f"   ︻┳═一 Bạn hiện có : ${Money}")
    print("----------------------------------------------------")
    Play(Money)
    print(f"Tạm biệt( o˘◡˘o)")