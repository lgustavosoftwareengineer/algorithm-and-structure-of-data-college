def researchAgentsRecursive(list, identifier):
    if(len(list) > 1):
        mid = len(list) // 2
        if (list[mid].identifier == identifier):
            return list[mid]
        elif (list[mid].identifier < identifier): # 6 < 7
           return researchAgentsRecursive(list[mid:], identifier)
        else:
            return researchAgentsRecursive(list[:mid], identifier)
    else: 
        return None
