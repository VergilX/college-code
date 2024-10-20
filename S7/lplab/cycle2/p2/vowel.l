%{
    int vowelcount = 0;
%}

VOWEL   [AEIOUaeiou]

%%

{VOWEL} { vowelcount++; }
.   ;

%%

int main(void)
{
    printf("Enter sentence: ");
    yylex();

    printf("Number of vowels: %d\n", vowelcount);

    return 0;
}

