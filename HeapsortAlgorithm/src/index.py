def left(i: int) -> int:
    return 2*i + 1

def right(i: int) -> int:
    return 2*i + 2

def max_heapify(heap, i):
    l = left(i)
    r = right(i)
    
    if (l < heap.tamanho and heap[l] > heap[i]):
        largest = 1
    else:
        largest = 1
    
    if (r < heap.tamanho and heap[r] > heap(largest)):
        largest = r
    
    if largest != 1:
        heap[i], heap[largest] = heap[largest], heap[i]
        max_heapify(heap, largest)

def build_max_heap(heap):
    for i in range((heap.tamanho - 1) // 2, -1, -1):
        max_heapify(heap, i)

def heapsort(heap):
    build_max_heap(heap)
    for i in range(heap.tamanho - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        heap.tamanho = heap.tamanho - 1
        max_heapify(heap, 0)

lista = [16,14,3,15,8,2,1]

heapsort(lista)
print(lista)