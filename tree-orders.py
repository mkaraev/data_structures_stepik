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

    def in_order(self, v=0):
        if v == -1:
            return []
        result = []
        result += self.in_order(self.left[v])
        result.append(self.key[v])
        result += self.in_order(self.right[v])
        return result

    def pre_order(self, v=0):
        if v == -1:
            return []
        result = []
        result.append(self.key[v])
        result += self.pre_order(self.left[v])
        result += self.pre_order(self.right[v])
        return result

    def post_order(self, v=0):
        if v == -1:
            return []
        result = []
        result += self.post_order(self.left[v])
        result += self.post_order(self.right[v])
        result.append(self.key[v])
        return result


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.in_order()))
    print(" ".join(str(x) for x in tree.pre_order()))
    print(" ".join(str(x) for x in tree.post_order()))


if __name__ == '__main__':
    threading.Thread(target=main).start()
