""" El Algortimo radix sort está basado en counting sort. Se coge el ultimo digito de de cada elemento y son almecenados en una "cubeta" ya sea de forma creciente o decreciente
(basado en el ultimo digito) esto se hara tantas veces como el numero de digitos del elemento mayor, a este elemento se le conoce como k. Por lo que su complejidad es de o(n+k)
Ejemplo de radixsort sacado de: https://www.programiz.com/dsa/radix-sort
"""
def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    # Calculate cummulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


# Main function to implement radix sort
def radixSort(array):
    # Get maximum element
    max_element = max(array)

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10


data = [121, 432, 564, 23, 1, 45, 788]
radixSort(data)
print(data)

"""El algoritmo Bin sort o Bucket sort es un algoritmo que ordena los elemento de una lista dividiendo los elementos en multiples "cubetas" o "basureros" cada cubeta ordenan individualmente usando cualquiera de los 
algoritmos de ordenamiento, o incluso llamando este mismo algoritmo de forma recursiva. Finalmente se vuelven a unir todoas las cubetas en una sola lista y esta lista final ya estara ordenada  
Informacion y ejemplo sacados de: https://www.programiz.com/dsa/bucket-sort
"""

def bucketSort(array):
    bucket = []

    # Create empty buckets
    for i in range(len(array)):
        bucket.append([])

    # Insert elements into their respective buckets
    for j in array:
        index_b = int(10 * j)
        bucket[index_b].append(j)

    # Sort the elements of each bucket
    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])

    # Get the sorted elements
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array


array = [.42, .32, .33, .52, .37, .47, .51]
print("Sorted Array in descending order is")
print(bucketSort(array))