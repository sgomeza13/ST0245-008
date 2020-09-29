"""Este algoritmo implementa lo que son los 'sets' o en español 'conjuntos' que basicamente son una coleccion de elementos finita sin ningun orden necesario, muy parecido a lo que es una lista.
Con esta clase se crean una cantidad de funciones muy utiles a la hora de manipular estos conjuntos como conocer su longitud, añadir elementos, entre otras."""
class set:
    #Constructor de la clase set(conjunto), crea una instancia de set vacia
    def __init__(self):
        self._theElements = list()
        #Retorna la longitud del conjunto
        def __len__(self):
            return len(self._theElements)
        #Busca un elemento en el conjunto
        def __contains__(self,element):
            ndx = self._findPosition(element)
            self._theElements.insert(ndx,element)

        #Elimnina un elemento del conjunto
        def remove(self,element):
            assert element in self:
                ndx = self._findPosition(element)
                self._theElements.pop(ndx)

        #Determina si si el conjunto es subconjunto de del conjunto B
        def isSubsetOf(self,setB):
            for elementt in self:
                if element not in setB:
                    return False
                return True

        #Retorna un iterador para recorrer la lista de items
        def __iter__(self):
            return _SetIterator(self._theElements)

        #Encuentra la posicion del elemento entre la lista ordenada
        def _findPosition(self,element):
            low = 0
            high = len(theList) - 1
            while low <= high:
                mid = (high + low) / 2
                if theList[mid] == target:
                    return mid
                elif target < theList[mid]:
                    high = mid-1
                else:
                    low = mid+1
                return low
"""Su complejidad es de o(n)"""