ans = []
for i in range(5):
    line = input()
    if "FBI" in line:
        ans.append(i + 1)
if ans != []:
    print(*ans)
else:
    print("HE GOT AWAY!")