while True:
    try:
        expression = input()
        cont = 0
        for i in range(len(expression)):
            if(expression[i] == '('):
                cont += 1
            elif(expression[i] == ')'):
                cont -= 1
            if(cont<0):
                break
        if(cont != 0):
            print('incorrect')
        else:
            print('correct')
    except EOFError:
        break
