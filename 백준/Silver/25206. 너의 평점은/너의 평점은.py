amount = 0

grade = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5,
         'B0': 3.0, 'C+': 2.5, 'C0': 2.0,
         'D+':1.5 , 'D0': 1.0, 'F': 0.0}
count = 0

for i in range(20):
    X, Y, Z = input().split()

    Y = float(Y)
    if Z == 'P':
        continue
    else:
        amount += Y * grade[Z]
        count += Y

print(round((amount / count), 6))
