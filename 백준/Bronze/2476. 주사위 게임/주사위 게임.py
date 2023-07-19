draw = int(input())

# draw_1, draw_2, draw_3 = map(int, input().split())

score = []
# max_score = draw_1, draw_2, draw_3
for i in range(0, draw):
    draw_1, draw_2, draw_3 = map(int, input().split())
    max_score = draw_1, draw_2, draw_3
    if draw_1 == draw_2 == draw_3:
        score.append(10000 + (draw_1 * 1000))
    elif draw_1 == draw_2 != draw_3:
        score.append(1000 + (draw_1 * 100))
    elif draw_1 != draw_2 == draw_3:
        score.append(1000 + (draw_2 * 100))
    elif draw_1 == draw_3 != draw_2:
        score.append(1000 + (draw_1 * 100))
    else:
        score.append(max(max_score) * 100)
    i += 1
    
print(max(score))    