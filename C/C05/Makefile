CC = cc
CFLAGS = -Wall -Wextra -Werror
EX ?= ex00
EXERCISES = ex00 ex01 ex02 ex03 ex04 ex05 ex06 ex07 ex08
PROGRAMS = $(addprefix build/,$(EXERCISES))

all: $(PROGRAMS)

build:
	mkdir -p $@

build/ex00: main.c ex00/ft_iterative_factorial.c Makefile | build
	$(CC) $(CPPFLAGS) $(CFLAGS) -D EXERCISE=0 main.c ex00/ft_iterative_factorial.c $(LDFLAGS) $(LDLIBS) -o $@

build/ex01: main.c ex01/ft_recursive_factorial.c Makefile | build
	$(CC) $(CPPFLAGS) $(CFLAGS) -D EXERCISE=1 main.c ex01/ft_recursive_factorial.c $(LDFLAGS) $(LDLIBS) -o $@

build/ex02: main.c ex02/ft_iterative_power.c Makefile | build
	$(CC) $(CPPFLAGS) $(CFLAGS) -D EXERCISE=2 main.c ex02/ft_iterative_power.c $(LDFLAGS) $(LDLIBS) -o $@

build/ex03: main.c ex03/ft_recursive_power.c Makefile | build
	$(CC) $(CPPFLAGS) $(CFLAGS) -D EXERCISE=3 main.c ex03/ft_recursive_power.c $(LDFLAGS) $(LDLIBS) -o $@

build/ex04: main.c ex04/ft_fibonacci.c Makefile | build
	$(CC) $(CPPFLAGS) $(CFLAGS) -D EXERCISE=4 main.c ex04/ft_fibonacci.c $(LDFLAGS) $(LDLIBS) -o $@

build/ex05: main.c ex05/ft_sqrt.c Makefile | build
	$(CC) $(CPPFLAGS) $(CFLAGS) -D EXERCISE=5 main.c ex05/ft_sqrt.c $(LDFLAGS) $(LDLIBS) -o $@

build/ex06: main.c ex06/ft_is_prime.c Makefile | build
	$(CC) $(CPPFLAGS) $(CFLAGS) -D EXERCISE=6 main.c ex06/ft_is_prime.c $(LDFLAGS) $(LDLIBS) -o $@

build/ex07: main.c ex07/ft_find_next_prime.c Makefile | build
	$(CC) $(CPPFLAGS) $(CFLAGS) -D EXERCISE=7 main.c ex07/ft_find_next_prime.c $(LDFLAGS) $(LDLIBS) -o $@

build/ex08: main.c ex08/ft_ten_queens_puzzle.c Makefile | build
	$(CC) $(CPPFLAGS) $(CFLAGS) -D EXERCISE=8 main.c ex08/ft_ten_queens_puzzle.c $(LDFLAGS) $(LDLIBS) -o $@

run: build/$(EX)
	./build/$(EX) $(ARGS)

clean:
	$(RM) $(PROGRAMS)

fclean: clean

re:
	$(MAKE) fclean
	$(MAKE) all

.PHONY: all run clean fclean re
