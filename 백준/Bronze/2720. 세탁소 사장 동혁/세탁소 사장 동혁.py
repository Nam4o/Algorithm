T = int(input())

for tc in range(T):
    C = int(input())

    coins = {25: 0, 10: 0, 5: 0, 1: 0}

    one = C // 25
    two = (C % 25) // 10
    three = ((C % 25) % 10) // 5
    four = (((C % 25) % 10) % 5) // 1

    coins[25] = one
    coins[10] = two
    coins[5] = three
    coins[1] = four
    print(*coins.values())