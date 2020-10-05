
from typing import List


def quick_sort(list: List[int]) -> list:
    length = len(list)
    if length <= 1:
        return list
    else:
        pivot: int = list.pop()

    itens_greater: List[int] = []
    itens_lower: List[int] = []

    for item in list:
        if item > pivot:
            itens_greater.append(item)
        else:
            itens_lower.append(item)

    return quick_sort(itens_lower) + [pivot] + quick_sort(itens_greater) 

list = [1,4,2,5,8,3,5]
print(quick_sort(list))