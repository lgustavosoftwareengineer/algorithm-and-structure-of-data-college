def sequencialSearch(list, id):
    for i in list:
        if i.identifier == id:
            return i
    return None

