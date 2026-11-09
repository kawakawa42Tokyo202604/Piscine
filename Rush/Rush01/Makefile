CC = cc
CFLAGS = -Wall -Wextra -Werror
NAME = rush-01
SRCS = rush01.c check.c solve.c
HINTS ?= 4 3 2 1 1 2 2 2 4 3 2 1 1 2 2 2

all: $(NAME)

$(NAME): $(SRCS) Makefile
	$(CC) $(CPPFLAGS) $(CFLAGS) $(SRCS) $(LDFLAGS) $(LDLIBS) -o $@

run: $(NAME)
	./$(NAME) "$(HINTS)"

clean:
	$(RM) $(NAME)

fclean: clean

re:
	$(MAKE) fclean
	$(MAKE) all

.PHONY: all run clean fclean re

PYTHON ?= python3

test: $(NAME)
	$(PYTHON) -m unittest discover -s tests -v

.PHONY: test
