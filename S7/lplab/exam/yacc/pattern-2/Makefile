FLEX_PATH := $(shell dirname $(shell which flex))
LIB_PATH := $(shell readlink -f "$(FLEX_PATH)/../lib")

install:
	yacc -d yacc.y
	lex lex.l
	gcc -L $(LIB_PATH) y.tab.c lex.yy.c -lfl

report:
	yacc -t --report=state -d yacc.y
	lex lex.l
	gcc -L $(LIB_PATH) y.tab.c lex.yy.c -lfl

debug:
	yacc -t yacc.y
	lex lex.l
	gcc -L $(LIB_PATH) y.tab.c lex.yy.c -lfl

compile:
	gcc -L $(LIB_PATH) y.tab.c lex.yy.c -lfl

clean:
	rm lex.yy.c
	rm y.tab.c
