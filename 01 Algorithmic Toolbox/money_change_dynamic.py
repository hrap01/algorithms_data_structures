from sys import maxsize

def change(money):
    coins_array = [4, 3, 1]
    coins_length = len(coins_array)
    money_array = [0 for i in range(money + 1)]

    for a in range(1, money + 1):
        money_array[a] = maxsize

    for i in range(1, len(money_array)):
        for j in range(coins_length):
            if coins_array[j] <= i:
                sub_value = money_array[i-coins_array[j]]
                if sub_value < maxsize and (sub_value + 1) < money_array[i]:
                    money_array[i] = sub_value + 1

    return money_array[-1]


if __name__ == '__main__':
    m = int(input())
    print(change(m))
