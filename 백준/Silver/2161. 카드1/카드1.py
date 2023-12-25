n = int(input())

arr = [_ for _ in range(1, n + 1)]

answer = []
if len(arr) >= 2:
    while len(arr) >= 2:
        if len(arr) != 2:
            answer.append(arr.pop(0))
            arr.append(arr.pop(0))
        else:
            answer.append(arr.pop(0))
            answer.append(arr.pop(0))
    print(*answer)
else:
    print(*arr)