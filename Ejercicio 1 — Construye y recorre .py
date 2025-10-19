#Paola de Jesus Morales Andrade
#Estructura de datos Gpo C
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

# Ejemplo de uso
ld = ListaDoble()
ld.push_back(10)
ld.push_back(20)
ld.push_back(30)
ld.push_front(5)

print(ld.forward())   # [5, 10, 20, 30]
print(ld.backward())  # [30, 20, 10, 5]