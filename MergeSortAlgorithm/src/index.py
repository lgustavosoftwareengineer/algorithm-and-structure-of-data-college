from typing import List


def mergeSort(list: List[int]) -> List[int]:
     
    if len(list)>1: 
        m = len(list)//2
        left = list[:m] 
        right = list[m:] 
        left = mergeSort(left) 
        right = mergeSort(right)
  
        list = [] 
  
        while len(left)>0 and len(right)>0: 
            if left[0]<right[0]: 
                list.append(left[0]) 
                left.pop(0) 
            else: 
                list.append(right[0]) 
                right.pop(0) 
  
        for i in left: 
            list.append(i) 
        for i in right: 
            list.append(i) 
                  
    return list

list = [4, 1, 7, 2, 8, 3]

newList = mergeSort(list)

print(newList)