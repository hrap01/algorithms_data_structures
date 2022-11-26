def money_change(a: int) -> list:
    change = []
    denominators = [10, 5, 1]
    while a > 0:
        for b in denominators:
            while a:
                if a >= b:
                    change.append(b)
                    a -= b
                else:
                    break
    return change


if __name__ == '__main__':
    a = int(input())
    print(money_change(a))

