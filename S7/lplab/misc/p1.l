VOWEL   [AEIOUaeiou]
CONS    [^AEIOUaeiou\n]

%%

" " ;
{CONS}*{VOWEL}{2,}{CONS}*     { printf("invalid\n"); }
{CONS}*{VOWEL}{CONS}*     { printf("valid\n"); }
.*   { printf("invalid\n"); }

%%

int main(void)
{
    yylex();

    return 0;
}
