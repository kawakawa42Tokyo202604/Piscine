#include <stdio.h>

#ifndef EXERCISE
# define EXERCISE 0
#endif

#if EXERCISE == 0
int ft_strcmp(char *s1, char *s2);

int main(void)
{
    printf("%d\n", ft_strcmp("abc", "abd"));
    return (0);
}

#elif EXERCISE == 1
int ft_strncmp(char *s1, char *s2, unsigned int n);

int main(void)
{
    printf("%d\n", ft_strncmp("abc", "abd", 2));
    return (0);
}

#elif EXERCISE == 2
char *ft_strcat(char *dest, char *src);

int main(void)
{
    char text[32] = "Hello, ";
    printf("%s\n", ft_strcat(text, "42!"));
    return (0);
}

#elif EXERCISE == 3
char *ft_strncat(char *dest, char *src, unsigned int nb);

int main(void)
{
    char text[32] = "Hello, ";
    printf("%s\n", ft_strncat(text, "42!ignored", 3));
    return (0);
}

#elif EXERCISE == 4
char *ft_strstr(char *str, char *to_find);

int main(void)
{
    char *found = ft_strstr("Hello, 42!", "42");
    if (found == NULL)
        return (1);
    printf("%s\n", found);
    return (0);
}

#elif EXERCISE == 5
unsigned int ft_strlcat(char *dest, char *src, unsigned int size);

int main(void)
{
    char text[32] = "Hello, ";
    unsigned int length = ft_strlcat(text, "42!", sizeof(text));
    printf("%s (%u)\n", text, length);
    return (0);
}

#else
# error Unsupported exercise
#endif
