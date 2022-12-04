
def maximum_gold(capacity, n, weight):
    gold_array = [[0 for x in range(capacity + 1)] for x in range(n + 1)]
    weight.reverse()

    for i in range(n + 1):
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                gold_array[i][j] = 0
            elif weight[i-1] <= j:
                gold_array[i][j] = max(gold_array[i-1][j], weight[i - 1] + gold_array[i - 1][j - weight[i-1]])
            else:
                gold_array[i][j] = gold_array[i-1][j]
    return gold_array[-1][-1]



if __name__ == '__main__':
    input_capacity, n = list(map(int, input().split()))
    input_weights = list(map(int, input().split()))

    print(maximum_gold(input_capacity, n, input_weights))