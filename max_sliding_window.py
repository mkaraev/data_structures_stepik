# python3

from collections import namedtuple

Pair = namedtuple("Pair", ["first", "second"])


class StackWithMax:
    def __init__(self):
        self.__stack = []

    def is_empty(self):
        return len(self.__stack) == 0

    def push(self, a):
        if len(self.__stack) == 0:
            self.__stack.append(Pair(a, a))
        else:
            max_ = max(self.__stack[-1].second, a)
            self.__stack.append(Pair(a, max_))

    def pop(self):
        assert (len(self.__stack))
        self.__stack.pop()

    def top(self):
        assert (len(self.__stack))
        return self.__stack[-1].first

    def max(self):
        assert (len(self.__stack))
        return self.__stack[-1].second


class Queue:
    def __init__(self, size):
        self.in_stack = StackWithMax()
        self.out_stack = StackWithMax()
        self.size = size

    def push(self, a):
        self.in_stack.push(a)

    def pop(self):
        if self.out_stack.is_empty():
            while not self.in_stack.is_empty():
                a = self.in_stack.top()
                self.in_stack.pop()
                self.out_stack.push(a)

        self.out_stack.pop()

    def max(self):
        max_1, max_2 = 0, 0
        if not self.in_stack.is_empty():
            max_1 = self.in_stack.max()
        if not self.out_stack.is_empty():
            max_2 = self.out_stack.max()
        return max(max_1, max_2)


def max_sliding_window_naive(sequence, m):
    maximums = []
    queue = Queue(m)
    for x in sequence[:m]:
        queue.push(x)

    maximums.append(queue.max())
    for x in sequence[m:]:
        queue.pop()
        queue.push(x)
        maximums.append(queue.max())

    return maximums


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))
