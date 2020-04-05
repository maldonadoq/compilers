
weird = {}

def checkGerund(verb, gerund):
    if(verb in weird):
        return (weird[verb] == gerund)

    sv = (verb[:len(verb) - 2], verb[-2:])

    tgerund = sv[0]

    if(sv[1] == 'ar'):
        tgerund += 'ando'
    elif(sv[1][0] == 'e' or sv[1][0] == 'i'):
        tmp = sv[0][-1:]
        if(tmp == 'a' or tmp == 'e' or tmp == 'i' or tmp == 'o' or tmp == 'u'):
            tgerund += 'yendo'
        else:
            if(sv[1][0]):
                tgerund += 'iendo'
            elif(sv[1][0]):
                tgerund += 'endo'

    return (tgerund == gerund)    

    

if __name__ == '__main__':
    weird['reir'] = 'riendo'

    while(True):
        verb = input('Verb  : ')

        if(verb == 'q'):
            break

        gerund = input('Gerund: ')
        print('Result: {}\n'.format(checkGerund(verb, gerund)))