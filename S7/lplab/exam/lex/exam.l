/*
1. Replace computer by science
2. Replace whitespace by underscore
3. Count and display words with length 5
4. Count keywords, digits, chars
*/

%{
    int wc = 0;
    int keywords = 0;
    int digits = 0;
    int chars = 0;

    FILE *in;
    FILE *out;
%}

KEYWORD    if|"else if"|else|int|bool|float|char|void|return
DIGIT       [0-9]
CHAR        [a-zA-Z]

%%

computer|COMPUTER   { chars += 8; ++wc; fprintf(out, "science"); }
" "                 { chars += 1; fprintf(out, "_"); }
{KEYWORD}           { 
                        keywords += 1;
                        ++wc;
                        int n = strlen(yytext);
                        if (n == 5) {
                            fprintf(stdout, "%s\n", yytext);
                        }
                        chars += n;
                        fprintf(out, "%s", yytext);
                    }
{DIGIT}             { ++digits; fprintf(out, "%s", yytext); }
{CHAR}{5}           { ++wc; fprintf(out, "%s", yytext); printf("%s\n", yytext); }
{CHAR}              { ++chars; fprintf(out, "%s", yytext); }
.                   { fprintf(out, "%s", yytext); }

%%

int yywrap() {
    return 1;
}

int main(void)
{
    in = fopen("input.txt", "r");
    yyin = in;

    out = fopen("output.txt", "w");
    yylex();

    printf("Word count: %d\nKeywords: %d\nDigits: %d\nCharacters: %d\n", wc, keywords, digits, chars);
    return 0;
}
