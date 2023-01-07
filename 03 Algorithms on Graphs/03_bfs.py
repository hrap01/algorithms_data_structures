def distance(adj, start, stop):
    distance_counting = [-1 for x in range(len(adj))]
    grey_value = [start]
    distance_counting[start] = 0

    while grey_value:
        current_value = grey_value.pop(0)
        for b in adj[current_value]:
            if distance_counting[b] == -1:
                grey_value.append(b)
                distance_counting[b] = distance_counting[current_value] + 1

    return distance_counting[stop]


if __name__ == '__main__':
    input1 = (input().split())
    nr_vertices, nr_edges = int(input1[0]), int(input1[1])
    vertices_split = [(input().split()) for i in range(nr_edges)]
    edges = [(int(i[0]), int(i[1])) for i in vertices_split]
    input2 = (input().split())
    start, stop = int(input2[0]), int(input2[1])
    adj = [[] for _ in range(nr_vertices)]
    start, stop = start - 1, stop - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(distance(adj, start, stop))
