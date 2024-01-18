arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

ans1 = sum(arr1)
ans2 = sum(arr2)

if ans1 < ans2:
    print(ans2)
else:
    print(ans1)