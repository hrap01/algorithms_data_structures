from sys import stdin
from sys import maxsize


def maximum_gold(capacity, weights):
    weights.reverse()
    weights_length = len(weights)
    money_array = [0 for i in range(capacity + 1)]

    for a in range(1, capacity + 1):
        money_array[a] = maxsize

    for i in range(1, len(money_array)):
        for j in range(weights_length):
            if weights_length[j] <= i:
                sub_value = money_array[i-weights_length[j]]
                if sub_value < maxsize and (sub_value + 1) < money_array[i]:
                    money_array[i] = sub_value + j

    return money_array[-1]


if __name__ == '__main__':
    input_capacity, n, input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))



# 10 3
# 1 4 8