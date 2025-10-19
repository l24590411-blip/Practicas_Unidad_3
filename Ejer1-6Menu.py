#paola de Jesus Morales Andrade
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

    def find(self, v):
        cur = self.head
        while cur:
            if cur.dato == v:
                return cur
            cur = cur.next
        return None

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

    def insert_after(self, objetivo, x):
        nodo = self.find(objetivo)
        if not nodo:
            return
        n = Nodo(x)
        n.prev = nodo
        n.next = nodo.next
        if nodo.next:
            nodo.next.prev = n
        else:
            self.tail = n
        nodo.next = n

    def remove_value(self, v):
        nodo = self.find(v)
        self.remove_node(nodo)

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

    def backward(self):
        cur, out = self.tail, []
        while cur:
            out.append(cur.dato)
            cur = cur.prev
        return out

class NodoKV:
    def __init__(self, k, v):
        self.k, self.v = k, v
        self.prev = None
        self.next = None

class LRU:
    def __init__(self, cap):
        self.cap = cap
        self.map = {}
        self.head = NodoKV(0, 0)
        self.tail = NodoKV(0, 0)
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

def menu():
    ld = ListaDoble()
    cache = LRU(2)

    while True:
        print("\n📘 MENÚ DE EJERCICIOS")
        print("1. Insertar en lista doble")
        print("2. Insertar después de un valor")
        print("3. Eliminar por valor")
        print("4. Contar nodos y obtener k-ésimo desde el final")
        print("5. Remover duplicados")
        print("6. Usar LRU Cache")
        print("0. Salir")

        op = input("Opción: ")

        if op == "1":
            x = int(input("Valor a insertar (push_back): "))
            ld.push_back(x)
            print("Lista:", ld.forward())

        elif op == "2":
            objetivo = int(input("Insertar después de: "))
            x = int(input("Valor a insertar: "))
            ld.insert_after(objetivo, x)
            print("Lista:", ld.forward())

        elif op == "3":
            v = int(input("Valor a eliminar: "))
            ld.remove_value(v)
            print("Lista:", ld.forward())

        elif op == "4":
            print("Longitud:", len(ld))
            k = int(input("k desde el final: "))
            print("Resultado:", ld.k_from_end(k))

        elif op == "5":
            ld.remove_dups()
            print("Lista sin duplicados:", ld.forward())

        elif op == "6":
            print("LRU Cache (capacidad 2)")
            print("1. put(key, value)")
            print("2. get(key)")
            sub = input("Opción: ")
            if sub == "1":
                k = int(input("Key: "))
                v = int(input("Value: "))
                cache.put(k, v)
                print("Insertado.")
            elif sub == "2":
                k = int(input("Key: "))
                print("Valor:", cache.get(k))

        elif op == "0":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()