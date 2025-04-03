FLEX_PATH := $(shell dirname $(shell which flex))
LIB_PATH := $(shell readlink -f "$(FLEX_PATH)/../lib")

install: cfilecopy.l
	lex cfilecopy.l
	gcc -L $(LIB_PATH) lex.yy.c -lfl

clean:
	rm lex.yy.c
