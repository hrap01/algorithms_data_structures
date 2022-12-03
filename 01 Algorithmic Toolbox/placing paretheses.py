import math


def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def calculation(M, m, i, j, operators):
    min_value = math.inf
    max_value = -math.inf

    for k in range(i, j):
        a = evaluate(M[i][k], M[k+1][j], operators[k])
        b = evaluate(M[i][k], m[k+1][j], operators[k])
        c = evaluate(m[i][k], M[k+1][j], operators[k])
        d = evaluate(m[i][k], m[k+1][j], operators[k])
        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)
    return min_value, max_value


def maximum_value(operators, values):
    m = [[0 for x in range(len(values))] for x in range(len(values))]
    M = [[0 for x in range(len(values))] for x in range(len(values))]

    for i in range(len(values)):
        m[i][i] = values[i]
        M[i][i] = values[i]

    for s in range(1, len(values)):
        for i in range(0, len(values)-s):
            j = i + s
            m[i][j], M[i][j] = calculation(M, m, i, j, operators)

    return M[0][len(values)-1]


if __name__ == "__main__":
    input = input()
    operators, values = [], []

    for i in input:
        if i in ['+', '-', '*']:
            operators.append(i)
        else:
            values.append(int(i))

    print(maximum_value(operators, values))
