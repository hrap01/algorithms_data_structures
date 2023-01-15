from sys import maxsize
import math


def minimum_distance(data, n):
    distance = [[0] * n for _ in range(n)]
    adj = [[] for _ in range(n)]
    for i in range(n):
        adj[i] = list(v for v in range(n) if v != i)
        for j in range(n):
            if i != j:
                x = math.sqrt(math.pow(int(data[i][0]) - int(data[j][0]), 2) + math.pow(int(data[i][1]) - int(data[j][1]), 2))
                distance[i][j] = x
                distance[j][i] = x

    connecting_points(adj, distance, n)


def connecting_points(adj, distance, n):
    result = 0.
    X = set()
    X.add(0)

    while len(X) != n:
        crossing = set()
        for u in X:
            for v in adj[u]:
                if v not in X:
                    crossing.add((u, v))
        edge = sorted(crossing, key=lambda e: distance[e[0]][e[1]])[0]
        result += distance[edge[0]][edge[1]]
        X.add(edge[1])

    return print("{0:.9f}".format(result))


if __name__ == '__main__':
    n = int(input())
    data = [(input().split()) for i in range(n)]
    cost = [maxsize for _ in range(n)]
    minimum_distance(data, n)

