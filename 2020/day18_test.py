FILENAME = "inputs/day18.txt"


def get_expressions(FILENAME=FILENAME):
    expressions = list()

    with open(FILENAME, "r") as f:
        for line in f:
            expressions.append(line[:-1] if line[-1] == '\n' else line)

    return expressions


def evaluate(expression, operators, operations):
    operation_stack = list()
    number_stack = list()

    expression_list = expression[:-1].split(" ") if expression[-1] == '\n' else expression.split(" ")

    for string in expression_list:
        if string in operators.keys():
            while len(operation_stack) > 0 and operators[string] <= operators[operation_stack[-1]]:
                operation = operation_stack.pop()
                num1 = number_stack.pop()
                num2 = number_stack.pop()

                result = operations[operation](num1, num2)
                number_stack.append(result)

            operation_stack.append(string)
        elif string[0] == '(':
            while string[0] == '(':
                operation_stack.append('(')
                string = string[1:]
            number_stack.append(int(string))

        elif string[-1] == ')':
            number_stack.append(int(string[:string.index(')')]))

            while string[-1] == ')':
                string = string[:-1]
                operation = ')'

                while operation != '(':
                    operation = operation_stack.pop()

                    if operation == '(':
                        break

                    num1 = number_stack.pop()
                    num2 = number_stack.pop()

                    result = operations[operation](num1, num2)
                    number_stack.append(result)
        else:
            number_stack.append(int(string))

    while len(operation_stack) > 0:
        operation = operation_stack.pop()
        num1 = number_stack.pop()
        num2 = number_stack.pop()

        result = operations[operation](num1, num2)

        number_stack.append(result)

    return number_stack[0]


operations = {
    '+': lambda num1, num2: num1 + num2,
    '*': lambda num1, num2: num1 * num2
}

# For part 1
operators_part_1 = {
    '+': 1,
    '*': 1,
    '(': 0
}

# For part 2
operators_part_2 = {
    '+': 2,
    '*': 1,
    '(': 0
}

expressions = get_expressions()

sum_part_1 = 0
sum_part_2 = 0
for expression in expressions:
    sum_part_1 += evaluate(expression, operators_part_1, operations)
    sum_part_2 += evaluate(expression, operators_part_2, operations)

print("Part 1 sum {}".format(sum_part_1))
print("Part 2 sum {}".format(sum_part_2))