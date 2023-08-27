T = int(input())

for tc in  range(1, T + 1):
    N = int(input())

    arr = list(map(int, input().split()))
    mn = -1
    for i in range(len(arr)):
        if i + 1 < len(arr):
            for j in range(i + 1, len(arr)):
                s = str(arr[i] * arr[j])
                for k in range(len(s) - 1):
                    if s[k + 1] < s[k]:
                        break
                    if k == len(s) - 2 and int(s) > mn:
                        mn = int(s)
                        
    print(f'#{tc} {mn}')