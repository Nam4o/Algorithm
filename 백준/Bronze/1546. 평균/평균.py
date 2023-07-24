test = int(input())
num_list = list(map(int, input().split()))
mean_score = []
M = max(num_list)

for i in range(0, test):
    mean_score.append((num_list[i] / M)*(100))
print(sum(mean_score) / test)