N = int(input())

numbers = str(input())

blank = []

for i in range(N):
    blank.append(int(numbers[i]))

print(sum(blank))