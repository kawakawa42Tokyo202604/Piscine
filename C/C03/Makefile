CC = cc
CFLAGS = -Wall -Wextra -Werror
EX ?= ex00
EXERCISES = ex00 ex01 ex02 ex03 ex04 ex05
PROGRAMS = $(addprefix build/,$(EXERCISES))

all: $(PROGRAMS)

build:
	mkdir -p $@

build/ex00: main.c ex00/ft_strcmp.c Makefile | build
	$(CC) $(CPPFLAGS) $(CFLAGS) -D EXERCISE=0 main.c ex00/ft_strcmp.c $(LDFLAGS) $(LDLIBS) -o $@

build/ex01: main.c ex01/ft_strncmp.c Makefile | build
	$(CC) $(CPPFLAGS) $(CFLAGS) -D EXERCISE=1 main.c ex01/ft_strncmp.c $(LDFLAGS) $(LDLIBS) -o $@

build/ex02: main.c ex02/ft_strcat.c Makefile | build
	$(CC) $(CPPFLAGS) $(CFLAGS) -D EXERCISE=2 main.c ex02/ft_strcat.c $(LDFLAGS) $(LDLIBS) -o $@

build/ex03: main.c ex03/ft_strncat.c Makefile | build
	$(CC) $(CPPFLAGS) $(CFLAGS) -D EXERCISE=3 main.c ex03/ft_strncat.c $(LDFLAGS) $(LDLIBS) -o $@

build/ex04: main.c ex04/ft_strstr.c Makefile | build
	$(CC) $(CPPFLAGS) $(CFLAGS) -D EXERCISE=4 main.c ex04/ft_strstr.c $(LDFLAGS) $(LDLIBS) -o $@

build/ex05: main.c ex05/ft_strlcat.c Makefile | build
	$(CC) $(CPPFLAGS) $(CFLAGS) -D EXERCISE=5 main.c ex05/ft_strlcat.c $(LDFLAGS) $(LDLIBS) -o $@

run: build/$(EX)
	./build/$(EX) $(ARGS)

clean:
	$(RM) $(PROGRAMS)

fclean: clean

re:
	$(MAKE) fclean
	$(MAKE) all

.PHONY: all run clean fclean re
