import sys

def lists(adj):
    recursion_stack = [False for x in range(len(adj))]
    visited = [False for x in range(len(adj))]
    for node in range(len(adj)):
        if visited[node] is False:
            looking_for_cycle(adj, recursion_stack, visited, node)
    return 0

def looking_for_cycle(adj, recursion_stack, visited, v):
    recursion_stack[v] = True
    visited[v] = True
    for a in adj[v]:
        if visited[a] is False:
            looking_for_cycle(adj, recursion_stack, visited, a)
        elif recursion_stack[a]:
            print(1)
            sys.exit()

    recursion_stack[v] = False

if __name__ == '__main__':
    input1 = (input().split())
    nr_vertices, nr_edges = int(input1[0]), int(input1[1])
    vertices_split = [(input().split()) for i in range(nr_edges)]
    edges = [(int(i[0]), int(i[1])) for i in vertices_split]
    adj = [[] for _ in range(nr_vertices)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(lists(adj))



