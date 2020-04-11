import re

def checkIdentifier(line):
    rg = re.compile('^[a-z|A-Z]+[0-9]*')

    return rg.search(line) != None


if __name__ == "__main__":
    while(True):
        line = input('line: ')

        if(line == 'q'):
            break    
        
        print(checkIdentifier(line))
        print()