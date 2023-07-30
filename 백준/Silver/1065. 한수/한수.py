N = int(input())


result = 0

if N < 100:
    result = N     
    

elif N <= 1000:
    for i in range(100, N+1):
        if int(str(i)[2]) != 0:
            if (int(str(i)[0]) + int(str(i)[2])) / 2 == int(str(i)[1]):
                result += 1
        elif int(str(i)[2]) < int(str(i)[1]) and int(str(i)[1]) < int(str(i)[0]) :
            if (int(str(i)[0]) + int(str(i)[2])) / 2 == int(str(i)[1]):
                result += 1
        else:
            continue
    result += 99
print(result)    

