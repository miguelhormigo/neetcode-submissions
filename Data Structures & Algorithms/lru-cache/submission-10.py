class ListNode:
    def __init__(self, key=None, val=0):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.left, self.right = ListNode(), ListNode()
        self.left.next, self.right.prev = self.right, self.left
        self.nodes = {}
        self.cap = capacity

    def _remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next, nxt.prev = nxt, prev
        del self.nodes[node.key]
    
    def _insert(self, node):
        prev = self.right.prev
        node.prev, node.next = prev, self.right
        prev.next = self.right.prev = node
        self.nodes[node.key] = node

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        
        node = self.nodes[key]
        self._remove(node)
        self._insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            node = self.nodes[key]
            self._remove(node)
            node.val = value
        else:
            node = ListNode(key=key,val=value)
        
        self._insert(node)

        if len(self.nodes) > self.cap:
            self._remove(self.left.next)