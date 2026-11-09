#include <stdio.h>

#ifndef EXERCISE
# define EXERCISE 0
#endif

#if EXERCISE == 0
int ft_iterative_factorial(int nb);

int main(void)
{
    printf("%d\n", ft_iterative_factorial(5));
    return (0);
}

#elif EXERCISE == 1
int ft_recursive_factorial(int nb);

int main(void)
{
    printf("%d\n", ft_recursive_factorial(5));
    return (0);
}

#elif EXERCISE == 2
int ft_iterative_power(int nb, int power);

int main(void)
{
    printf("%d\n", ft_iterative_power(2, 10));
    return (0);
}

#elif EXERCISE == 3
int ft_recursive_power(int nb, int power);

int main(void)
{
    printf("%d\n", ft_recursive_power(2, 10));
    return (0);
}

#elif EXERCISE == 4
int ft_fibonacci(int index);

int main(void)
{
    printf("%d\n", ft_fibonacci(10));
    return (0);
}

#elif EXERCISE == 5
int ft_sqrt(int nb);

int main(void)
{
    printf("%d\n", ft_sqrt(81));
    return (0);
}

#elif EXERCISE == 6
int ft_is_prime(int nb);

int main(void)
{
    printf("%d\n", ft_is_prime(97));
    return (0);
}

#elif EXERCISE == 7
int ft_find_next_prime(int nb);

int main(void)
{
    printf("%d\n", ft_find_next_prime(100));
    return (0);
}

#elif EXERCISE == 8
int ft_ten_queens_puzzle(void);

int main(void)
{
    int count = ft_ten_queens_puzzle();
    printf("solutions: %d\n", count);
    return (0);
}

#else
# error Unsupported exercise
#endif
