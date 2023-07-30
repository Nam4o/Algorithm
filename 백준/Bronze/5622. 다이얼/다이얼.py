alpha = list(map(str, input()))


time = 0
for i in range(len(alpha)):
    if ord(alpha[i]) < 65:
        time += 2
    elif ord(alpha[i]) in range(65, 68):   #2
        time += 3
    elif ord(alpha[i]) in range(68, 71): #3
        time += 4
    elif ord(alpha[i]) in range(71, 74): #4
        time += 5
    elif ord(alpha[i]) in range(74, 77): #5
        time += 6
    elif ord(alpha[i]) in range(77, 80): #6
        time += 7
    elif ord(alpha[i]) in range(80, 84): #7
        time += 8
    elif ord(alpha[i]) in range(84, 87): #8
        time += 9
    elif ord(alpha[i]) in range(87, 101): #9
        time += 10
    else:
        time += 11

print(time)