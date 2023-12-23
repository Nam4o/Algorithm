def solution(m, musicinfos):


    target = []
    check = False


    for f in m:
        if f != "#":
            target.append(f)
        else:
            target[-1] += f


    print(target)

    answer = ""
    ans = []
    dictionary = {}
    cnt = 100
    for i in musicinfos:
        i = i.split(",")


        runtime = (int(i[1][:2]) * 60 + int(i[1][3:])) - (int(i[0][:2]) * 60 + int(i[0][3:]))

        tmp = []
        for j in i[3]:
            if j != "#":
                tmp.append(j)
            else:
                tmp[-1] += j
        if runtime >= len(tmp):
            dictionary[i[2]] = [tmp * (runtime // len(tmp)) + tmp[:runtime % len(tmp)], runtime, cnt]

        else:
            dictionary[i[2]] = [tmp[:runtime], runtime, cnt]
        cnt -= 1

    for t in dictionary:

        for w in range(len(dictionary[t][0])):
            if dictionary[t][0][w:w + len(target)] == target:

                # print(dictionary[t][w:w + len(target)])

                check = True
                ans.append([t, dictionary[t][1], dictionary[t][2]])


    if check == False:
        answer = "(None)"
    else:
        ans.sort(key=lambda x: (x[1], x[2]), reverse=True)

        answer = ans[0][0]

    return answer