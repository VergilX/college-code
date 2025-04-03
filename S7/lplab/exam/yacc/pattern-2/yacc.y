%{
    #include <stdio.h>
    int yyerror(char *);
    int yylex(void);
%}

%token CHAR

%%

start:
     prog '\n'  { return 0; }
     |
     ;

prog:
    expr prog expr      { 
                            printf("%d %d %d\n", $1, $2, $3);
                            if (($3 != 0) && ($1 != $3)) {
                                return 1;
                            }
                        }
    |
    ;

expr:
    CHAR
    |
    ;

%%

int yyerror(char *s) {
    printf("Error: %s\n", s);
    return 1;
}

int main() {
    int returncode = yyparse();
    if (returncode == 1)
        printf("Not palindrome\n");
    else printf("Palindrome\n");
    return returncode;
}
