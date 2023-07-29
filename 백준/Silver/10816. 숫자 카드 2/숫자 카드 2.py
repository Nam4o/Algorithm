
N = int(input())
base_number = list(map(int, input().split()))
M = int(input())
given_number = list(map(int, input().split()))

num_dict = {}

for i in given_number:
    
    num_dict[i] = 0
   



for i in base_number:
    if i not in num_dict:
        continue
    
    num_dict[i] += 1

for i in given_number:
    print(num_dict[i], end=' ')