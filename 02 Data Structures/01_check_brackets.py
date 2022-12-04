from collections import namedtuple
from collections import deque

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    if (left + right) in ["()", "[]", "{}"]:
        return True
    else:
        return False


def find_mismatch(text):
    opening_brackets_stack = deque()
    for i, next in enumerate(text):
        save_info = Bracket(char=i+1, position=next)

        if next in "([{":
            opening_brackets_stack.append([i+1, next])
            pass

        if next in ")]}":
            if len(opening_brackets_stack) == 0:
                return save_info[0]
            left = opening_brackets_stack.pop()
            if are_matching(left[1], next):
                pass
            else:
                return save_info[0]

    if opening_brackets_stack:
        output = opening_brackets_stack.pop()
        return output[0]
    else:
        return 'Success'


if __name__ == "__main__":
    text = input()
    print(find_mismatch(text))

