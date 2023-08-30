while True:
    arr = input()
    if arr == '0':
        break
    if arr == arr[::-1]:
        print('yes')
    else:
        print('no')