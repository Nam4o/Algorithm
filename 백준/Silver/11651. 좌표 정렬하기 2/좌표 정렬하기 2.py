N = int(input())

new_list = []

for i in range(N):
    x, y = map(int,input().split())
    new_list.append([y, x])
    
a = sorted(new_list)

for i in range(len(new_list)):
    print(str(a[i][1]), str(a[i][0]))
