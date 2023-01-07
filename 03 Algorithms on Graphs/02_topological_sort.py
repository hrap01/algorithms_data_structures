def lists(adj):
    number_list = []
    visited = [False for x in range(len(adj))]
    for node in range(len(adj)):
        if visited[node] is False:
            looking_for_cycle(adj, visited, node, number_list)
    return number_list

def looking_for_cycle(adj, visited, v, number_list):
    visited[v] = True
    for a in adj[v]:
        if visited[a] is False:
            looking_for_cycle(adj, visited, a, number_list)
    number_list.append(v)
    return number_list

if __name__ == '__main__':
    input1 = (input().split())
    nr_vertices, nr_edges = int(input1[0]), int(input1[1])
    vertices_split = [(input().split()) for i in range(nr_edges)]
    edges = [(int(i[0]), int(i[1])) for i in vertices_split]
    adj = [[] for _ in range(nr_vertices)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = lists(adj)
    for x in reversed(order):
        print(x + 1, end=' ')


