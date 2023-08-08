word = input()

empty = {}

word = word.upper()

for i in word:
    if i not in empty:
        empty.setdefault(i, word.count(i))

result = [x for x in empty.keys() if empty[x] == max(empty.values())]

if len(result) >= 2:
    print('?')
else:
    print(*result)

