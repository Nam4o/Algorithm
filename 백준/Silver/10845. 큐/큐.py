import sys
input = sys.stdin.readline

N = int(input())


my_list = []


for i in range(N):
    text = list(map(str, input().split()))
    
    if text[0] == 'push':
        my_list.append(int(text[1]))
        # print(my_list)
    elif text[0] == 'pop':
        if my_list == []:
            print(-1)
        else:
            a = my_list.pop(0)
            print(a)
            # my_list.pop()
    elif text[0] == 'size':
        print(len(my_list))
    elif text[0] == 'empty':
        if my_list == []:
            print(1)
        else:
            print(0)
    elif text[0] == 'front':
        if my_list == []:
            print(-1)
        else:
            print(my_list[0])
    elif text[0] == 'back':
        if my_list == []:
            print(-1)
        else:
            print(my_list[len(my_list)-1])
    