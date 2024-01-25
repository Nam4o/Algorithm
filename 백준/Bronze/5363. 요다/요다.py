t = int(input())

for tc in range(t):
    arr = list(input().split())
    arr.append(arr.pop(0))
    arr.append(arr.pop(0))  
    print(*arr)