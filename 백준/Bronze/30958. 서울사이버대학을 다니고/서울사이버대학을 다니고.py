n = int(input())
arr = input()
ans = {}
for i in arr:
    if 97<= ord(i) <= 122:
        if i in ans:
            ans[i] += 1
        else:
            ans[i] = 1
print(max(ans.values()))

