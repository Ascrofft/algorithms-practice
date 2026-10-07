class MyDataStructure:
    def __init__(self, default_data=[], capacity=1024):  # noqa: B006
        """ usage:
                structure = MyDataStructure()
                structure.add(42)
                    OR
                structure = MyDataStructure([42])
        """
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]
        for value in default_data:
            self.add(value)

    def _hash(self, value):
        return hash(value) % self.capacity

    def add(self, value):
        index = self._hash(value)
        bucket = self.buckets[index]

        if value not in bucket:
            bucket.append(value)
            self.size += 1

    def remove(self, value):
        index = self._hash(value)
        bucket = self.buckets[index]

        if value in bucket:
            bucket.remove(value)
            self.size -= 1
        else:
            raise KeyError(value)

    def __contains__(self, value):
        """ usage: value in myDataStructure """
        index = self._hash(value)
        return value in self.buckets[index]

    def __len__(self):
        """ usage: len(myDataStructure) """
        return self.size

    def __iter__(self):
        """ usage: for item in myDataStructure """
        for bucket in self.buckets:
            yield from bucket

    def to_list(self):
        return list(self)

    def union(self, other):
        result = MyDataStructure()

        for value in self:
            result.add(value)

        for value in other:
            result.add(value)

        return result

    def intersection(self, other):
        result = MyDataStructure()

        for value in self:
            if value in other:
                result.add(value)

        return result

    def difference(self, other):
        result = MyDataStructure()

        for value in self:
            if value not in other:
                result.add(value)

        return result

    def __str__(self):
        values = list(self)
        return "{" + ", ".join(str(v) for v in values) + "}"
