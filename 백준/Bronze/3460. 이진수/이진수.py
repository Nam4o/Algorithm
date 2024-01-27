t = int(input())

for tc in range(t):
    answer = []
    number = int(input())
    number = bin(number)[2:]
    for i in range(1, len(number) + 1):
        if number[-i] == "1":
            answer.append(i - 1)
    print(*answer)