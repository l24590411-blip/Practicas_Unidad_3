class NodoKV:
    def __init__(self, k, v):
        self.k, self.v = k, v
        self.prev = None
        self.next = None

class LRU:
    def __init__(self, cap):
        self.cap = cap
        self.map = {}
        self.head = NodoKV(0, 0)  # centinela head
        self.tail = NodoKV(0, 0)  # centinela tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_front(self, n):
        n.prev = self.head
        n.next = self.head.next
        self.head.next.prev = n
        self.head.next = n

    def _remove(self, n):
        n.prev.next = n.next
        n.next.prev = n.prev
        n.prev = n.next = None

    def _move_to_front(self, n):
        self._remove(n)
        self._add_front(n)

    def _evict_lru(self):
        lru = self.tail.prev
        if lru is self.head:
            return
        self._remove(lru)
        del self.map[lru.k]

    def get(self, k):
        if k not in self.map:
            return -1
        n = self.map[k]
        self._move_to_front(n)
        return n.v

    def put(self, k, v):
        if k in self.map:
            n = self.map[k]
            n.v = v
            self._move_to_front(n)
        else:
            n = NodoKV(k, v)
            self.map[k] = n
            self._add_front(n)
            if len(self.map) > self.cap:
                self._evict_lru()
cache = LRU(2)
cache.put(1, 10)    # {1:10}
cache.put(2, 20)    # {1:10, 2:20}
print(cache.get(1)) # 10 → 1 es MRU
cache.put(3, 30)    # expulsa 2
print(cache.get(2)) # -1
cache.put(4, 40)    # expulsa 3
print(cache.get(1)) # 10
print(cache.get(3)) # -1
print(cache.get(4)) # 40