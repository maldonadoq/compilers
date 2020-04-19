all: calc

parser.tab.c parser.tab.h: parser.y
	bison -d parser.y

lex.yy.c: scanner.l
	flex scanner.l

calc: lex.yy.c parser.tab.c
	gcc parser.tab.c lex.yy.c -o calc.out

clean:
	rm calc.out parser.tab.c parser.tab.h lex.yy.c