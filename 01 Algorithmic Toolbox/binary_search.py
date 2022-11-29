def binary_search_list(keys: list, query: list) -> str:
    return_list = []
    max_number = len(keys) - 1
    min_number = 0
    for q in query:
        def binary_search_number(keys: list, q: int, min_number: int, max_number: int):
            nonlocal return_list
            if max_number >= min_number:
                mid_number = (min_number + max_number) // 2
                if q == keys[mid_number]:
                    return_list.append(mid_number)
                elif q < keys[mid_number]:
                    binary_search_number(keys, q, min_number, mid_number-1)
                else:
                    binary_search_number(keys, q, mid_number+1, max_number)
            else:
                return_list.append(-1)
        binary_search_number(keys=keys, q=q, min_number=min_number, max_number=max_number)
    return ' '.join(str(n) for n in return_list)


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

print((binary_search_list(input_keys, input_queries)))
