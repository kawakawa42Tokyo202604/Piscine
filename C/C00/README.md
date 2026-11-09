# Piscine C 00

## English

C functions for printing characters and integers. Display the alphabet, identify a number's sign, and enumerate digit combinations using conditions and loops.

For example, `ft_putchar('A')` prints one `A`. The digit-combination function in `ex08` is still in progress.

### Exercises

| Location | Source | Behavior |
| --- | --- | --- |
| ex00 | [ft_putchar.c](ex00/ft_putchar.c) | Print one character |
| ex01 | [ft_print_alphabet.c](ex01/ft_print_alphabet.c) | Print a through z |
| ex02 | [ft_print_reverse_alphabet.c](ex02/ft_print_reverse_alphabet.c) | Print z through a |
| ex03 | [ft_print_numbers.c](ex03/ft_print_numbers.c) | Print digits 0 through 9 |
| ex04 | [ft_is_negative.c](ex04/ft_is_negative.c) | Print whether an integer is negative |
| ex05 | [ft_print_comb.c](ex05/ft_print_comb.c) | Print combinations of three distinct digits |
| ex06 | [ft_print_comb2.c](ex06/ft_print_comb2.c) | Print pairs of two-digit numbers |
| ex07 | [ft_putnbr.c](ex07/ft_putnbr.c) | Print an integer |
| ex08 | [ft_print_combn.c](ex08/ft_print_combn.c) | Print combinations with a specified digit count; in progress |

### Compile an example

Use a C compiler from this directory.

```sh
cc -Wall -Wextra -Werror -c ex00/ft_putchar.c -o ft_putchar.o
```

This creates an object file. To run the function, link its source with a `main.c` that calls it.

## 日本語

文字や整数を端末に表示するC関数を作る演習です。アルファベットを順に表示する、正負を判定する、数字の組み合わせを列挙するといった処理を、条件分岐と繰り返しで実装します。

例えば `ft_putchar('A')` は `A` を1文字表示します。`ex08` の数字の組み合わせの出力は実装途中です。

### 演習

| 場所 | ソース | 処理 |
| --- | --- | --- |
| ex00 | [ft_putchar.c](ex00/ft_putchar.c) | 1文字を表示 |
| ex01 | [ft_print_alphabet.c](ex01/ft_print_alphabet.c) | a〜zを表示 |
| ex02 | [ft_print_reverse_alphabet.c](ex02/ft_print_reverse_alphabet.c) | z〜aを表示 |
| ex03 | [ft_print_numbers.c](ex03/ft_print_numbers.c) | 0〜9を表示 |
| ex04 | [ft_is_negative.c](ex04/ft_is_negative.c) | 整数が負かどうかを表示 |
| ex05 | [ft_print_comb.c](ex05/ft_print_comb.c) | 異なる3桁の組み合わせを表示 |
| ex06 | [ft_print_comb2.c](ex06/ft_print_comb2.c) | 2つの2桁の数の組み合わせを表示 |
| ex07 | [ft_putnbr.c](ex07/ft_putnbr.c) | 整数を表示 |
| ex08 | [ft_print_combn.c](ex08/ft_print_combn.c) | 指定桁数の数字の組み合わせを表示（実装途中） |

### ビルド例

Cコンパイラを使用し、このディレクトリで実行します。

```sh
cc -Wall -Wextra -Werror -c ex00/ft_putchar.c -o ft_putchar.o
```

上の例はオブジェクトファイルを生成します。関数の動作を確かめる場合は、呼び出し用の `main.c` と必要なソースを指定してリンクします。
