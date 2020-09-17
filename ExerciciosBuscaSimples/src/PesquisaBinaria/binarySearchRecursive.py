def binaryResearch(list, id):
    if(len(list) > 1):
        mid = len(list) // 2
        if (list[mid].identifier == id):
            return list[mid]
        elif (list[mid].identifier < id): # 6 < 7
           return binaryResearch(list[mid:], id)
        else:
            return binaryResearch(list[:mid], id)
    else: 
        return None
