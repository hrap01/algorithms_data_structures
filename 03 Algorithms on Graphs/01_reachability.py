import sys

def reach(adj, x, y):
    visited = [False for x in range(len(adj))]

    def dfs(x):
        visited[x] = True
        for w in adj[x]:
            if w == y:
                print(1)
                sys.exit(1)
            if visited[w] is False:
                dfs(w)
        return 0

    return dfs(x)



if __name__ == "__main__":
    input1 = (input().split())
    nr_vertices = int(input1[0])
    nr_edges = int(input1[1])
    vertices_split = [(input().split()) for i in range(nr_edges)]
    edges = [(int(i[0]), int(i[1])) for i in vertices_split]
    input2 = (input().split())
    start = int(input2[0])
    stop = int(input2[1])
    adj = [[] for _ in range(nr_vertices)]
    start, stop = start - 1, stop - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, start, stop))
