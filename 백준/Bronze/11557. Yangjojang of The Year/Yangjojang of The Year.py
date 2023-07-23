tc = int(input())


for t in range(tc):
    school_nubers = int(input())
    school_list = []
    numbers = []
    schools = []
    for i in range(school_nubers):
        A , B = map(str, input().split())
        int_b = int(B)


        numbers.append(int_b)
        schools.append(A)
    for x in range(len(numbers)):
        if numbers[x] == max(numbers):
            print(schools[x])
        else:
            continue        