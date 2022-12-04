def highest_number(a_list: list) -> int:
    highest = None
    for number in a_list:
        if highest is None:
            highest = number
        elif number > highest:
            highest = number
    return highest


def max_dot_product(n: int, first_sequence: list, second_sequence: list) -> int:
    i=0
    max_product = 0
    if n == 0:
        return 0
    while len(first_sequence) > 0:
        a = highest_number(first_sequence)
        b = highest_number(second_sequence)
        max_product += a*b
        first_sequence.remove(a)
        second_sequence.remove(b)
    return max_product


if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(n, prices, clicks))

