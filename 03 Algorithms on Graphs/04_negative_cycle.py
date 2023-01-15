from sys import maxsize

def negative_cycle(adj, cost):
    value = [maxsize for x in range(len(adj))]
    value[0] = 0

    for _ in range(len(adj) - 1):
        for i in range(len(adj)):
            next = 0
            for j in adj[i]:
                if value[j] > value[i] + cost[i][next]:
                    value[j] = value[i] + cost[i][next]
                next += 1

    for i in range(len(adj) - 1):
        next = 0
        for j in adj[i]:
            if value[j] > value[i] + cost[i][next]:
                return 1
            next += 1

    return 0


if __name__ == '__main__':
    input1 = (input().split())
    nr_vertices, nr_edges = int(input1[0]), int(input1[1])
    vertices_split = [(input().split()) for i in range(nr_edges)]
    edges = [((int(i[0]), int(i[1])), int(i[2])) for i in vertices_split]
    adj = [[] for _ in range(nr_vertices)]
    cost = [[] for _ in range(nr_vertices)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
