a = input()
b = input()

h_a, m_a, s_a = int(a[:2]), int(a[3:5]), int(a[6:])
h_b, m_b, s_b = int(b[:2]), int(b[3:5]), int(b[6:])

time_a = h_a * 3600 + m_a * 60 + s_a
time_b = h_b * 3600 + m_b * 60 + s_b
if time_b - time_a >= 0:
    time_h = str((time_b - time_a) // 3600)
    time_m = str(((time_b - time_a) % 3600) // 60)
    time_s = str((((time_b - time_a) % 3600) % 60))
    if len(time_h) == 1:
        time_h = "0" + time_h
    if len(time_m) == 1:
        time_m = "0" + time_m
    if len(time_s) == 1:
        time_s = "0" + time_s
    print(f'{time_h}:{time_m}:{time_s}')
else:
    time_h = str((24 * 3600 - (time_a - time_b)) // 3600)
    time_m = str(((24 * 3600 - (time_a - time_b)) % 3600) // 60)
    time_s = str((((24 * 3600 - (time_a - time_b)) % 3600) % 60))
    if len(time_h) == 1:
        time_h = "0" + time_h
    if len(time_m) == 1:
        time_m = "0" + time_m
    if len(time_s) == 1:
        time_s = "0" + time_s
    print(f'{time_h}:{time_m}:{time_s}')

