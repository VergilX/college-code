%{
    #include <stdio.h>
    #include <stdlib.h>
    int yylex(void);
    void yyerror(char *);

    #define YYDEBUG 1
%}

%%

start:
     prod '\n'     { return 0; }
     |
     ;

prod:
     |'a' prod 'b'
     ;

%%

void yyerror(char *s) {
    printf("Error: %s\n", s);
}

int main()
{
    int returncode = yyparse();
    if (returncode == 0) {
        printf("Valid string\n");
    }

    return 0;
}
