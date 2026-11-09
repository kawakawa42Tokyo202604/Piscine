# Piscine C 03

## English

C functions for comparing, joining, and searching strings. They account for string endings and available destination capacity.

For example, `ft_strstr("hello world", "world")` returns a pointer to the start of the matching `world`.

### Exercises

| Location | Source | Behavior |
| --- | --- | --- |
| ex00 | [ft_strcmp.c](ex00/ft_strcmp.c) | Compare strings |
| ex01 | [ft_strncmp.c](ex01/ft_strncmp.c) | Compare up to a character limit |
| ex02 | [ft_strcat.c](ex02/ft_strcat.c) | Append a string |
| ex03 | [ft_strncat.c](ex03/ft_strncat.c) | Append up to a character limit |
| ex04 | [ft_strstr.c](ex04/ft_strstr.c) | Find a substring |
| ex05 | [ft_strlcat.c](ex05/ft_strlcat.c) | Append within destination capacity |

### Build and run

Requires a C compiler and Make.

```sh
make
make run EX=ex00
```

Combines the supplied [main.c](main.c) with each exercise to create executables such as `build/ex00`. Select an exercise with `EX` and pass runtime arguments through `ARGS`.

`ex00` compares `abc` with `abd` and prints a negative value because the first string is smaller.

## 日本語

文字列を比較する、後ろにつなぐ、中から別の文字列を探す、といったC関数を作る演習です。文字列の終わりや書き込み先の長さを意識して処理します。

例えば `ft_strstr("hello world", "world")` は、一致した `world` の先頭位置を返します。

### 演習

| 場所 | ソース | 処理 |
| --- | --- | --- |
| ex00 | [ft_strcmp.c](ex00/ft_strcmp.c) | 2つの文字列の大小を比較 |
| ex01 | [ft_strncmp.c](ex01/ft_strncmp.c) | 指定した文字数まで比較 |
| ex02 | [ft_strcat.c](ex02/ft_strcat.c) | 文字列を末尾につなぐ |
| ex03 | [ft_strncat.c](ex03/ft_strncat.c) | 指定した文字数だけ末尾につなぐ |
| ex04 | [ft_strstr.c](ex04/ft_strstr.c) | 文字列の中から別の文字列を探す |
| ex05 | [ft_strlcat.c](ex05/ft_strlcat.c) | 保存先の容量内で文字列をつなぐ |

### ビルドと実行

Cコンパイラ・Make が必要です。

```sh
make
make run EX=ex00
```

付属の [main.c](main.c) と各演習のソースを組み合わせ、`build/ex00` などの実行ファイルを生成します。 `EX` で演習を選び、`ARGS` で実行時の引数を渡せます。

`ex00` の実行例は `abc` と `abd` を比較し、前者が小さいことを表す負の値を表示します。
