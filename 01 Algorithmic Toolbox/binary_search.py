def binary_search_list(keys: list, query: list) -> list:
    return_list = []
    max_number = len(keys) - 1
    min_number = 0
    mid_number = (min_number + max_number) // 2
    for q in query:
        def binary_search_number(keys: list, q: int, min_number: int, max_number: int, mid_number: int):
            nonlocal return_list
            if q < keys[min_number]:
                return_list.append(-1)
            elif q > keys[max_number]:
                return_list.append(-1)
            elif q == keys[mid_number]:
                return_list.append(mid_number)
            elif q < keys[mid_number]:
                #max_number = mid_number
                binary_search_number(keys, q, min_number, max_number, mid_number-1)
            else:
                #min_number = mid_number
                binary_search_number(keys, q, min_number, max_number, mid_number+1)

        binary_search_number(keys=keys, q=q, min_number=min_number, max_number=max_number, mid_number=mid_number)
    return return_list




if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

print((binary_search_list(input_keys, input_queries)))
    #for q in input_queries:
    #    print(binary_search_list(input_keys, q), end=' ')
