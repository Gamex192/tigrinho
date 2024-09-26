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
        print(result)
        return result

    else:
        print("vc se fudeu kkkkkk")
        result = money - bet
        print(result)
        return result


sla = 1
money = float(input("quanto reais vc quer depositar: "))
while sla == 1:
    bet = float(input("quanto vc quer apostar: "))
    if bet > money:
        print("vc tá doido home apostando mais do que tem kkkkkk")
        sla = 2
    else:
        money = bets()
        sla = int(input("você quer continuar apostando? 1 = sim 2 = não:"))
