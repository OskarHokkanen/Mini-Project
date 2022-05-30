from dataclasses import dataclass
from typing import List


@dataclass
class HashSet:
    buckets: List[List] = None
    size: int = 0

    def init(self):
        self.size = 0
        self.buckets = [[] for i in range(8)]

    # Computes hash value for a word (a string)
    def get_hash(self, word):
        n = len(self.buckets)
        sum = 0
        for c in word:
            sum += ord(c)
        hashing_value = sum % n
        return hashing_value

    # Doubles size of bucket list
    def rehash(self):
        old = []
        self.size = 0
        for bucket in self.buckets:
            if bucket is not None:
                for items in bucket:
                    old.append(items)
        self.buckets = [[] for i in range(len(self.buckets) * 2)]
        for w in old:
            self.add(w)

    # Adds a word to set if not already added
    def add(self, word):
        val = self.get_hash(word)
        if word not in self.buckets[val]:
            self.buckets[val].append(word)
            self.size += 1
        if self.size > len(self.buckets):
            self.rehash()

    # Returns a string representation of the set content
    def to_string(self):
        s = "{ "
        for c in self.buckets:
            for i in c:
                s += i + " "
        s += " }"
        return s

    # Returns current number of elements in set
    def get_size(self):
        return self.size

    # Returns True if word in set, otherwise False
    def contains(self, word):
        hashing_val = self.get_hash(word)
        if word in self.buckets[hashing_val]:
            return True
        else:
            return False

    # Returns current size of bucket list
    def bucket_list_size(self):
        return len(self.buckets)

    # Removes word from set if there, does nothing
    # if word not in set
    def remove(self, word):
        val = self.get_hash(word)
        if word in self.buckets[val]:
            self.buckets[val].remove(word)
            self.size -= 1

    # Returns the size of the bucket with most elements
    def max_bucket_size(self):
        max = 0
        for bucket in self.buckets:
            if max < len(bucket):
                max = len(bucket)
        return max
