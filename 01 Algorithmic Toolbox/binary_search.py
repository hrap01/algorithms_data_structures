def binary_search_list(keys: list, query: list) -> list:
    return_list = []
    max_number = len(keys) - 1
    min_number = 0
    for q in query:
        a = binary_search_number(query=query, q=q, min_number=min_number, max_number=max_number)
        return_list.append(a)
    return return_list


def binary_search_number(query: list, q: int, min_number: int, max_number: int):
    mid_number = round((max_number - min_number) / 2)
    if q == query[mid_number]:
        return mid_number
    elif q < mid_number:
        mid_number -= 1
        binary_search_number(query, q, min_number, max_number)
    else:
        mid_number += 1
        binary_search_number(query, q, min_number, max_number)


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
