#include <stdio.h>

#ifndef EXERCISE
# define EXERCISE 0
#endif

#if EXERCISE == 0
int ft_strlen(char *str);

int main(void)
{
    printf("%d\n", ft_strlen("Hello"));
    return (0);
}

#elif EXERCISE == 1
void ft_putstr(char *str);

int main(void)
{
    ft_putstr("Hello, 42!\n");
    return (0);
}

#elif EXERCISE == 2
void ft_putnbr(int nb);

int main(void)
{
    ft_putnbr(-42);
    putchar('\n');
    return (0);
}

#elif EXERCISE == 3
int ft_atoi(char *str);

int main(void)
{
    printf("%d\n", ft_atoi("  -42"));
    return (0);
}

#elif EXERCISE == 4
void ft_putnbr_base(int nbr, char *base);

int main(void)
{
    ft_putnbr_base(42, "0123456789abcdef");
    putchar('\n');
    return (0);
}

#elif EXERCISE == 5
int ft_atoi_base(char *str, char *base);

int main(void)
{
    printf("%d\n", ft_atoi_base("101010", "01"));
    return (0);
}

#else
# error Unsupported exercise
#endif
