import re

def checkIP(line):
    rg = re.compile('^(?:[0-9]{1,3}\.){3}[0-9]{1,3}')

    return rg.search(line) != None


if __name__ == "__main__":
    while(True):
        line = input('line: ')

        if(line == 'q'):
            break    
        
        print(checkIP(line))
        print()