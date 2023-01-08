import sys
from queue import PriorityQueue


class Queue:
    def __init__(self, id_info, time=0):
        self.id_info = id_info
        self.time = time

    # def __lt__(self, other):
    #     if self.time > other.time:
    #         return self.id_info < other.id_info
    #     return self.time < other.time


class Distance:
    def read_data(self):
        input1 = (input().split())
        self.nr_vertices, self.nr_edges = int(input1[0]), int(input1[1])
        self.vertices_split = [(input().split()) for i in range(self.nr_edges)]
        self.edges = [((int(i[0]), int(i[1])), int(i[2])) for i in self.vertices_split]
        input2 = (input().split())
        self.start, self.stop = int(input2[0]), int(input2[1])
        self.adj = [[] for _ in range(self.nr_vertices)]
        self.cost = [[] for _ in range(self.nr_vertices)]
        self.start, self.stop = self.start - 1, self.stop - 1
        for ((a, b), w) in self.edges:
            self.adj[a - 1].append(b - 1)
            self.cost[a - 1].append(w)

    def counter(self):
        distance_counting = [-1 for x in range(len(self.adj))]
        visited = [None for x in range(len(self.adj))]
        first_value = Queue(self.start)
        grey_value = PriorityQueue(first_value)
        distance_counting[self.start] = 0
        while grey_value:
            current_value = grey_value.get()
            for b in self.adj[current_value]:
                if distance_counting[b] == -1:
                    grey_value.put(b)
                    distance_counting[b] = distance_counting[current_value] + 1
                if distance_counting[self.stop] != -1:
                    print(distance_counting[self.stop])
                    sys.exit()
        return distance_counting[self.stop]

    def output(self):
        pass

    def solve(self):
        self.read_data()
        self.counter()
        self.output()

if __name__ == "__main__":
    dijkstra = Distance()
    dijkstra.solve()

# if __name__ == '__main__':
#     input1 = (input().split())
#     nr_vertices, nr_edges = int(input1[0]), int(input1[1])
#     vertices_split = [(input().split()) for i in range(nr_edges)]
#     edges = [((int(i[0]), int(i[1])), int(i[2])) for i in vertices_split]
#     input2 = (input().split())
#     start, stop = int(input2[0]), int(input2[1])
#     adj = [[] for _ in range(nr_vertices)]
#     cost = [[] for _ in range(nr_vertices)]
#     start, stop = start - 1, stop - 1
#     for ((a, b), w) in edges:
#         adj[a - 1].append(b - 1)
#         cost[a - 1].append(w)
#     print(distance(adj, cost, start, stop))

first_value