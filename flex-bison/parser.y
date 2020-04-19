%{

#include <stdio.h>
#include <stdlib.h>

extern int yylex();
extern int yyparse();
extern FILE* yyin;

void yyerror(const char* s);
%}

%union {
	int val;
}

%token<val> T_INT
%token T_PLUS T_MINUS T_MULT T_DIV T_LPAR T_RPAR
%token T_NLINE T_QUIT

%left T_PLUS T_MINUS
%left T_MULT T_DIV

%type<val> expr

%start calc

%%

calc:
    | calc line
    ;

line: T_NLINE
    | expr T_NLINE  { printf(" %i\n", $1); }
    | T_QUIT        { exit(0); }
    ;

expr: T_INT                 { $$ = $1; }
    | expr T_PLUS expr      { $$ = $1 + $3; }
    | expr T_MINUS expr     { $$ = $1 - $3; }
    | expr T_MULT expr      { $$ = $1 * $3; }
    | expr T_DIV expr       {
                                if($3 == 0){
                                    printf("Error: Can't divide by 0\n");
                                }
                                else{
                                    $$ = $1 / $3;
                                }
                            }
    | T_LPAR expr T_RPAR    { $$ = $2; }
    ;

%%

int main() {
	yyin = stdin;

	do {
		yyparse();
	} while(!feof(yyin));

	return 0;
}

void yyerror(const char* s) {
	fprintf(stderr, "Error: %s\n", s);
	exit(1);
}