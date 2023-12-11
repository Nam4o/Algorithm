def solution(expression):
    stack1 = []
    stack2 = []

    tmp = ''
    idx = 0
    while idx < len(expression):

        if expression[idx] not in '*+-':
            tmp += expression[idx]
        else:
            stack1.append(int(tmp))
            stack2.append(expression[idx])
            tmp = ''
        idx += 1
        if idx == len(expression):
            stack1.append(int(tmp))

    check = set(stack2)
    check = list(check)

    mx = 0

    if len(check) == 3:
        for tc in range(6):
            new1 = stack1[:]
            new2 = stack2[:]
            t = 0
            while new2:
                if tc == 0:
                    if "*" in new2:
                        if new2[t] == "*":
                            new1[t] *= new1.pop(t + 1)
                            new2.pop(t)
                        else:
                            t += 1
                        if "*" not in new2:
                            t = 0
                    else:

                        if "+" in new2:
                            if new2[t] == "+":
                                new1[t] += new1.pop(t + 1)
                                new2.pop(t)
                            else:
                                t += 1
                            if "+" not in new2:
                                t = 0
                        else:
                            new1[t] -= new1.pop(t + 1)
                            new2.pop(t)
                elif tc == 1:
                    if "+" in new2:
                        if new2[t] == "+":
                            new1[t] += new1.pop(t + 1)
                            new2.pop(t)
                        else:
                            t += 1
                        if "+" not in new2:
                            t = 0
                    else:

                        if "*" in new2:
                            if new2[t] == "*":
                                new1[t] *= new1.pop(t + 1)
                                new2.pop(t)
                            else:
                                t += 1
                            if "*" not in new2:
                                t = 0
                        else:
                            new1[t] -= new1.pop(t + 1)
                            new2.pop(t)
                elif tc == 2:
                    if "-" in new2:
                        if new2[t] == "-":
                            new1[t] -= new1.pop(t + 1)
                            new2.pop(t)
                        else:
                            t += 1
                        if "-" not in new2:
                            t = 0
                    else:

                        if "*" in new2:
                            if new2[t] == "*":
                                new1[t] *= new1.pop(t + 1)
                                new2.pop(t)
                            else:
                                t += 1
                            if "*" not in new2:
                                t = 0
                        else:
                            new1[t] += new1.pop(t + 1)
                            new2.pop(t)
                elif tc == 3:
                    if "-" in new2:
                        if new2[t] == "-":
                            new1[t] -= new1.pop(t + 1)
                            new2.pop(t)
                        else:
                            t += 1
                        if "-" not in new2:
                            t = 0
                    else:

                        if "+" in new2:
                            if new2[t] == "+":
                                new1[t] += new1.pop(t + 1)
                                new2.pop(t)
                            else:
                                t += 1
                            if "+" not in new2:
                                t = 0
                        else:
                            new1[t] *= new1.pop(t + 1)
                            new2.pop(t)
                elif tc == 4:
                    if "+" in new2:
                        if new2[t] == "+":
                            new1[t] += new1.pop(t + 1)
                            new2.pop(t)
                        else:
                            t += 1
                        if "+" not in new2:
                            t = 0
                    else:

                        if "-" in new2:
                            if new2[t] == "-":
                                new1[t] -= new1.pop(t + 1)
                                new2.pop(t)
                            else:
                                t += 1
                            if "-" not in new2:
                                t = 0
                        else:
                            new1[t] *= new1.pop(t + 1)
                            new2.pop(t)
                if tc == 5:
                    if "*" in new2:
                        if new2[t] == "*":
                            new1[t] *= new1.pop(t + 1)
                            new2.pop(t)
                        else:
                            t += 1
                        if "*" not in new2:
                            t = 0
                    else:

                        if "-" in new2:
                            if new2[t] == "-":
                                new1[t] -= new1.pop(t + 1)
                                new2.pop(t)
                            else:
                                t += 1
                            if "-" not in new2:
                                t = 0
                        else:
                            new1[t] += new1.pop(t + 1)
                            new2.pop(t)

            if abs(new1[0]) > mx:
                mx = abs(new1[0])

    elif len(check) == 2:
        for tc in range(6):
            new1 = stack1[:]
            new2 = stack2[:]
            t = 0
            while new2:
                if tc == 0 and "*" in check:
                    if "*" in new2:
                        if new2[t] == "*":
                            new1[t] *= new1.pop(t + 1)
                            new2.pop(t)
                        else:
                            t += 1
                        if "*" not in new2:
                            t = 0
                    else:

                        if "+" in check:

                            new1[t] += new1.pop(t + 1)
                            new2.pop(t)
                            if not new2:
                                if abs(new1[0]) > mx:
                                    mx = abs(new1[0])

                        else:
                            new1[t] -= new1.pop(t + 1)
                            new2.pop(t)
                            if not new2:
                                if abs(new1[0]) > mx:
                                    mx = abs(new1[0])
                elif tc == 1 and "+" in check:
                    if "+" in new2:
                        if new2[t] == "+":
                            new1[t] += new1.pop(t + 1)
                            new2.pop(t)
                        else:
                            t += 1
                        if "+" not in new2:
                            t = 0
                    else:

                        if "*" in check:
                            new1[t] *= new1.pop(t + 1)
                            new2.pop(t)
                            if not new2:
                                if abs(new1[0]) > mx:
                                    mx = abs(new1[0])

                        else:
                            new1[t] -= new1.pop(t + 1)
                            new2.pop(t)
                            if not new2:
                                if abs(new1[0]) > mx:
                                    mx = abs(new1[0])
                elif tc == 2 and "-" in check:
                    if "-" in new2:
                        if new2[t] == "-":
                            new1[t] -= new1.pop(t + 1)
                            new2.pop(t)
                        else:
                            t += 1
                        if "-" not in new2:
                            t = 0
                    else:
                        if "*" in check:
                            new1[t] *= new1.pop(t + 1)
                            new2.pop(t)
                            if not new2:
                                if abs(new1[0]) > mx:
                                    mx = abs(new1[0])
                        else:
                            new1[t] += new1.pop(t + 1)
                            new2.pop(t)
                            if not new2:
                                if abs(new1[0]) > mx:
                                    mx = abs(new1[0])
                elif tc == 3 and "-" in check:
                    if "-" in new2:
                        if new2[t] == "-":
                            new1[t] -= new1.pop(t + 1)
                            new2.pop(t)
                        else:
                            t += 1
                        if "-" not in new2:
                            t = 0
                    else:
                        if "+" in check:
                            new1[t] += new1.pop(t + 1)
                            new2.pop(t)
                            if not new2:
                                if abs(new1[0]) > mx:
                                    mx = abs(new1[0])
                        else:
                            new1[t] *= new1.pop(t + 1)
                            new2.pop(t)
                            if not new2:
                                if abs(new1[0]) > mx:
                                    mx = abs(new1[0])
                elif tc == 4 and "*" in check:
                    if "*" in new2:
                        if new2[t] == "*":
                            new1[t] *= new1.pop(t + 1)
                            new2.pop(t)

                        else:
                            t += 1
                        if "*" not in new2:
                            t = 0
                    else:

                        if "-" in check:

                            new1[t] -= new1.pop(t + 1)
                            new2.pop(t)
                            if not new2:
                                if abs(new1[0]) > mx:
                                    mx = abs(new1[0])

                        else:
                            new1[t] += new1.pop(t + 1)
                            new2.pop(t)
                            if not new2:
                                if abs(new1[0]) > mx:
                                    mx = abs(new1[0])
                elif tc == 5 and "+" in check:
                    if "+" in new2:
                        if new2[t] == "+":
                            new1[t] += new1.pop(t + 1)
                            new2.pop(t)
                        else:
                            t += 1
                        if "+" not in new2:
                            t = 0
                    else:

                        if "-" in check:
                            new1[t] -= new1.pop(t + 1)
                            new2.pop(t)
                            if not new2:
                                if abs(new1[0]) > mx:
                                    mx = abs(new1[0])

                        else:
                            new1[t] *= new1.pop(t + 1)
                            new2.pop(t)
                            if not new2:
                                if abs(new1[0]) > mx:
                                    mx = abs(new1[0])

                else:
                    break


    elif len(check) == 1:
        new1 = stack1[:]
        new2 = stack2[:]

        while new2:
            if check[-1] == "*":
                new1[0] *= new1.pop(1)
                new2.pop()
            elif check[-1] == "+":
                new1[0] += new1.pop(1)
                new2.pop()
            else:
                new1[0] -= new1.pop(1)
                new2.pop()
        if abs(new1[0]) > mx:
            mx = abs(new1[0])

    answer = 0
    return mx

