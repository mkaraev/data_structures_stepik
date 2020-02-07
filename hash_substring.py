# python3


class HashEncoder:
    _prime = 1000000007
    _multiplier = 263

    def __init__(self, s):
        self.n = len(s)
        self.hash = [0] * (self.n + 1)
        self.deg = [0] * (self.n + 1)
        self.s = s

        self.deg[0] = 1
        for i in range(self.n):
            self.hash[i + 1] = (self.hash[i] * self._multiplier + ord(s[i])) % self._prime
            self.deg[i + 1] = (self.deg[i] * self._multiplier) % self._prime

    def get_hash(self, l, r):
        x = (self.hash[l] * self.deg[r - l + 1]) % self._prime
        return (self.hash[r + 1] - x + self._prime) % self._prime


def read_input():
    return input().rstrip(), input().rstrip()


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    encoder = HashEncoder(text)
    hash_ = HashEncoder(pattern).hash[-1]
    res = []
    for i in range(len(text) - len(pattern) + 1):
        s_hash = encoder.get_hash(i, i + len(pattern) - 1)
        if s_hash == hash_:
            res.append(i)
    return res


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
