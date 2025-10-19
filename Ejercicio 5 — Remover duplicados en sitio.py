class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.prev = None
        self.next = None

class ListaDoble:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_back(self, x):
        n = Nodo(x)
        n.prev = self.tail
        if self.tail:
            self.tail.next = n
        else:
            self.head = n
        self.tail = n

    def remove_node(self, nodo):
        if not nodo:
            return
        if nodo.prev:
            nodo.prev.next = nodo.next
        else:
            self.head = nodo.next
        if nodo.next:
            nodo.next.prev = nodo.prev
        else:
            self.tail = nodo.prev
        nodo.prev = nodo.next = None

    def remove_dups(self):
        vistos = set()
        cur = self.head
        while cur:
            if cur.dato in vistos:
                borrar = cur
                cur = cur.next
                self.remove_node(borrar)
            else:
                vistos.add(cur.dato)
                cur = cur.next

    def forward(self):
        cur, out = self.head, []
        while cur:
            out.append(cur.dato)
            cur = cur.next
        return out

# 🔍 Prueba rápida
ld = ListaDoble()
for x in [10, 20, 10, 30, 20, 40, 30]:
    ld.push_back(x)

print("Antes:", ld.forward())  # [10, 20, 10, 30, 20, 40, 30]
ld.remove_dups()
print("Después:", ld.forward())  # [10, 20, 30, 40]