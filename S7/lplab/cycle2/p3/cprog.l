%{
    #include <fcntl.h>

    int stmt = 0;
    int id = 0;
    int asgt = 0;
    int rel = 0;
    int integer = 0;

    // char *outfile = "output.c";
%}

DATATYPE    int|float|char|double
COND        if|else
KEYWORD     return|printf|main
REL     <|>|==|!=|<=|>=
DIGIT   [0-9]
CHAR    [a-zA-Z]

%%

{REL}   { rel++; }
=   { asgt++; }
;   { stmt++; }
{DATATYPE}|{COND}|{KEYWORD} ;
({CHAR}|_)({CHAR}|{DIGIT}|_)*   { id++; printf("%s\n", yytext); }
{DIGIT}*    { integer++; }
.   ;

%%

int main(int argc, char *argv[])
{
    if (argc != 2) {
        printf("Usage: ./a.out <filename>\n");
        return 1;
    }

    yyin = fopen(argv[1], "r");
    // yyout = open(outfile, O_WRONLY);

    yylex();
    printf("Statements: %d\nIdentifier: %d\nAssignment: %d\nRelational: %d\nInteger: %d\n", stmt, id, asgt, rel, integer);

    return 0;
}
