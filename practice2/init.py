import readline
import re

def isNumber(line):
    p = re.compile('[0-9]+')

    t = False
    if(p.match(line)):
        t = True

    return t

def allWords(line):
    reg = '[a-z]+'

    groups = re.findall(reg, line)

    for group in groups:
        print(group)


if __name__ == "__main__":

    while(True):
        line = input('line: ')

        if(line == 'q'):
            break    
        
        # print(isNumber(line))
        allWords(line)
        
        print()
