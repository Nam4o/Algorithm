import sys
input = sys.stdin.readline

N = int(input())

new_list = []
for i in range(N):
    number = int(input())
    new_list.append(number)

new_list.sort()

for i in range(len(new_list)):
    print(new_list[i])
