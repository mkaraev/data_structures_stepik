# python3

import sys
import threading

from typing import List


class Tree:
    __slots__ = ["root", "n", "graph"]

    def __init__(self):
        self.root = None
        self.n = 0
        self.graph = {}

    def construct_tree(self, n: int, parents: List[int]):
        self.n = n
        for i, p in enumerate(parents):
            if p == -1:
                self.root = i
            else:
                if p not in self.graph:
                    self.graph[p] = []
                self.graph[p].append(i)
        return self

    def compute_height(self, node):
        if node not in self.graph:
            return 1
        max_sub_height = 0
        for v in self.graph[node]:
            max_sub_height = max(max_sub_height, self.compute_height(v))
        return max_sub_height + 1


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    tree = Tree().construct_tree(n, parents)
    print(tree.compute_height(node=tree.root))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
if __name__ == '__main__':
    sys.setrecursionlimit(10 ** 7)  # max depth of recursion
    threading.stack_size(2 ** 27)  # new thread will get stack of such size
    threading.Thread(target=main).start()
