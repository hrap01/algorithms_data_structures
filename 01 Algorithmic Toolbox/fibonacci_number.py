def fibonacci_number(n):
    #fibonacci_list = [0,1]
    i = 1
    n_1, n_2 = 1, 0
    if n <= 1:
        return n
    else:
        while i < n:
            sum_n = n_1 + n_2
            n_2 = n_1
            n_1 = sum_n
            #fibonacci_list.append(sum_n)
            i += 1
    return sum_n


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
