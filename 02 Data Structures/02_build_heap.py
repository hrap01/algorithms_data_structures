class HeapBuilder:
    def __init__(self):
        self._swaps = []
        self.data = []

    def read_data(self):
        n = int(input())
        self.data = [-1]
        self.data += [int(s) for s in input().split()]
        assert n == len(self.data) - 1

    def write_response(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def sift_down(self, i):
        min = i
        left = 2*i
        right = 2*i + 1

        if left <= len(self.data) - 1 and self.data[left] < self.data[min] and self.data[left] < self.data[right]:
            self._swaps.append((i - 1, left - 1))
            self.data[left], self.data[min] = self.data[min], self.data[left]
            self.sift_down(left)
        if right <= len(self.data) - 1 and self.data[right] < self.data[min] and self.data[right] < self.data[left]:
            self._swaps.append((i - 1, right - 1))
            self.data[right], self.data[min] = self.data[min], self.data[right]
            self.sift_down(right)


    def generate_swaps(self):
        for i in range((len(self.data) - 1) // 2, 0, -1):
            self.sift_down(i)

    def solve(self):
        self.read_data()
        self.generate_swaps()
        self.write_response()


if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.solve()