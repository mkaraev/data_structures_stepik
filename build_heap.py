# python3


def parent(i):
    return i // 2


def left_child(i):
    return 2 * i


def right_child(i):
    return 2 * i + 1


def sift_up(data, i):
    while i > 1 and data[parent(i)] > data[i]:
        data[parent(i)], data[i] = data[i], data[parent(i)]
        i = parent(i)


def sift_down(data, i, swaps):
    min_index = i
    l, r = left_child(i), right_child(i)
    if l < len(data) and data[l] < data[min_index]:
        min_index = l

    if r < len(data) and data[r] < data[min_index]:
        min_index = r

    if i != min_index:
        data[i], data[min_index] = data[min_index], data[i]
        swaps.append((i - 1, min_index - 1))
        sift_down(data, min_index, swaps)


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    data_ = [0] * (len(data) + 1)
    data_[1:] = data
    n = len(data)
    swaps = []
    for i in reversed(range(n // 2 + 1)):
        if i == 0:
            break
        sift_down(data_, i, swaps)

    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
