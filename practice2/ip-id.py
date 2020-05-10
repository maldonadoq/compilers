import readline
import re

def checkIP(line):
    rg = re.compile('^((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])$')

    return rg.search(line) != None


def checkIdentifier(line):
    rg = re.compile('^[a-z|A-Z]+[0-9]*')

    return rg.search(line) != None


if __name__ == "__main__":
    while(True):
        line = input('line: ')

        if(line == 'q'):
            break    
        
        print(checkIP(line))
        # print(checkIdentifier(line))
        print()