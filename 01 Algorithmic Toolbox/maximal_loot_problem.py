def price_weight_ratio(price_sort: list, weight_sort: list) -> list:
    price_weight_list = []
    for i in range(0, len(price_sort)):
        ratio = price_sort[i]/weight_sort[i]
        price_weight_list.append(ratio)
    return price_weight_list

def bubble_sort(price_weight_list: list, price_item_input: list, weight_item_input: list):
    i = 0
    if price_weight_list is not None:
        while i < len(price_weight_list) - 1:
            if price_weight_list[i] >= price_weight_list[i + 1]:
                i += 1
            else:
                back_value = 1
                for j in range(0, len(price_weight_list) - back_value):
                    if price_weight_list[j] < price_weight_list[j + 1]:
                        price_weight_list[j], price_weight_list[j + 1] = price_weight_list[j + 1], price_weight_list[j]
                        price_item_input[j], price_item_input[j + 1] = price_item_input[j + 1], price_item_input[j]
                        weight_item_input[j], weight_item_input[j + 1] = weight_item_input[j + 1], weight_item_input[j]
                    back_value += 1
                    i = 0
    return price_weight_list, price_item_input, weight_item_input


def loop_solution(W: int, weight_item_input: list, price_item_input: list):
    if len(weight_item_input) != len(price_item_input):
        raise ValueError('lenght of weight input and price input needs to be the same')

    price_weight_list = price_weight_ratio(price_item_input, weight_item_input)
    price_weight_list_sorted, price_item_input_sorted, weight_item_input_sorted = bubble_sort(price_weight_list, price_item_input, weight_item_input)

    total_loot = []
    loop_count = 0
    while W > 0:
        if loop_count > len(weight_item_input_sorted):
            break
        for i in range(0, len(weight_item_input_sorted)):
            while W:
                if W >= weight_item_input_sorted[i]:
                    total_loot.append(price_item_input_sorted[i])
                    W -= weight_item_input_sorted[i]
                else:
                    loop_count += 1
                    break

    return total_loot


if __name__ == '__main__':
    W = int(input('weight of backpack: '))
    weight_item_input = list(map(int, input('weight of items: ').split()))
    price_item_input = list(map(int, input('price of items: ').split()))
    print(loop_solution(W, weight_item_input, price_item_input))