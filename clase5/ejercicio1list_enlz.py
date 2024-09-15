class Node:
    def _init_(self, data):
        self.data = data
        self.next = None
class ListaEnlazada:

    def _init_(self):
        self.cabeza = None

    def es_vacio(self):
        return self.cabeza is None

    def agregar_nodo(self, dato):
        nodo = Node(dato)
        if self.es_vacio():
            self.cabeza = nodo
        else:
                nodo_actual = self.cabeza
                while nodo_actual.next is not None:
                    nodo_actual = nodo_actual.next
                nodo_actual.next = nodo

    def imprimir(self):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            print(nodo_actual.data)
            nodo_actual = nodo_actual.next

    def buscar_elemento(self, dato):
        nodo = Node(dato)
        if self.es_vacio():
            return f"Esta vacía la lista o no existe"

        else:
            c = 0
            nodo_actual = self.cabeza
            if nodo_actual.data == dato:
                    return f"El dato es {nodo_actual} y su posición es {c}"
            else:
                nodo_actual=nodo_actual.next
                c = c + 1        
            while nodo_actual is not None:
                if nodo_actual.data == dato:
                    return f"El dato es {nodo_actual.data} y su posición es {c} "
                nodo_actual=nodo_actual.next
                c = c + 1
            return f"El dato no está en la lista"


lista = ListaEnlazada()
print("Agregamos datos al nodo")
lista.agregar_nodo(5)
lista.agregar_nodo(3)
lista.agregar_nodo(8)

print("Imprimimos los datos")
lista.imprimir()
