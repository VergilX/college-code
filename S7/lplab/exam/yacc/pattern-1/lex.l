%{
    #include <stdlib.h>
    #include "y.tab.h"
    void yyerror(char *);
%}

%%

[ab\n]  { return *yytext; }
.       { yyerror("Invalid input"); return 1; }

%%
