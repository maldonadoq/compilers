import re

def repeated(line):
    rx = re.compile(r'(.)\1{1,}')

    groups = re.findall(rx, line)

    for group in groups:
        print(group)


if __name__ == '__main__':
    while(True):
        line = input('line: ')

        if(line == 'q'):
            break    
        
        repeated(line)
        print()
    