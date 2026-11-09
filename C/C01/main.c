#include <stdio.h>

#ifndef EXERCISE
# define EXERCISE 0
#endif

#if EXERCISE == 0
void ft_ft(int *nbr);

int main(void)
{
    int value = 0;
    ft_ft(&value);
    printf("%d\n", value);
    return (0);
}

#elif EXERCISE == 1
void ft_ultimate_ft(int *********nbr);

int main(void)
{
    int value = 0;
    int *p1 = &value;
    int **p2 = &p1;
    int ***p3 = &p2;
    int ****p4 = &p3;
    int *****p5 = &p4;
    int ******p6 = &p5;
    int *******p7 = &p6;
    int ********p8 = &p7;
    ft_ultimate_ft(&p8);
    printf("%d\n", value);
    return (0);
}

#elif EXERCISE == 2
void ft_swap(int *a, int *b);

int main(void)
{
    int a = 1;
    int b = 2;
    ft_swap(&a, &b);
    printf("%d %d\n", a, b);
    return (0);
}

#elif EXERCISE == 3
void ft_div_mod(int a, int b, int *div, int *mod);

int main(void)
{
    int quotient;
    int remainder;
    ft_div_mod(17, 5, &quotient, &remainder);
    printf("%d %d\n", quotient, remainder);
    return (0);
}

#elif EXERCISE == 4
void ft_ultimate_div_mod(int *a, int *b);

int main(void)
{
    int a = 17;
    int b = 5;
    ft_ultimate_div_mod(&a, &b);
    printf("%d %d\n", a, b);
    return (0);
}

#elif EXERCISE == 5
void ft_putstr(char *str);

int main(void)
{
    ft_putstr("Hello, 42!\n");
    return (0);
}

#elif EXERCISE == 6
int ft_strlen(char *str);

int main(void)
{
    printf("%d\n", ft_strlen("Hello"));
    return (0);
}

#elif EXERCISE == 7
void ft_rev_int_tab(int *tab, int size);

int main(void)
{
    int values[] = {1, 2, 3};
    ft_rev_int_tab(values, 3);
    printf("%d %d %d\n", values[0], values[1], values[2]);
    return (0);
}

#elif EXERCISE == 8
void ft_sort_int_tab(int *tab, int size);

int main(void)
{
    int values[] = {3, 1, 2};
    ft_sort_int_tab(values, 3);
    printf("%d %d %d\n", values[0], values[1], values[2]);
    return (0);
}

#else
# error Unsupported exercise
#endif
