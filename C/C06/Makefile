CC = cc
CFLAGS = -Wall -Wextra -Werror
EX ?= ex00
EXERCISES = ex00 ex01 ex02 ex03
PROGRAMS = $(addprefix build/,$(EXERCISES))

all: $(PROGRAMS)

build:
	mkdir -p $@

build/ex00: ex00/ft_print_program_name.c Makefile | build
	$(CC) $(CPPFLAGS) $(CFLAGS) ex00/ft_print_program_name.c $(LDFLAGS) $(LDLIBS) -o $@

build/ex01: ex01/ft_print_params.c Makefile | build
	$(CC) $(CPPFLAGS) $(CFLAGS) ex01/ft_print_params.c $(LDFLAGS) $(LDLIBS) -o $@

build/ex02: ex02/ft_rev_params.c Makefile | build
	$(CC) $(CPPFLAGS) $(CFLAGS) ex02/ft_rev_params.c $(LDFLAGS) $(LDLIBS) -o $@

build/ex03: ex03/ft_sort_params.c Makefile | build
	$(CC) $(CPPFLAGS) $(CFLAGS) ex03/ft_sort_params.c $(LDFLAGS) $(LDLIBS) -o $@

run: build/$(EX)
	./build/$(EX) $(ARGS)

clean:
	$(RM) $(PROGRAMS)

fclean: clean

re:
	$(MAKE) fclean
	$(MAKE) all

.PHONY: all run clean fclean re
