N = int(input())
word_count = N
for i in range(N):
    word = list(input())
    for j in range(len(word) - 1):
        if word[j] == word[j + 1]:
            pass
        elif word[j] in word[j+1:]:
            word_count -= 1
            break
print(word_count)