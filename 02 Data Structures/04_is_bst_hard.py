import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    if self.n == 0:
      print("CORRECT")
      sys.exit("CORRECT")
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def in_order(self):
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
        return self.smaller_than(result)

  def smaller_than(self, result: list):
      for i in range(0, len(self.key)):
          if (self.key[i] == self.key[self.left[i]]) and (self.left[i] != -1):
              return "INCORRECT"
      return self.is_binary_search_tree(result)

  def is_binary_search_tree(self, tree: list):
    flag = 0
    for i in range(0, len(tree)-1):
      if tree[i] <= tree[i+1]:
        continue
      else:
        flag += 1

    if flag == 0:
      return "CORRECT"
    else:
      return "INCORRECT"


def main():
  tree = TreeOrders()
  tree.read()
  print(tree.in_order())


threading.Thread(target=main).start()
