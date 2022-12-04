from sys import maxsize

def compute_operations(n):
    numbers_array = [3, 2, 1]
    numbers_length = len(numbers_array)
    outcome_array = [0 for i in range(n + 1)]
    outcome_number_array = [0 for i in range(n + 1)]
    list_of_numbers = []

    for a in range(1, n + 1):
        outcome_array[a] = maxsize

    if n == 1:
        outcome_array = [0]

    for i in range(1, len(outcome_array)):
        for j in range(numbers_length):
            if i % numbers_array[j] == 0:
                if (j == 0 or j == 1) and (i == 2 or i == 3):
                    int_value = int(i / numbers_array[j])
                    sub_value = int(outcome_array[int_value])-1
                    if sub_value < maxsize and (sub_value + 1) < outcome_array[i]:
                        outcome_array[i] = sub_value + 1
                        outcome_number_array[i] = numbers_array[j]
                elif j == 0 or j == 1:
                    int_value = int(i/numbers_array[j])
                    sub_value = int(outcome_array[int_value])
                    if sub_value < maxsize and (sub_value + 1) < outcome_array[i]:
                        outcome_array[i] = sub_value + 1
                        outcome_number_array[i] = numbers_array[j]
                else:
                    sub_value = outcome_array[i - numbers_array[j]]
                    if sub_value < maxsize and (sub_value + 1) < outcome_array[i]:
                        outcome_array[i] = sub_value + 1
                        outcome_number_array[i] = numbers_array[j]

    list_of_numbers.append(n)
    for number in range(outcome_array[-1]):
        if outcome_number_array[n] == 1:
            n = n - 1
            list_of_numbers.append(n)
        elif outcome_number_array[n] == 3:
            n = int(n/3)
            list_of_numbers.append(n)
        else:
            n = int(n / 2)
            list_of_numbers.append(n)

    list_of_numbers.reverse()
    return outcome_array[-1], ' '.join(str(n) for n in list_of_numbers)


if __name__ == '__main__':
    input_n = int(input())
    a = (compute_operations(input_n))
    print(a[0])
    print(a[1])
