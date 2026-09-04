'''
Implement the Least Recently Used (LRU) cache class LRUCache. The class should support the following operations
LRUCache(int capacity) Initialize the LRU cache of size capacity.
int get(int key) Return the value corresponding to the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.
A key is considered used if a get or a put operation is called on it.
Ensure that get and put each run in O(1) average time complexity.
'''


class Node:
    def __init__(self, key: int = 0, val: int = 0):
        self.key, self.val = key, val
        self.prev, self.next = None, None


class LRUCache:
    '''
        we need to preserve the order of insertion and update the order when a key is accessed.
        need hash map to access in O(1), doubly linked list to modify in O(1)
    '''

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        # for simplicity, wrap the linked list with dummy left and right to unify the operation interface
        self.left, self.right = Node(0), Node(-1)
        self.left.next, self.right.prev = self.right, self.left

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv

        # insert to right
        prv = self.right.prev
        prv.next, node.prev = node, prv
        node.next, self.right.prev = self.right, node

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.get(key)
            return
        
        if len(self.cache) >= self.cap:
            node = self.left.next
            prv, nxt = self.left, node.next
            del self.cache[node.key]
            prv.next = nxt
            nxt.prev = prv

        # add the last and cache dict
        newNode = Node(key, value)
        self.cache[key] = newNode

        prv = self.right.prev
        prv.next, newNode.prev = newNode, prv
        newNode.next, self.right.prev = self.right, newNode
