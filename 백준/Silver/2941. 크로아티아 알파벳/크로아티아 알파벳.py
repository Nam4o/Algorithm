word = input()

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
trans = ['1', '2', '3', '4', '5', '6', '7', '8']

for i in range(8):
    if croatia[i] in word:
        word = word.replace(croatia[i], trans[i])
print(len(word))