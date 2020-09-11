while True:
    try:
        numOfRows = int(input())

        if numOfRows == 0 :
            break

        initial = []
        for i in range(1,numOfRows+1):
            initial.append(i)

        result = []
        while len(initial) > 1:
            result.append(initial.pop(0))
            initial.insert(len(initial)-1,initial.pop(0))

        print("Discarded cards: " + str(result).replace("[","").replace("]",""))
        print("Remaining card: " + str(initial[0]))
    
    except EOFError:
        break