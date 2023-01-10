def min_value(value, visited):
    min_value_int = len(visited)
    min_distance = 9223372036854775807

    for i in range(min_value_int):
        if visited[i] is False and value[i] < min_distance:
            min_value_int = i
            min_distance = value[i]

    return min_value_int


def distance(adj, cost, start, stop):
    visited = [False for x in range(len(adj))]
    value = [9223372036854775807 for x in range(len(adj))]
    value[start] = 0

    for j in range((len(adj)-1)):
        minimal = min_value(value, visited)
        if minimal == len(adj):
            break
        visited[minimal] = True

        i = 0  # magic variable
        for u in adj[minimal]:
            if not visited[u] and value[u] > value[minimal] + cost[minimal][i]:
                value[u] = value[minimal] + cost[minimal][i]
            i += 1

    return value[stop] if value[stop] != 9223372036854775807 else -1


if __name__ == '__main__':
    input1 = (input().split())
    nr_vertices, nr_edges = int(input1[0]), int(input1[1])
    vertices_split = [(input().split()) for i in range(nr_edges)]
    edges = [((int(i[0]), int(i[1])), int(i[2])) for i in vertices_split]
    input2 = (input().split())
    start, stop = int(input2[0]), int(input2[1])
    adj = [[] for _ in range(nr_vertices)]
    cost = [[] for _ in range(nr_vertices)]
    start, stop = start - 1, stop - 1
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(distance(adj, cost, start, stop))
