#include "rush.h"

static int	check_key(int value, char *dict)
{
	char	key[3];

	if (value >= 10)
	{
		key[0] = value / 10 + '0';
		key[1] = value % 10 + '0';
		key[2] = '\0';
	}
	else
	{
		key[0] = value + '0';
		key[1] = '\0';
	}
	return (is_key_in_dict(dict, key));
}

static int	check_chunk_keys(int value, char *dict)
{
	if (value >= 100)
	{
		if (!check_key(value / 100, dict) || !is_key_in_dict(dict, "100"))
			return (0);
	}
	value %= 100;
	if (value == 0)
		return (1);
	if (value < 20)
		return (check_key(value, dict));
	if (!check_key(value / 10 * 10, dict))
		return (0);
	return (value % 10 == 0 || check_key(value % 10, dict));
}

int	check_number_keys(char *str, char *dict)
{
	int	len;
	int	size;
	int	value;

	len = ft_strlen(str);
	if (len == 1 && *str == '0')
		return (is_key_in_dict(dict, "0"));
	while (len > 0)
	{
		size = len % 3;
		if (size == 0)
			size = 3;
		len -= size;
		value = 0;
		while (size-- > 0)
			value = value * 10 + *str++ - '0';
		if (!check_chunk_keys(value, dict))
			return (0);
	}
	return (1);
}
