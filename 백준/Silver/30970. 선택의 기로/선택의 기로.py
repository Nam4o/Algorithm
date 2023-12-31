n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

arr1 = sorted(arr, key=lambda x : (-x[0], x[1]))
arr2 = sorted(arr, key= lambda x : (x[1], -x[0]))
print(*arr1[0], *arr1[1])
print(*arr2[0], *arr2[1])