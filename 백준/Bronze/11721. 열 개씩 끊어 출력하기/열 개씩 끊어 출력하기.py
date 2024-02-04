a = input()
arr = list(a)

idx = 0
ans = ""
while True:
    if idx != 0 and (idx % 10) == 0:
        print(ans)
        ans = ""
    if idx == len(arr):
        print(ans)
        break
    ans += arr[idx]
    idx += 1