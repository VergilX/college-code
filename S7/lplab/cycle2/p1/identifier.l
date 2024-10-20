DIGIT   [0-9]
CHAR    [a-zA-Z]

%%

\n  ;
(_|{CHAR})({DIGIT}|{CHAR}|_)*   { printf("valid identifier\n"); }
.*   { printf("Invalid identifier\n"); }

%%

int main(void)
{
    yylex();

    return 0;
}
