class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class HashTable:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.table = {}
        self.bucket_count = bucket_count

    def _hash(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def find(self, s):
        hash_value = self._hash(s)
        if not hash_value in self.table:
            return False

        return s in self.table[hash_value]

    def add(self, s):
        if self.find(s):
            return

        hash_value = self._hash(s)
        if hash_value not in self.table:
            self.table[hash_value] = []

        self.table[hash_value].append(s)

    def delete(self, s):
        if not self.find(s):
            return

        hash_value = self._hash(s)
        self.table[hash_value].remove(s)

    def check(self, i):
        if i in self.table:
            return list(reversed(self.table[i]))
        return []


class QueryProcessor:

    def __init__(self, bucket_count):
        self.hash_table = HashTable(bucket_count)

    @staticmethod
    def write_search_result(was_found):
        print('yes' if was_found else 'no')

    @staticmethod
    def write_chain(chain):
        print(' '.join(chain))

    @staticmethod
    def read_query():
        return Query(input().split())

    def process_query(self, query):
        if query.type == "find":
            # use reverse order, because we append strings to the end
            self.write_search_result(self.hash_table.find(query.s))

        if query.type == 'add':
            self.hash_table.add(query.s)
        if query.type == 'del':
            self.hash_table.delete(query.s)
        if query.type == 'check':
            self.write_chain(self.hash_table.check(query.ind))

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
