def max_pairwise(input_numbers: list):
    second_highest = None
    highest = None
    for i in input_numbers:
        if highest is None:
            highest = i
        elif i > highest:
            second_highest = highest
            highest = i
        elif highest >= i and (second_highest is None or i > second_highest):
            second_highest = i
    return highest*second_highest



if __name__ == '__main__':
    a = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise(input_numbers))