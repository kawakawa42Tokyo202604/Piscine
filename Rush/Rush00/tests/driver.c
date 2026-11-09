#include <stdlib.h>

void rush(int width, int height);

int main(int argc, char **argv)
{
	if (argc != 3)
		return (1);
	rush(atoi(argv[1]), atoi(argv[2]));
	return (0);
}
