from collections import deque
import sys

input = sys.stdin.readline

N, d, k, c = map(int, input().split())

arr = [int(input()) for _ in range(N)]

dish = {}

unique_count = 0  # 유니크한 음식 수를 추적

queue = deque()

mx = 0

for i in range(k):
    queue.append(arr[i])
    if arr[i] in dish:
        dish[arr[i]] += 1
    else:
        dish[arr[i]] = 1
        unique_count += 1



if unique_count >= mx:
    if c in dish and dish[c] > 0:
        mx = unique_count
    else:
        mx = unique_count + 1

i = k

while i - k < N:
    tmp = queue.popleft()
    dish[tmp] -= 1
    if dish[tmp] == 0:
        unique_count -= 1

    queue.append(arr[i % N])
    if arr[i % N] in dish:
        if dish[arr[i % N]] == 0:
            unique_count += 1
        dish[arr[i % N]] += 1

    else:
        dish[arr[i % N]] = 1
        unique_count += 1
    if unique_count >= mx:
        if c in dish and dish[c] > 0:
            mx = unique_count
        else:
            mx = unique_count + 1



    i += 1

print(mx)
