class Node:
    def __init__(self, val, key=None):
        self.val = val
        self.key = key
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.left, self.right = Node(0), Node(0)
        self.left.next, self.right.prev = self.right, self.left
    
    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    def _insert(self, key, val):
        prev, nxt = self.right.prev, self.right
        node = Node(val, key=key)
        node.prev, node.next = prev, nxt
        prev.next = nxt.prev = node
        self.cache[key] = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._remove(node)
        self._insert(key, node.val)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])

        self._insert(key, value)

        if len(self.cache) > self.capacity:
            to_del = self.left.next
            print('*to remove',to_del.key)
            self._remove(to_del)
            del self.cache[to_del.key]
