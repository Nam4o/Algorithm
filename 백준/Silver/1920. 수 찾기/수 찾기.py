N = int(input())
nums_N = set(map(int, input().split()))

M = int(input())
nums_M = list(map(int, input().split()))



for i in nums_M:
    if i in nums_N:
        print(1)
    else:
        print(0)


