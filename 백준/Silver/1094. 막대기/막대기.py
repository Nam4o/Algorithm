base = int(input())

stick = 64

stick_list = [64]


for i in range(0, 7):
    if sum(stick_list)>= base:
        input_num = stick // (2**(i))
        if sum(stick_list) == base:
            break
        del stick_list[-1]
        if sum(stick_list) >= base:
            del stick_list[-1]
        stick_list.append(input_num)
        i += 1
    else:
        if sum(stick_list) == base:
            break
        stick_list.append(input_num)
        if sum(stick_list) >= base:
            input_num = stick // (2**(i))
            del stick_list[-1]
            stick_list.append(input_num)
        else:
            if sum(stick_list) == base:
                break
            stick_list.append(input_num)
            if sum(stick_list) >= base:
                input_num = stick // (2**(i))
                del stick_list[-1]
                stick_list.append(input_num)
            else:
                if sum(stick_list) == base:
                    break
                stick_list.append(input_num)
        if sum(stick_list) == base:
            break
        stick_list.append(input_num)
print(len(stick_list))