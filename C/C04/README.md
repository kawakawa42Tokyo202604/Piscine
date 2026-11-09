# Piscine C 04

## English

C exercises for displaying integers and converting numeric text to integer values. They also support different bases, such as binary and hexadecimal, which use different sets of digits.

For example, `ft_atoi("42")` returns the integer `42`.

### Exercises

| Location | Source | Behavior |
| --- | --- | --- |
| ex00 | [ft_strlen.c](ex00/ft_strlen.c) | Count characters |
| ex01 | [ft_putstr.c](ex01/ft_putstr.c) | Print a string |
| ex02 | [ft_putnbr.c](ex02/ft_putnbr.c) | Print an integer |
| ex03 | [ft_atoi.c](ex03/ft_atoi.c) | Parse an integer string |
| ex04 | [ft_putnbr_base.c](ex04/ft_putnbr_base.c) | Print an integer in a specified base |
| ex05 | [ft_atoi_base.c](ex05/ft_atoi_base.c) | Parse a string in a specified base |

### Build and run

Requires a C compiler and Make.

```sh
make
make run EX=ex00
```

Combines the supplied [main.c](main.c) with each exercise to create executables such as `build/ex00`. Select an exercise with `EX` and pass runtime arguments through `ARGS`.

`ex00` prints `5`, the length of `Hello`.

## 日本語

整数を文字として表示したり、数字の文字列を整数に変換したりするC演習です。10進数に加え、2進数・16進数など、数を表す桁の種類（基数）を指定する変換も扱います。

例えば `ft_atoi("42")` は整数の `42` を返します。

### 演習

| 場所 | ソース | 処理 |
| --- | --- | --- |
| ex00 | [ft_strlen.c](ex00/ft_strlen.c) | 文字数を数える |
| ex01 | [ft_putstr.c](ex01/ft_putstr.c) | 文字列を表示 |
| ex02 | [ft_putnbr.c](ex02/ft_putnbr.c) | 整数を表示 |
| ex03 | [ft_atoi.c](ex03/ft_atoi.c) | 数字の文字列を整数に変換 |
| ex04 | [ft_putnbr_base.c](ex04/ft_putnbr_base.c) | 指定した基数で整数を表示 |
| ex05 | [ft_atoi_base.c](ex05/ft_atoi_base.c) | 指定した基数の文字列を整数に変換 |

### ビルドと実行

Cコンパイラ・Make が必要です。

```sh
make
make run EX=ex00
```

付属の [main.c](main.c) と各演習のソースを組み合わせ、`build/ex00` などの実行ファイルを生成します。 `EX` で演習を選び、`ARGS` で実行時の引数を渡せます。

`ex00` の実行例は `Hello` の文字数である `5` を表示します。
