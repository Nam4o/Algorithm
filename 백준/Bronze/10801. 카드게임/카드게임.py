a = list(map(int, input().split()))
b = list(map(int, input().split()))

cnt_a = 0
cnt_b = 0
for i in range(len(a)):
    if a[i] < b[i]:
        cnt_b += 1
    elif a[i] > b[i]:
        cnt_a += 1


if cnt_a > cnt_b:
    print("A")
elif cnt_a < cnt_b:
    print("B")
else:
    print("D")