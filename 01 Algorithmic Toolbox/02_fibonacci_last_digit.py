
def fibonacci_last_digit(n):
    current, previous = 1, 0
    if n <= 1:
        return n
    for _ in range(n - 1):
        previous, current = current, previous + current
    return str(current)[-1]



if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))
