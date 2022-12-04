# Function to find majority element
from collections import Counter


def majority(arr):
    freqDict = Counter(arr)

    size = len(arr)
    for (key, val) in freqDict.items():
        if (val > (size / 2)):
            return 1
    return 0

if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority(input_elements))