%option noyywrap

%{
	#include <stdio.h>
	#define YY_DECL int yylex()
	#include "parser.tab.h"
%}

%%

[ \t]	;
[0-9]+	{yylval.val = atoi(yytext); return T_INT;}
\n		{return T_NLINE;}
"+"		{return T_PLUS;}
"-"		{return T_MINUS;}
"*"		{return T_MULT;}
"/"		{return T_DIV;}
"("		{return T_LPAR;}
")"		{return T_RPAR;}
"q"		{return T_QUIT;}

%%