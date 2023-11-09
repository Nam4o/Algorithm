import sys
input = sys.stdin.readline

word = input()

check = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']

for i in check:
    word = word.replace(i, "")
print(word)