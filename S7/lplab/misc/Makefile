FLEX_PATH := $(shell dirname $(shell which flex))
LIB_PATH := $(shell readlink -f "$(FLEX_PATH)/../lib")

install: p1.l lex.yy.c
	lex p1.l
	gcc -L $(LIB_PATH) lex.yy.c -lfl

clean:
	rm lex.yy.c
