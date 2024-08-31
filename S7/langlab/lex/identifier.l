digit   [0-9]
alpha   [A-Za-z]
%{
    int count;
%}

%%

({alpha})[{digit}|{alpha}]*     ++count;

%%

int main(void) {
    yylex();
    printf("Number of identifiers: %d\n", count);
    return 0;
}
