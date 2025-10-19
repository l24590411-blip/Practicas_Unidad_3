class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.prev = None
        self.next = None

class ListaDoble:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, x):
        n = Nodo(x)
        n.next = self.head
        if self.head:
            self.head.prev = n
        else:
            self.tail = n
        self.head = n

    def push_back(self, x):
        n = Nodo(x)
        n.prev = self.tail
        if self.tail:
            self.tail.next = n
        else:
            self.head = n
        self.tail = n

    def __len__(self):
        cur, c = self.head, 0
        while cur:
            c += 1
            cur = cur.next
        return c

    def k_from_end(self, k):
        cur = self.tail
        i = 1
        while cur and i < k:
            cur = cur.prev
            i += 1
        return cur.dato if cur else None

    def forward(self):
        cur, out = self.head, []
        while cur:
            out.append(cur.dato)
            cur = cur.next
        return out

    def backward(self):
        cur, out = self.tail, []
        while cur:
            out.append(cur.dato)
            cur = cur.prev
        return out

# 🔍 Prueba rápida
ld = ListaDoble()
for x in [5, 10, 15, 20, 25, 30]:
    ld.push_back(x)

print(len(ld))             # 6
print(ld.k_from_end(1))    # 30
print(ld.k_from_end(3))    # 20
print(ld.k_from_end(6))    # 5
print(ld.k_from_end(7))    # None (fuera de rango)