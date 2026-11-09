CC = cc
CFLAGS = -Wall -Wextra -Werror
PATTERN ?= 00
NAME = rush-$(PATTERN)
SRCS = main.c ft_putchar.c rush$(PATTERN).c
PROGRAMS = rush-00 rush-01 rush-02 rush-03 rush-04

all: $(NAME)

$(NAME): $(SRCS) Makefile
	$(CC) $(CPPFLAGS) $(CFLAGS) $(SRCS) $(LDFLAGS) $(LDLIBS) -o $@

run: $(NAME)
	./$(NAME)

clean:
	$(RM) $(PROGRAMS)

fclean: clean

re:
	$(MAKE) fclean
	$(MAKE) all

.PHONY: all run clean fclean re

PYTHON ?= python3

test:
	CC="$(CC)" TEST_CFLAGS="$(CFLAGS)" $(PYTHON) -m unittest discover -s tests -v

.PHONY: test
