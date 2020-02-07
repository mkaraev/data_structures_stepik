from collections import namedtuple

Pair = namedtuple("Pair", ["x", "y"])


class DSU:
    def __init__(self, n):
        self.ranks = [0] * n
        self.parents = list(range(n))

    def get_parent(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.get_parent(self.parents[x])
        return self.parents[x]

    def merge(self, x, y):
        x = self.get_parent(x)
        y = self.get_parent(y)

        if x == y:
            return

        if self.ranks[x] > self.ranks[y]:
            x, y = y, x

        self.parents[x] = y
        if self.ranks[x] == self.ranks[y]:
            self.ranks[y] += 1

    def are_in_one_set(self, x, y):
        x = self.get_parent(x)
        y = self.get_parent(y)
        return x == y


def main():
    n, e, d = map(int, input().split())
    dsu = DSU(n)
    for i in range(e):
        x, y = map(int, input().split())
        x, y = x - 1, y - 1
        dsu.merge(x, y)

    for i in range(d):
        x, y = map(int, input().split())
        x, y = x - 1, y - 1
        if dsu.are_in_one_set(x, y):
            print("0\n")
            return

    print("1")


if __name__ == '__main__':
    main()
