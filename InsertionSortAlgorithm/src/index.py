from typing import List

def insertionSort(list: List[int]) -> List[int]:
    for i in range(1, len(list)):
        key: int = list[i]
        lvi: int = i - 1 # lvi - last value index
        while lvi >= 0 and list[lvi] > key:
            list[lvi + 1] = list[lvi]
            lvi -= 1
        list[lvi + 1] = key 
    return list

list = [4,1,7,2,8,3]
insertionSort(list)
print(list)