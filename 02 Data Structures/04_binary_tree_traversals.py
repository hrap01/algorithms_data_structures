# python3

import sys, threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self):
        current_id = 0
        stack = []
        result = []

        while True:
            if current_id != -1:
                stack.append(current_id)
                current_id = self.left[current_id]
            elif stack:
                current_id = stack.pop()
                result.append(self.key[current_id])
                current_id = self.right[current_id]
            else:
                return (" ".join(str(x) for x in result))

    def preOrder(self):
        current_id = 0
        stack = []
        result = []

        while True:
            if current_id != -1:
                stack.append(current_id)
                result.append(self.key[current_id])
                current_id = self.left[current_id]
            elif stack:
                current_id = stack.pop()
                current_id = self.right[current_id]
            else:
                return (" ".join(str(x) for x in result))

    def postOrder(self):
        stack1 = [0]
        stack2 = []
        result = []

        while stack1:
            current_id = stack1.pop()
            stack2.append(self.key[current_id])

            left_id = self.left[current_id]
            right_id = self.right[current_id]
            if left_id != -1:
                stack1.append(left_id)
            if right_id != -1:
                stack1.append(right_id)

        while stack2:
            result.append(stack2.pop())

        return (" ".join(str(x) for x in result))


def main():
    tree = TreeOrders()
    tree.read()
    print(tree.inOrder())
    print(tree.preOrder())
    print(tree.postOrder())


threading.Thread(target=main).start()
