from collections import defaultdict


class Book:
    def __init__(self, information: str):
        self.command = information[0]
        self.number = information[1]
        if self.command == 'add':
            self.name = information[2]


class BookStep:

    def solution(self):
        self.result = []
        self.book_dict = defaultdict(lambda: "not found")
        for instruction in self.book_split:
            if instruction.command == 'add':
                self.book_dict[instruction.number] = instruction.name
            elif instruction.command == 'find':
                self.result.append(self.book_dict[instruction.number])
            else:
                try:
                    del self.book_dict[instruction.number]
                except KeyError:
                    pass

    def read_data(self):
        n = int(input())
        self.book_split = [Book(input().split()) for i in range(n)]

    def output(self):
        for output in self.result:
            print(output)

    def solve(self):
        self.read_data()
        self.solution()
        self.output()


if __name__ == "__main__":
    new_list = BookStep()
    new_list.solve()
