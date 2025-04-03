%{
    #include <stdlib.h>
    int yyerror(char *);
    #include "y.tab.h"
%}

%%

[a-zA-Z]    {
                yylval = *yytext;
                return CHAR;
            }

"\n"          { return *yytext; }

.           { yyerror("Invalid input"); }

%%
