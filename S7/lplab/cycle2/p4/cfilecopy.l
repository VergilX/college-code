%%

<INITIAL>{  { printf("begin\n"); }
[^}]*<<EOF>>    { printf("end\n"); }

%%

int main(void)
{
    yyin = fopen("input.c", "r");
    yylex();
    close(yyin);
    return 0;
}
