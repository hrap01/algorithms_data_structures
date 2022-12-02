from sys import maxsize

def compute_operations(n):
    numbers_array = [3, 2, 1]
    numbers_length = len(numbers_array)
    outcome_array = [0 for i in range(n + 1)]

    for a in range(1, n + 1):
        outcome_array[a] = maxsize

    for i in range(1, len(outcome_array)):
        for j in range(numbers_length):
            if i % numbers_array[j] == 0:
                if (j == 0 or j == 1) and (i == 2 or i == 3):
                    int_value = int(i / numbers_array[j])
                    sub_value = int(outcome_array[int_value])-1
                    if sub_value < maxsize and (sub_value + 1) < outcome_array[i]:
                        outcome_array[i] = sub_value + 1
                elif j == 0 or j == 1:
                    int_value = int(i/numbers_array[j])
                    sub_value = int(outcome_array[int_value])
                    if sub_value < maxsize and (sub_value + 1) < outcome_array[i]:
                            outcome_array[i] = sub_value + 1
                else:
                    sub_value = outcome_array[i - numbers_array[j]]
                    if sub_value < maxsize and (sub_value + 1) < outcome_array[i]:
                        outcome_array[i] = sub_value + 1
    return outcome_array[-1]


if __name__ == '__main__':
    input_n = int(input())
    print(compute_operations(input_n))
    #print(len(output_sequence) - 1)
    #print(*output_sequence)
