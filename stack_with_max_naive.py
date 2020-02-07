# python3
import sys

from collections import namedtuple

Pair = namedtuple("Pair", ["first", "second"])


class StackWithMax:
    def __init__(self):
        self.__stack = []

    def push(self, a):
        if len(self.__stack) == 0:
            self.__stack.append(Pair(a, a))
        else:
            max_ = max(self.__stack[-1].second, a)
            self.__stack.append(Pair(a, max_))

    def pop(self):
        assert (len(self.__stack))
        self.__stack.pop()

    def max(self):
        assert (len(self.__stack))
        return self.__stack[-1].second


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.push(int(query[1]))
        elif query[0] == "pop":
            stack.pop()
        elif query[0] == "max":
            print(stack.max())
        else:
            assert 0
