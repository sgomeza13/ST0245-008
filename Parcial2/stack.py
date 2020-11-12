class pila:
    def __init__(self):
        self.items = []    
    def __str__(self):
        return str(self.items)

    def is_empty(self):
        return len(self.items) == 0
    
    def inspeccionar(self):
        assert not self.is_empty()
        return self.items[-1] #[-1] para retornar el ultimo elemento

    def apilar(self, elemento):
        self.items.append(elemento)
    
    def desapilar(self):
        assert not self.is_empty()
        self.items.pop()
    def peek(self):
        if len(self.items) > 0:
            return self.items[len(self.items)-1]
        else:
            return None
    def invertir(self):
        if self.is_empty():
            return self.items
        else:
            inv = pila()
            for i in self.items[::-1]:
                inv.apilar(i)
                self.desapilar()
        return inv
        

mi_pila = pila()
mi_pila.apilar(11)
mi_pila.apilar(22)
mi_pila.apilar(33)
mi_pila.apilar(44)
print(mi_pila)
print(mi_pila.invertir())

