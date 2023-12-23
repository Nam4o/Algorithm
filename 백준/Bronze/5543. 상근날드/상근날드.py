arr = []
for i in range(5):
    arr.append(int(input()))
print(min(arr[:3]) + min(arr[3:]) - 50)