class Node:

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = self.next = None
    
    def __str__(self):
        return f'{self.key}: {self.value}'
    
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(), Node()
        self.left.next, self.right.prev = self.right, self.left

    def _add(self, node):
        self.cache[node.key] = node
        node.prev, node.next = self.right.prev, self.right
        self.right.prev.next = self.right.prev = node
    
    def _remove(self, node):
        del self.cache[node.key]
        node.prev.next, node.next.prev = node.next, node.prev

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        
        node = self.cache[key]
        self._remove(node)
        self._add(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
        else:
            node = Node(key=key, value=value)
        
        self._add(node)

        if len(self.cache.keys()) > self.capacity:
            self._remove(self.left.next)