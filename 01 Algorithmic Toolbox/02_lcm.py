def lcm(a, b):
    a_ = a
    b_ = b
    while b != 0:
        (a, b) = (b, a % b)
    return int(a_*b_/a)


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))

