x, y, w, h = map(int, input().split())
a = []
a.append(abs(w - x))
a.append(abs(0 - x))
a.append(abs(h - y))
a.append(abs(0 - y))
print(min(a))