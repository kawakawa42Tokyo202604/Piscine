CC = cc
CFLAGS = -Wall -Wextra -Werror
NAME = build/example
LIBRARY = ex01/libft.a

all: $(NAME)

$(LIBRARY): FORCE
	$(MAKE) -C ex01

$(NAME): main.c ex01/includes/ft.h $(LIBRARY) | build
	$(CC) $(CPPFLAGS) $(CFLAGS) -I ex01/includes main.c $(LIBRARY) $(LDFLAGS) $(LDLIBS) -o $@

build:
	mkdir -p $@

run: $(NAME)
	./$(NAME)

clean:
	$(MAKE) -C ex01 clean
	$(RM) $(NAME)

fclean:
	$(MAKE) -C ex01 fclean
	$(RM) $(NAME)

re:
	$(MAKE) fclean
	$(MAKE) all

FORCE:

.PHONY: all run clean fclean re FORCE
