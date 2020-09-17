def researchAgentsIterative(list, id):
    newList = list
    for i in list:
        if (len(newList) >= 1):
            mid = len(newList) // 2
            if (newList[mid].identifier == id):
                return newList[mid]
                break
            elif newList[mid].identifier > id:
                newList = newList[:mid]
                
            elif newList[mid].identifier < id:
                newList = newList[mid:]
        else:
            return None
            
