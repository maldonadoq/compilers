# Percy Maldonado Quispe


# Token Class [word, idx, type]
class Token:
    # Constructor
    def __init__(self, _word, _idx, _type):
        self.word = _word
        self.idx = _idx
        self.type = _type

    # Override Print Function
    def __str__(self):
        return 'Token[{}]: pos = {}, type = {}'.format(self.word, self.idx, self.type)


# Lexical Analyzer Class
class LexicalAnalizer:
    def __init__(self):
        pass

    # Check character by character if it is digit, and add in a  temporary word,
    # he loop ends if no character of type digit is found.
    # The token and the new idx are returned.
    def isNumber(self, line, idx):

        tword = line[idx]
        tidx = idx + 1

        while(tidx < len(line) and line[tidx].isdigit()):
            tword += line[tidx]
            tidx += 1

        token = Token(tword, idx, 'I')

        return token, tidx

    # Check character by character if it is alalnum, and add in a  temporary word,
    # he loop ends if no character of type isalnum is found.
    # The token and the new idx are returned.
    def isVariable(self, line, idx):

        tword = line[idx]
        tidx = idx + 1

        while(tidx < len(line) and line[tidx].isalnum()):
            tword += line[tidx]
            tidx += 1

        token = Token(tword, idx, 'V')

        return token, tidx

    # Run the Lexical Analyzer, check if the character is a
    # Digit, Alphabet or Operation.
    def run(self, line):
        idx = 0

        self.tokens = []

        while(idx < len(line)):
            if(line[idx].isdigit()):
                token, idx = self.isNumber(line, idx)
                self.tokens.append(token)
            elif(line[idx].isalpha()):
                token, idx = self.isVariable(line, idx)
                self.tokens.append(token)
            elif(line[idx] in "+-*/="):
                token, idx = Token(line[idx], idx, 'O'), idx + 1
                self.tokens.append(token)          
            else:
                idx += 1

    # Print all Tokens
    def printTokens(self):
        for token in self.tokens:
            print(token)

if __name__ == "__main__":
    lex = LexicalAnalizer()
    
    while(True):
        line = input('line: ')

        if(line == 'q'):
            break    
        
        lex.run(line)
        lex.printTokens()
        print()