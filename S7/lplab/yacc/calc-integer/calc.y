%{
    #include <stdio.h>
    int yylex(void);
    void yyerror(char *);
%}

%token INTEGER

%%

S:
    S expr '\n'     { printf("calc: %d\n", $2); }
    |
    ;

expr:
    INTEGER
    | expr '+' expr     { $$ = $1 + $3; }
    | expr '-' expr     { $$ = $1 - $3; }
    | expr '*' expr     { $$ = $1 * $3; }
    | expr '/' expr     { $$ = (int) ($1 / $3); }
    ;

%%

void yyerror(char *s) {
    fprintf(stderr, "Error: %s\n", s);
}
    
int main() {
    return yyparse();
}



