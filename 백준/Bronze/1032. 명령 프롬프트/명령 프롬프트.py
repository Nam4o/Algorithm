t = int(input())
start = list(input())
if t > 1:
    for tc in range(1, t):
        file = input()
        for i in range(len(file)):
            if start[i] != file[i]:
                start[i] = "?"

print("".join(start))