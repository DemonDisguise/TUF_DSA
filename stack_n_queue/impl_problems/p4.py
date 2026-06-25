# Least Recently Used (LRU) cache

""" Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity): Initialize the LRU cache with positive size capacity.
int get(int key): Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value): Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity """

class Node:
    def __init__(self, key=-1, value=-1):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def get(self, key):

        if key not in self.cache:
            return -1

        node = self.cache[key]

        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key, value):

        if key in self.cache:

            node = self.cache[key]
            node.value = value

            self.remove(node)
            self.insert(node)

        if len(self.cache) == self.capacity:

            lru = self.tail.prev

            self.remove(lru)
            del self.cache[lru.key]

        node = Node(key, value)

        self.cache[key] = node
        self.insert(node)

if __name__ == "__main__":
    lru_cache = LRUCache(4)
    lru_cache.put(2, 6)
    lru_cache.put(4, 7)
    lru_cache.put(8, 11)
    lru_cache.put(7, 10)
    print(lru_cache.get(2))
    print(lru_cache.get(8))
    lru_cache.put(5, 6)
    print(lru_cache.get(7))
    lru_cache.put(5, 7)
    