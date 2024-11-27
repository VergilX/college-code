%{
    #include <stdlib.h>
    void yyerror(char *);
    #include "y.tab.h"
%}

%%

[0-9]+  { 
    yylval = atoi(yytext); // very important line received by yacc
    return INTEGER;
} // imported from header generated by yacc
[-+*/\n]  { return *yytext; }  // returns character code
[ \t]   ;   // skip whitespace
.       { yyerror("Invalid character"); }

%%

// works without this
int yywrap(void) {
    return 1;
}