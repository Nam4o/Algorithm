import sys
input = sys.stdin.readline

N, M = map(int, input().split())

word_dict = {}

for i in range(N):
    a = input().strip()
    if len(a) >= M:
        if a in word_dict:
            word_dict[a] += 1
        else:
            word_dict[a] = 1
word_len = max(word_dict.values())
ans = [[] for _ in range(word_len + 1)]

for j in word_dict:
    ans[-word_dict[j]].append(j)

for t in ans:
    if t:
        t.sort()
        t.sort(key=lambda x: len(x), reverse=True)
        for w in t:
            print(w)