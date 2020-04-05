
def problemChallenge(line):

    isP = isU = isI = False
    P = U = I = 0
    
    for i in range(len(line)):
        if(line[i] == '='):
            ch = line[i-1]
            i += 1

            val = ''
            while(line[i].isdigit()):
                val += line[i]
                i += 1

            if(line[i] == '.'):
                val += '.'
                i += 1

            while(line[i].isdigit()):
                val += line[i]
                i += 1

            val = float(val)
            if(line[i] == 'm'):
                val /= 1000
            elif(line[i] == 'k'):
                val *= 1000
            elif(line[i] == 'M'):
                val *= 1000000


            if(ch == 'P'):
                P = val
                isP = True
            elif(ch == 'U'):
                U = val
                isU = True
            elif(ch == 'I'):
                I = val
                isI = True

            print('{} = {}'.format(ch, val))
        else:
            i += 1

    if(not isP):
        print('P = {0:.3f}W'.format(U*I))
    elif(not isU):
        print('U = {0:.3f}V'.format(P/I))
    elif(not isI):
        print('I = {0:.3f}A'.format(P/U))

    print()
    
if __name__ == "__main__":

    while(True):
        line = input('line: ')

        if(line == 'q'):
            break    
        
        problemChallenge(line)