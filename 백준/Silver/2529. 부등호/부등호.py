import sys
input = sys.stdin.readline

def findMX():
    cnt_mx = 0
    i = 0
    while i != len(arr):
        if arr[i] == '>':
            if cnt_mx == 0:
                mx.append(numb_mx.pop())
                i += 1
            while cnt_mx != 0:
                mx.append(numb_mx.pop(- cnt_mx - 1))
                cnt_mx -= 1
        elif arr[i] == '<':
            cnt_mx += 1
            i += 1
    while True:
        if cnt_mx == 0:
            mx.append(numb_mx[-1])
            break
        mx.append(numb_mx.pop(- cnt_mx - 1))
        cnt_mx -= 1

    return mx


def findMN():
    cnt_mn = 0
    j = 0
    while j != len(arr):
        if arr[j] == '<':
            if cnt_mn == 0:
                mn.append(numb_mn.pop(0))
                j += 1
            while cnt_mn != 0:
                mn.append(numb_mn.pop(0 + cnt_mn))
                cnt_mn -= 1
        elif arr[j] == '>':
            cnt_mn += 1
            j += 1
    while True:
        if cnt_mn == 0:
            mn.append(numb_mn.pop(0))
            break
        mn.append(numb_mn.pop(0 + cnt_mn))
        cnt_mn -= 1

    return mn

k = int(input())

arr = list(input().split())
left = arr.count('>')
right = arr.count('<')

numb_mx = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
numb_mn = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

mx = []
mn = []

findMX()
findMN()

mx = ''.join(mx)
mn = ''.join(mn)

print(mx)
print(mn)