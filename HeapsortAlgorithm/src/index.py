from typing import List

def heapify(list: List[int], lenList: int, parentNodeIndex: int):
    largest = parentNodeIndex
    left = 2*parentNodeIndex + 1
    right = 2*parentNodeIndex + 2

    if (left<lenList and list[left] > list[largest]):
        largest = left

    if (right<lenList and list[right] > list[largest]):
        largest = right

    if largest != parentNodeIndex:
        list[largest], list[parentNodeIndex] = list[parentNodeIndex], list[largest]
        heapify(list, lenList, largest)

def heap_sort(list: List[int]) -> List[int]:
    lenList = len(list)

    for i in range(lenList, -1, -1):
        heapify(list, lenList, i)

    for i in range(lenList-1, 0, -1):
        list[i], list[0] = list[0], list[i]
        heapify(list, i, 0)
    
    return list


print(heap_sort([10, 7, 8, 11, 1, 2, 3, 4]))


