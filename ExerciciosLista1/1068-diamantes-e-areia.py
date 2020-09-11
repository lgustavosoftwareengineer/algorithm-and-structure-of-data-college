numOfTests = input()
for i in range(int(numOfTests)):
    try:
        diggingInput = input()
        diamondAmount = 0
        cont = 0
        for f in diggingInput:
            if(f == '<'):
                cont+=1
            if(f == '>' and cont > 0):
                diamondAmount += 1
                cont -= 1
        print(diamondAmount)

    except EOFError:
        break
