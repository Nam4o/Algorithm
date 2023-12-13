def solution(phone_book):
    phone_book.sort(key=lambda x : len(x))

    check = True

    hs = set()
    hs.add(phone_book[0])
    for i in range(1, len(phone_book)):
        if not check:
            break
        for j in range(len(phone_book[0]), len(phone_book[i])):
            tmp = phone_book[i][:j]
            if tmp in hs:
                check = False
                break
        hs.add(phone_book[i])

    return check