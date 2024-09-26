import random


def bets():
    a = random.randint(0, 6)
    b = random.randint(0, 6)
    c = random.randint(0, 6)
    print(a, b, c)
    if a == b and a == c:
        print("vc ganhou, infeliz")
        prize = bet * 1.5
        result = money - bet + prize
        return result

    else:
        print("vc se fudeu kkkkkk")
        result = money - bet
        print(result)
        return result


def new_games():
    new_game = input("vc quer apostar denovo? 1 = sim 2 = não: ")
    if new_game == 1:
        bets()
    else:
        pass


money = float(input("quanto reais vc quer depositar: "))
while True:
    bet = float(input("quanto vc quer apostar: "))
    if bet > money:
        print("vc tá doido home apostando mais do que tem kkkkkk")
    else:
        money = bets()
        new_games()
