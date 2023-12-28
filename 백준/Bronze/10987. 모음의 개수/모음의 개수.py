cnt = 0
word = input()
for w in word:
    if w in "aeiou":
        cnt += 1
print(cnt)