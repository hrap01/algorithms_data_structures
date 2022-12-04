def majority_element_naive(elements: list):
    highest_value = 0
    comparison_value = 0
    comparison_length = len(elements)/2
    for number in elements:
        for value in elements:
            if number == value:
                comparison_value += 1
                #elements.remove(value)
        if comparison_value > highest_value:
            highest_value = comparison_value
            comparison_value = 0
        else:
            comparison_value = 0
    if highest_value > comparison_length:
        return 1
    else:
        return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_naive(input_elements))
