#!/usr/bin/python3

import sys, threading
from math import inf

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 25)  # new thread will get stack of such size


class Tree:
    def __init__(self, tree_data):
        self.key = [0] * len(tree_data)
        self.left = [0] * len(tree_data)
        self.right = [0] * len(tree_data)
        self.subtree_max = [-inf] * len(tree_data)
        self.subtree_min = [-inf] * len(tree_data)

        for i, a in enumerate(tree_data):
            self.key[i], self.left[i], self.right[i] = a[0], a[1], a[2]

    def calc_subtree_max(self, v=0):
        if v == -1:
            return -inf


        left_max = self.calc_subtree_max(self.left[v])
        right_max = self.calc_subtree_max(self.right[v])
        self.subtree_max[v] = max(left_max, right_max, self.key[v])
        return self.subtree_max[v]

    def calc_subtree_min(self, v=0):
        if v == -1:
            return inf

        left_min = self.calc_subtree_min(self.left[v])
        right_min = self.calc_subtree_min(self.right[v])
        self.subtree_min[v] = min(left_min, right_min, self.key[v])
        return self.subtree_min[v]

    def is_bst(self, v=0):
        if v == -1:
            return True
        left = self.is_bst(self.left[v])
        right = self.is_bst(self.right[v])
        if not (left and right):
            return False
        if self.left[v] != -1 and self.key[v] <= self.subtree_max[self.left[v]]:
            return False
        if self.right[v] != -1 and self.key[v] > self.subtree_min[self.right[v]]:
            return False
        return True


def is_bst(tree):
    t = Tree(tree)
    t.calc_subtree_min()
    t.calc_subtree_max()
    return t.is_bst()


def main():
    nodes = int(sys.stdin.readline().strip())
    if nodes == 0:
        print("CORRECT")
        return
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if is_bst(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


if __name__ == '__main__':
    threading.Thread(target=main).start()