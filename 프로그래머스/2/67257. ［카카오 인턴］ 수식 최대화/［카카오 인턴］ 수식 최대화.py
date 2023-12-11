def operate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b

def calculate(stack1, stack2, priority):
    for op in priority:
        temp_stack1 = []
        temp_stack2 = []
        while stack2:
            if stack2[0] == op:
                result = operate(stack1.pop(0), stack1.pop(0), op)
                stack1.insert(0, result)
                stack2.pop(0)
            else:
                temp_stack1.append(stack1.pop(0))
                temp_stack2.append(stack2.pop(0))

        stack1 = temp_stack1 + stack1
        stack2 = temp_stack2

    return abs(stack1[0])

def generate_priority(priority, operators, result):
    if len(priority) == len(operators):
        result.append(priority[:])
        return
    for op in operators:
        if op not in priority:
            priority.append(op)
            generate_priority(priority, operators, result)
            priority.pop()

def solution(expression):
    operators = ['+', '-', '*']
    priorities = []
    generate_priority([], operators, priorities)

    stack1 = []
    stack2 = []

    tmp = ''
    for char in expression:
        if char not in '*+-':
            tmp += char
        else:
            stack1.append(int(tmp))
            stack2.append(char)
            tmp = ''

    stack1.append(int(tmp))

    max_result = 0
    for priority in priorities:
        max_result = max(max_result, calculate(stack1[:], stack2[:], priority))

    return max_result

