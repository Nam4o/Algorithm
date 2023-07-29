total_student = []

for i in range(1, 31):
    total_student.append(i)

my_list = []

for i in range(1, 29):
    number = int(input())
    my_list.append(number)
    
my_list.sort()

result = list(set(total_student) - set(my_list))
result.sort()
a = result.pop(0)
b = result.pop(0)

print(a)
print(b)