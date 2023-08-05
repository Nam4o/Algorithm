N = int(input())

members = []

for i in range(N):
    age, name = input().split()
    age = int(age)
    someone = [age, name]
    members.append(someone)

members.sort(key = lambda x : x[0])
for i in range(N):
    print(members[i][0], members[i][1])
