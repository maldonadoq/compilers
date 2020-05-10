import readline

def checkBalance(expression):
    stack = []

    for i in range(len(expression)):        

        exp = expression[i]

        if(exp == '(' or exp == '[' or exp == '{'):
            stack.append(exp)
            continue

        if(len(stack) == 0):
            return False

        if(exp == ')'):
            tmp = stack.pop()
            if(tmp != '('):
                return False
        elif(exp == ']'):
            tmp = stack.pop()
            if(tmp != '['):
                return False
        elif(exp == '}'):
            tmp = stack.pop()
            if(tmp != '{'):
                return False

    return len(stack) == 0

if __name__ == "__main__":

    while(True):
        exp = input('expres: ')

        if(exp == 'q'):
            break

        print('Result: {}\n'.format(checkBalance(exp)))